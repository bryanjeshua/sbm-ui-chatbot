"""
SBM UI 2024 Chatbot - FastAPI Backend
Peraturan Rektor Universitas Indonesia Nomor 16 Tahun 2024
"""
import os
import re
import json
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from rules_engine import SBM_UI_2024, search_rules, format_rupiah, LAMPIRAN_I, LAMPIRAN_II, LAMPIRAN_III, LAMPIRAN_IV, LAMPIRAN_V, LAMPIRAN_VI, LAMPIRAN_VII

app = FastAPI(title="SBM UI 2024 Chatbot")

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# ---------------------------------------------------------------------------
# Helper: flatten the rules tree into a table-friendly list
# ---------------------------------------------------------------------------

def _is_usd_context(path: str) -> bool:
    """Check if the path context indicates USD values."""
    p = path.lower()
    return "luar_negeri" in p or "luar negeri" in p


def _fmt(amount, is_usd: bool = False) -> str:
    """Format a numeric amount as Rupiah or USD."""
    if isinstance(amount, str):
        return amount
    if is_usd:
        return f"USD {amount:,.0f}".replace(",", ".")
    return format_rupiah(amount)


def flatten_lampiran(obj, lampiran_key: str, lampiran_name: str, path: str = "", results: list = None) -> list:
    if results is None:
        results = []

    if isinstance(obj, dict):
        uraian_default = path.split(" > ")[-1].replace("_", " ").title() if path else ""
        uraian = obj.get("uraian", uraian_default)
        satuan = obj.get("satuan", "-")
        is_usd = _is_usd_context(path)

        # Leaf node with single besaran
        if "besaran" in obj and ("satuan" in obj or "uraian" in obj):
            besaran = obj["besaran"]
            results.append({
                "lampiran": lampiran_key,
                "lampiran_nama": lampiran_name,
                "path": path,
                "uraian": uraian,
                "satuan": satuan,
                "besaran": _fmt(besaran, is_usd),
                "besaran_raw": besaran if isinstance(besaran, (int, float)) else 0,
            })
            return results

        # Leaf: per-kota tiket pesawat {"bisnis": ..., "ekonomi": ...}
        if "bisnis" in obj and "ekonomi" in obj and len(obj) <= 2:
            city = path.split(" > ")[-1]
            results.append({
                "lampiran": lampiran_key,
                "lampiran_nama": lampiran_name,
                "path": path,
                "uraian": f"Tiket Pesawat ke {city}",
                "satuan": "O/PP",
                "besaran": f"Bisnis: {_fmt(obj['bisnis'], is_usd)} / Ekonomi: {_fmt(obj['ekonomi'], is_usd)}",
                "besaran_raw": obj["bisnis"] if isinstance(obj["bisnis"], (int, float)) else 0,
            })
            return results

        # Leaf: besaran_bisnis / besaran_ekonomi (tiket pesawat)
        if "besaran_bisnis" in obj and "besaran_ekonomi" in obj:
            b_bisnis = obj["besaran_bisnis"]
            b_ekonomi = obj["besaran_ekonomi"]
            wilayah = obj.get("wilayah", "")
            label = f"{uraian} ({wilayah})" if wilayah else uraian
            results.append({
                "lampiran": lampiran_key,
                "lampiran_nama": lampiran_name,
                "path": path,
                "uraian": label,
                "satuan": satuan,
                "besaran": f"Bisnis: {_fmt(b_bisnis, is_usd)} / Ekonomi: {_fmt(b_ekonomi, is_usd)}",
                "besaran_raw": b_bisnis if isinstance(b_bisnis, (int, float)) else 0,
            })
            return results

        # Leaf: besaran_halfday / besaran_fullday / besaran_fullboard (paket rapat)
        if "besaran_halfday" in obj:
            hd = obj["besaran_halfday"]
            fd = obj.get("besaran_fullday", 0)
            fb = obj.get("besaran_fullboard", 0)
            results.append({
                "lampiran": lampiran_key,
                "lampiran_nama": lampiran_name,
                "path": path,
                "uraian": uraian,
                "satuan": satuan,
                "besaran": f"Half-day: {_fmt(hd)} / Full-day: {_fmt(fd)} / Fullboard: {_fmt(fb)}",
                "besaran_raw": fb if isinstance(fb, (int, float)) else 0,
            })
            return results

        # Leaf: kategori pegawai A/B/C/D/E (penginapan DN, uang harian LN)
        if all(k in obj for k in ("A", "B", "C", "D", "E")) and "satuan" in obj:
            parts = [f"Kat {k}: {_fmt(obj[k], is_usd)}" for k in ("A", "B", "C", "D", "E")]
            results.append({
                "lampiran": lampiran_key,
                "lampiran_nama": lampiran_name,
                "path": path,
                "uraian": uraian,
                "satuan": satuan,
                "besaran": " / ".join(parts),
                "besaran_raw": obj["A"] if isinstance(obj["A"], (int, float)) else 0,
            })
            return results

        # Leaf: luar_kota / dalam_kota_lebih_8_jam / diklat (uang harian DN)
        if "luar_kota" in obj and "diklat" in obj and "satuan" in obj:
            lk = obj["luar_kota"]
            dk = obj.get("dalam_kota_lebih_8_jam", 0)
            dkl = obj["diklat"]
            results.append({
                "lampiran": lampiran_key,
                "lampiran_nama": lampiran_name,
                "path": path,
                "uraian": uraian,
                "satuan": satuan,
                "besaran": f"Luar Kota: {_fmt(lk)} / Dalam Kota >8jam: {_fmt(dk)} / Diklat: {_fmt(dkl)}",
                "besaran_raw": lk if isinstance(lk, (int, float)) else 0,
            })
            return results

        for key, value in obj.items():
            if key in ("nama", "catatan", "penjelasan", "catatan_list", "wilayah"):
                continue
            child_path = f"{path} > {key}" if path else key

            # Handle plain numeric leaf values (e.g. province rates)
            if isinstance(value, (int, float)):
                results.append({
                    "lampiran": lampiran_key,
                    "lampiran_nama": lampiran_name,
                    "path": path,
                    "uraian": key.replace("_", " ").title(),
                    "satuan": _infer_satuan(path),
                    "besaran": _fmt(value, is_usd),
                    "besaran_raw": value,
                })
            elif isinstance(value, str) and key not in ("nama", "catatan"):
                # Skip pure string metadata
                pass
            else:
                flatten_lampiran(value, lampiran_key, lampiran_name, child_path, results)

    return results


def _infer_satuan(path: str) -> str:
    """Infer unit from the path context."""
    p = path.lower()
    if "penginapan" in p:
        return "O/H"
    if "uang_harian" in p or "harian" in p:
        return "O/H"
    if "sewa_kendaraan" in p:
        return "H"
    return "-"


def build_browse_data() -> dict:
    lampiran_map = {
        "I": ("Kegiatan Pendidikan", LAMPIRAN_I),
        "II": ("Kegiatan Kemahasiswaan", LAMPIRAN_II),
        "III": ("Penelitian/Inovasi/Pengabdian Masyarakat", LAMPIRAN_III),
        "IV": ("Operasional Manajemen", LAMPIRAN_IV),
        "V": ("Honorarium Kegiatan", LAMPIRAN_V),
        "VI": ("Perjalanan Dinas", LAMPIRAN_VI),
        "VII": ("Penerimaan Mahasiswa Baru", LAMPIRAN_VII),
    }

    all_data = {}
    for key, (name, data) in lampiran_map.items():
        rows = flatten_lampiran(data, key, name)
        all_data[key] = {"nama": name, "rows": rows}

    return all_data


BROWSE_DATA = build_browse_data()


# ---------------------------------------------------------------------------
# Build a compact text representation of all rules for the LLM context
# ---------------------------------------------------------------------------

def _readable_path(path: str, uraian: str = "") -> str:
    """Build a readable context breadcrumb for the LLM.

    When the last path segment IS the uraian key, it's redundant — drop it.
    When it differs (e.g. a province/city name), it's essential context — keep all parts.
    """
    parts = path.split(" > ")

    def _norm(s: str) -> str:
        return re.sub(r"^\d+_", "", s).replace("_", " ").strip().lower()

    last_norm = _norm(parts[-1])
    uraian_norm = uraian.strip().lower()

    if uraian_norm and last_norm != uraian_norm:
        # Last part is context (province/city/region), not the uraian — include all
        relevant = parts
    else:
        # Last part mirrors the uraian — drop it to avoid repetition
        relevant = parts[:-1] if len(parts) > 1 else parts

    return " > ".join(p.replace("_", " ").strip() for p in relevant)


def build_rules_context() -> str:
    lines = ["STANDAR BIAYA UI 2024 - DATA LENGKAP\n"]
    for lamp_key, lamp_info in BROWSE_DATA.items():
        lines.append(f"\n=== LAMPIRAN {lamp_key}: {lamp_info['nama'].upper()} ===")
        for row in lamp_info["rows"]:
            uraian = row["uraian"] or row["path"].split(" > ")[-1]
            ctx = _readable_path(row["path"], uraian)
            prefix = f"[{ctx}] " if ctx else ""
            lines.append(f"- {prefix}{uraian} | Satuan: {row['satuan']} | Besaran: {row['besaran']}")
    return "\n".join(lines)


RULES_CONTEXT = build_rules_context()

SYSTEM_PROMPT = f"""Kamu adalah asisten ahli Standar Biaya Universitas Indonesia (SB UI) Tahun 2024, berdasarkan Peraturan Rektor UI Nomor 16 Tahun 2024.

TUGAS:
- Jawab pertanyaan pengguna tentang standar biaya, tarif, honorarium, tunjangan, dan biaya operasional di lingkungan UI.
- Selalu berikan angka/tarif yang TEPAT sesuai data di bawah.
- Jawab dalam Bahasa Indonesia.
- Jika ada beberapa tarif yang relevan, tampilkan semuanya dalam format tabel yang rapi.
- Sebutkan satuan (O/J, O/K, O/H, dll) dan jelaskan singkatan jika perlu.
- Jika pertanyaan tidak terkait SBM UI, jelaskan bahwa kamu hanya bisa menjawab tentang Standar Biaya UI 2024.
- JANGAN pernah menjawab "tidak ada data" untuk topik yang memang ada dalam data — cari dengan teliti di semua konteks.

CARA MEMBACA DATA:
Setiap baris data memiliki format: [konteks/jalur] Nama Peran | Satuan | Besaran
Konteks dalam kurung siku menunjukkan di mana tarif itu berlaku (misal: "8 ujian tugas akhir > vokasi").
GUNAKAN KONTEKS INI untuk memilih tarif yang tepat sesuai pertanyaan.

PENANGANAN AMBIGUITAS:
Banyak peran (ketua penguji, anggota penguji, narasumber, moderator, fasilitator, dll) memiliki TARIF BERBEDA tergantung konteksnya.
- Jika konteks sudah jelas dari pertanyaan → berikan tarif yang sesuai konteks tersebut.
- Jika konteks TIDAK jelas (misal: hanya "honorarium ketua penguji" tanpa menyebut program) → TAMPILKAN SEMUA TARIF yang relevan dengan keterangan konteksnya, jangan hanya satu.
- Jangan pernah memilih satu tarif secara acak jika ada beberapa tarif untuk peran yang sama.

PERAN-PERAN YANG PUNYA TARIF BERBEDA PER KONTEKS (selalu cek konteks):
1. Ketua Penguji / Anggota Penguji Tugas Akhir: berbeda untuk Vokasi, S1, S1 Internasional, S2/Spesialis/Profesi, S3 (5 jenis ujian berbeda)
2. Narasumber: berbeda untuk Seminar Nasional, Seminar Internasional, Pelatihan Internal, Tata Kelola TI, OBM
3. Moderator: berbeda untuk Seminar (Nasional vs Internasional) dan Konferensi Internasional (3 kategori H-index)
4. Fasilitator: berbeda untuk Seminar (Nasional vs Internasional), Pelatihan Internal (Dosen/Tendik/Mahasiswa), Konferensi
5. Panitia (Ketua/Anggota): berbeda per jenis kegiatan — Kepanitiaan umum, Rapat Luar Kantor, Konferensi Internasional, Mini Simposium, PMB
6. Reviewer: berbeda per jenis — Jurnal (3 tier), Konferensi Internasional (abstrak/full, 3 H-index), Akreditasi, PKM
7. Pembimbing Tugas Akhir / Magang: berbeda per jenjang (D3, D4, S1, Profesi, S2, S3)
8. Penguji Luar Negeri: berbeda per jenjang (S1=USD 100, S2=USD 150, S3 datang=Rp8.4jt / tele=USD 300)
9. Uang Harian DN: berbeda per provinsi (34 provinsi) dan tipe (luar kota, dalam kota >8jam, diklat)
10. Penginapan DN: berbeda per provinsi dan kategori pegawai (A, B, C/D, E)

ATURAN TIKET PESAWAT DALAM NEGERI (LAMPIRAN VI):
- Batas atas (at cost). Kategori A: kelas BISNIS. Kategori B-E: kelas EKONOMI.
- Jika ditanya untuk jabatan tertentu, tentukan kategorinya dan berikan tarif kelas yang sesuai + tampilkan keduanya.

KATEGORI PEGAWAI (Pasal 7):
A: Rektor, Wakil Rektor, Dekan, Sekretaris Universitas, Kepala Badan, Direktur Vokasi (pimpinan tertinggi)
B: Kepala Satuan, Direktur, Kepala Biro, Ketua Departemen, PNS Gol IVc+, Wakil Dekan, Kepala RS UI
C: Manajer, Ketua Prodi, Kepala Lab, PNS Gol IIIc-IVb
D: Asisten Deputi, Kepala Seksi, Koordinator, Wakil/Asisten Manajer
E: Pegawai UI selain kategori A, B, C, D
(Jika jabatan struktural dan pangkat/golongan berbeda kategori → gunakan yang LEBIH TINGGI)

SATUAN: B=Bulan, H=Hari, J=Jam, O=Orang, Mhs=Mahasiswa, K=Kegiatan, P=Paket, PP=Pulang-Pergi, T=Tahun, U=Unit

{RULES_CONTEXT}
"""


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index():
    html_path = STATIC_DIR / "index.html"
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))


@app.get("/api/browse")
async def browse():
    return JSONResponse(content=BROWSE_DATA)


@app.get("/api/search")
async def search(q: str = ""):
    if not q or len(q) < 2:
        return JSONResponse(content={"results": []})
    results = search_rules(q)
    formatted = []
    is_usd = lambda p: "luar_negeri" in p.lower() or "luar negeri" in p.lower()
    for path, item in results[:50]:
        if not isinstance(item, dict):
            continue
        uraian = item.get("uraian", "")
        satuan = item.get("satuan", "-")
        usd = is_usd(path)

        if "besaran" in item:
            besaran = item["besaran"]
            besaran_str = _fmt(besaran, usd) if isinstance(besaran, (int, float)) else str(besaran)
            formatted.append({"path": path, "uraian": uraian, "satuan": satuan, "besaran": besaran_str})
        elif "bisnis" in item and "ekonomi" in item and len(item) <= 2:
            city = path.split(" > ")[-1]
            formatted.append({"path": path, "uraian": f"Tiket Pesawat ke {city}", "satuan": "O/PP",
                              "besaran": f"Bisnis: {_fmt(item['bisnis'], usd)} / Ekonomi: {_fmt(item['ekonomi'], usd)}"})
        elif "besaran_bisnis" in item and "besaran_ekonomi" in item:
            w = item.get("wilayah", "")
            label = f"{uraian} ({w})" if w else uraian
            formatted.append({"path": path, "uraian": label, "satuan": satuan,
                              "besaran": f"Bisnis: {_fmt(item['besaran_bisnis'], usd)} / Ekonomi: {_fmt(item['besaran_ekonomi'], usd)}"})
        elif "besaran_halfday" in item:
            formatted.append({"path": path, "uraian": uraian, "satuan": satuan,
                              "besaran": f"Half-day: {_fmt(item['besaran_halfday'])} / Full-day: {_fmt(item.get('besaran_fullday', 0))} / Fullboard: {_fmt(item.get('besaran_fullboard', 0))}"})
        elif all(k in item for k in ("A", "B", "C", "D", "E")) and "satuan" in item:
            parts = " / ".join(f"Kat {k}: {_fmt(item[k], usd)}" for k in ("A", "B", "C", "D", "E"))
            formatted.append({"path": path, "uraian": uraian, "satuan": satuan, "besaran": parts})
        elif "luar_kota" in item and "diklat" in item:
            formatted.append({"path": path, "uraian": uraian, "satuan": satuan,
                              "besaran": f"Luar Kota: {_fmt(item['luar_kota'])} / Dalam Kota >8jam: {_fmt(item.get('dalam_kota_lebih_8_jam', 0))} / Diklat: {_fmt(item['diklat'])}"})
    return JSONResponse(content={"results": formatted})


@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body.get("message", "")
    history = body.get("history", [])

    api_key = os.environ.get("GEMINI_API_KEY", "")

    if not api_key:
        # Fallback: search flattened browse data (broader coverage)
        q = user_message.lower()
        keywords = q.split()
        matches = []
        for lamp_info in BROWSE_DATA.values():
            for row in lamp_info["rows"]:
                text = f"{row['uraian']} {row['path']}".lower()
                if all(kw in text for kw in keywords):
                    matches.append(row)
        # Deduplicate and limit
        matches = matches[:15]
        if matches:
            lines = ["Berikut hasil pencarian dari database SBM UI 2024:\n"]
            for row in matches:
                lines.append(f"**{row['uraian']}**\n- Lampiran: {row['lampiran']} ({row['lampiran_nama']})\n- Satuan: {row['satuan']}\n- Besaran Tertinggi: {row['besaran']}\n")
            lines.append("\n---\n*Mode pencarian langsung (tanpa AI). Set GEMINI_API_KEY untuk mode AI.*")
            response_text = "\n".join(lines)
        else:
            response_text = f"Maaf, tidak ditemukan data untuk '{user_message}' dalam SBM UI 2024.\n\nCoba kata kunci lain, misalnya: dosen tamu, wisuda, asuransi, penginapan, perjalanan dinas.\n\n---\n*Mode pencarian langsung (tanpa AI). Set GEMINI_API_KEY untuk mode AI.*"

        return JSONResponse(content={"response": response_text, "streaming": False})

    # With Gemini API: streaming response
    import google.generativeai as genai

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash-lite", system_instruction=SYSTEM_PROMPT)

    gemini_history = []
    for msg in history[-10:]:
        role = "model" if msg["role"] == "assistant" else "user"
        gemini_history.append({"role": role, "parts": [{"text": msg["content"]}]})

    async def generate():
        try:
            chat = model.start_chat(history=gemini_history)
            response = chat.send_message(user_message, stream=True)
            for chunk in response:
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
