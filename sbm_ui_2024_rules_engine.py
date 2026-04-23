"""
STANDAR BIAYA UNIVERSITAS INDONESIA TAHUN 2024
Peraturan Rektor Universitas Indonesia Nomor 16 Tahun 2024
Ditetapkan: 12 Juli 2024 oleh Prof. Ari Kuncoro, S.E., M.A., Ph.D.

Validated against sbm_ordered.json (OCR of all 141 pages).
All rates below are "BESARAN TERTINGGI" (maximum amount) unless noted otherwise.

============================================================================
STRUCTURE
============================================================================
  METADATA        - Document info, citation.
  KATEGORI_PEGAWAI - Employee categories A-E (Pasal 7).
  SATUAN          - Unit abbreviations (Pasal 8).
  LAMPIRAN_I      - Kegiatan Pendidikan              (pages 14-29, 13 sections)
  LAMPIRAN_II     - Kegiatan Kemahasiswaan            (pages 30-52, 27 sections)
  LAMPIRAN_III    - Penelitian/Inovasi/Pengabdian     (pages 53-67,  9 sections)
  LAMPIRAN_IV     - Operasional Manajemen             (pages 68-95, 26 sections)
  LAMPIRAN_V      - Honorarium Kegiatan               (pages 96-112,11 sections)
  LAMPIRAN_VI     - Perjalanan Dinas                  (pages 113-133,10 sections)
  LAMPIRAN_VII    - Penerimaan Mahasiswa Baru         (pages 134-141, 8 sections)
  SBM_UI_2024     - Master tree combining all lampiran.

Each rate node is a dict of:
  {"uraian": "<description>", "satuan": "<unit>", "besaran": <int or string>}
Where `besaran` is an int (IDR) OR a string like "at cost" / "USD 150".

============================================================================
EMPLOYEE CATEGORIES (Pasal 7)
============================================================================
  A: Ketua/Sekretaris MWA/SA/DGB, Rektor, Sekretaris Universitas,
     Wakil Rektor, Kepala Badan, Dekan/Direktur Sekolah/Direktur
     Program Pendidikan Vokasi
  B: Anggota MWA/SA/DGB, Kepala Satuan, Direktur, Kepala Biro,
     Kepala Badan Penjaminan Mutu Akademik, Kepala Kantor, Kepala
     UPT, Kepala UKK, Ketua Departemen, Sekretaris Departemen,
     PNS Gol IVc+, Wakil Dekan/Wakil Direktur, Kepala RS UI
  C: Deputi, Kepala Sub Direktorat, Manajer, Ketua Program Studi,
     Sekretaris Program Studi, Kepala Lab Fakultas/Departemen,
     PNS Gol IIIc-IVb
  D: Asisten Deputi, Kepala Seksi, Koordinator di PAU, Wakil/
     Asisten Manajer, Koordinator di bawah Manajer
  E: Pegawai UI selain kategori A, B, C, D

If jabatan struktural and pangkat/golongan differ in category, use
the HIGHER one.
"""

# =============================================================================
# METADATA
# =============================================================================

METADATA = {
    "dokumen": "Peraturan Rektor Universitas Indonesia Nomor 16 Tahun 2024",
    "tentang": "Standar Biaya Universitas Indonesia Tahun 2024",
    "ditetapkan": "12 Juli 2024",
    "oleh": "Prof. Ari Kuncoro, S.E., M.A., Ph.D.",
    "mencabut": [
        "Peraturan Rektor UI No 14 Tahun 2023 tentang SBM 2023",
        "Peraturan Rektor UI No 19 Tahun 2023 tentang Perubahan atas No 14/2023",
    ],
    "total_halaman": 141,
}


KATEGORI_PEGAWAI = {
    "A": "Ketua/Sekretaris MWA/SA/DGB, Rektor, Sekretaris Universitas, Wakil Rektor, Kepala Badan, Dekan/Direktur Sekolah/Direktur Program Pendidikan Vokasi",
    "B": "Anggota MWA/SA/DGB, Kepala Satuan, Direktur, Kepala Biro, Kepala Badan Penjaminan Mutu Akademik, Kepala Kantor, Kepala UPT, Kepala UKK, Ketua/Sekretaris Departemen, PNS Gol IVc+, Wakil Dekan/Wakil Direktur, Kepala RS UI",
    "C": "Deputi, Kepala Sub Direktorat, Manajer, Ketua/Sekretaris Program Studi, Kepala Lab Fakultas/Departemen, PNS Gol IIIc-IVb",
    "D": "Asisten Deputi, Kepala Seksi, Koordinator di PAU, Wakil/Asisten Manajer, Koordinator di bawah Manajer",
    "E": "Pegawai UI selain kategori A, B, C, D",
}

SATUAN = {
    "B": "Bulan", "H": "Hari", "J": "Jam", "O": "Orang",
    "Mhs": "Mahasiswa", "K": "Kegiatan", "P": "Paket",
    "T": "Tahun", "U": "Unit",
}


# =============================================================================
# LAMPIRAN I — KEGIATAN PENDIDIKAN  (pages 14-29)
# =============================================================================

LAMPIRAN_I = {
    "nama": "Kegiatan Pendidikan",

    "1_honorarium_dosen_tamu": {
        "nama": "Honorarium Dosen Tamu",
        "dosen_tamu": {
            "menteri_pejabat_setingkat_menteri_internasional": {
                "uraian": "Menteri/Pejabat setingkat Menteri/Praktisi/Profesional tingkat Internasional",
                "satuan": "O/J", "besaran": 3_500_000},
            "guru_besar_eselon_i_nasional": {
                "uraian": "Guru Besar/Pejabat eselon I/Praktisi/Profesional tingkat Nasional",
                "satuan": "O/J", "besaran": 2_800_000},
            "doktor_eselon_ii": {
                "uraian": "Doktor/Pejabat eselon II/Praktisi/Profesional yang disetarakan",
                "satuan": "O/J", "besaran": 1_700_000},
            "magister_spesialis_eselon_iii": {
                "uraian": "Magister/Spesialis/Pejabat eselon III/Praktisi/Profesional yang disetarakan",
                "satuan": "O/J", "besaran": 900_000},
        },
        "dosen_tamu_luar_negeri": {"uraian": "Dosen Tamu Luar Negeri", "satuan": "O/J", "besaran": 5_500_000},
        "catatan": [
            "Dosen tamu luar jabodetabek/luar negeri: tiket kelas ekonomi + penginapan maks kategori B, at cost.",
            "Honor praktisi/profesional/pejabat negara disesuaikan dengan standar biaya profesor/doktor/magister berdasarkan tingkat kepakarannya.",
            "Maks 2 kali per orang per Fakultas dalam 1 semester.",
        ],
    },

    "2_honorarium_asisten_dosen": {
        "nama": "Honorarium Asisten Dosen",
        "perkuliahan": {
            "lulusan_s3":                         {"satuan": "O/Hadir", "besaran": 570_000},
            "lulusan_s2":                         {"satuan": "O/Hadir", "besaran": 570_000},
            "lulusan_s1":                         {"satuan": "O/Hadir", "besaran": 210_000},
            "lulusan_s1_rpl":                     {"satuan": "O/Hadir", "besaran": 235_000},
            "lulusan_s1_kelas_internasional":     {"satuan": "O/Hadir", "besaran": 340_000},
            "berstatus_mahasiswa":                {"satuan": "O/Hadir", "besaran": 160_000},
            "mahasiswa_s1_rpl":                   {"satuan": "O/Hadir", "besaran": 205_000},
            "mahasiswa_kelas_internasional":      {"satuan": "O/Hadir", "besaran": 315_000},
        },
        "praktikum_laboratorium": {
            "asisten_s3":                         {"satuan": "O/Hadir", "besaran": 300_000},
            "asisten_s2":                         {"satuan": "O/Hadir", "besaran": 225_000},
            "asisten_s1":                         {"satuan": "O/Hadir", "besaran": 160_000},
            "asisten_s1_rpl":                     {"satuan": "O/Hadir", "besaran": 255_000},
            "asisten_mahasiswa":                  {"satuan": "O/Hadir", "besaran":  75_000},
        },
        "sit_in": {"satuan": "O/Hadir", "besaran": 55_000},
    },

    "3_honorarium_tim_pengelola_modul": {
        "nama": "Honorarium Tim Pengelola Modul (Rumpun Ilmu Kesehatan)",
        "items": {
            "tim_pemicu_pj_modul":                {"uraian": "Tim Pemicu/Penanggung jawab modul",        "satuan": "O/Modul",  "besaran": 900_000},
            "pemeriksa_ujian_esai":               {"uraian": "Pemeriksa Ujian Esai",                      "satuan": "O/Mhs",    "besaran":  12_000},
            "pj_ujian_tulis_sumatif":             {"uraian": "Penanggung jawab Ujian Tulis Sumatif",      "satuan": "O/Modul",  "besaran": 900_000},
            "item_reviewer":                      {"uraian": "Item reviewer",                             "satuan": "O/Ujian",  "besaran": 900_000},
            "pj_praktikum_integrasi":             {"uraian": "Penanggung jawab Praktikum Integrasi",      "satuan": "O/Modul",  "besaran": 900_000},
            "penerjemah":                         {"uraian": "Penerjemah",                                "satuan": "O/Halaman","besaran":  90_000},
            "pj_harian":                          {"uraian": "Penanggung jawab Harian",                   "satuan": "O/H",      "besaran": 120_000},
            "sekretariat_modul":                  {"uraian": "Sekretariat Modul",                         "satuan": "O/Minggu", "besaran": 100_000},
        },
        "catatan": [
            "Hanya untuk Fakultas di Rumpun Ilmu Kesehatan (RIK) dengan sistem modul.",
            "Tim pemicu/penanggung jawab modul maksimal terdiri dari 5 orang.",
        ],
    },

    "4_stase_praktikum_klinik": {
        "nama": "Kegiatan Stase dan Pembimbing Praktikum Klinik",
        "kegiatan_stase": {
            "semua_program_studi": {"satuan": "Mhs/B", "besaran": "at cost"},
        },
        "praktikum_klinik_rik": {
            "pj_praktikum":         {"satuan": "O/Kali", "besaran": 120_000},
            "tutor_praktek_klinik": {"satuan": "O/J",    "besaran": 180_000},
            "laboran_praktikum":    {"satuan": "O/J",    "besaran":  40_000},
            "laboran_ujian":        {"satuan": "O/Sesi", "besaran":  40_000},
            "pasien_simulasi_sehat":{"satuan": "O/Sesi", "besaran": 150_000},
            "pasien_simulasi_sakit":{"satuan": "O/Sesi", "besaran": 300_000},
        },
        "pembimbing_magang_kasus": {
            "diploma_3":     {"uraian": "Pembimbing Magang / Praktek Klinik D3",       "satuan": "O/Mhs", "besaran":  30_000},
            "diploma_4":     {"uraian": "Pembimbing Magang / Praktek Klinik D4",       "satuan": "O/Mhs", "besaran":  40_000},
            "s1":            {"uraian": "Pembimbingan Magang Program S1",              "satuan": "O/Mhs", "besaran":  40_000},
            "profesi":       {"uraian": "Pembimbingan Magang Program Profesi",         "satuan": "O/Mhs", "besaran": 120_000},
            "kasus_profesi": {"uraian": "Pembimbingan Kasus Program Profesi",          "satuan": "O/Mhs", "besaran": 350_000},
        },
    },

    "5_penyiapan_brp_bahan_ajar": {
        "nama": "Kegiatan Penyiapan BRP/Bahan Ajar",
        "items": {
            "penyusunan_brp_rps":                {"uraian": "Penyusunan BRP/RPS",                                  "satuan": "Dokumen", "besaran":  3_000_000},
            "penyusunan_modul_ajar":             {"uraian": "Penyusunan Modul ajar/bahan praktikum",               "satuan": "Modul",   "besaran":  2_700_000},
            "modul_ajar_elearning":              {"uraian": "Penyusunan modul ajar dengan e-learning",             "satuan": "Modul",   "besaran":  3_700_000},
            "modul_ajar_rik":                    {"uraian": "Penyusunan modul ajar pada RIK",                      "satuan": "Modul",   "besaran":  5_000_000},
            "revisi_brp":                        {"uraian": "Revisi BRP/RPS/Modul ajar/bahan praktikum",           "satuan": "Dokumen", "besaran":  1_000_000},
            "revisi_modul_elearning_rik":        {"uraian": "Revisi modul ajar dengan e-learning/pada RIK",        "satuan": "Modul",   "besaran":  1_500_000},
            "studi_kasus_pengajaran":            {"uraian": "Pembuatan Studi Kasus Pengajaran",                    "satuan": "Kasus",   "besaran": 34_000_000},
            "konten_multimedia_baru":            {"uraian": "Pembuatan Konten Multimedia Baru",                    "satuan": "Modul",   "besaran": 45_000_000},
            "pengembangan_revisi_multimedia":    {"uraian": "Pengembangan/revisi Modul Multimedia",                "satuan": "Modul",   "besaran": 24_000_000},
            "honor_pembimbing_brp":              {"uraian": "Honorarium Pembimbing BRP/Buku Ajar/Kurikulum Prodi", "satuan": "Dokumen", "besaran":    300_000},
            "honor_penelaahan_kurikulum":        {"uraian": "Honorarium Penelaahan Kurikulum Prodi",               "satuan": "Dokumen", "besaran":    500_000},
            "honor_penelaah_proposal_prodi_baru":{"uraian": "Honorarium Penelaah Proposal Pembukaan Prodi Baru/Peminatan Khusus/Kelas Khusus", "satuan": "Proposal", "besaran": 500_000},
        },
    },

    "6_ujian_evaluasi": {
        "nama": "Kegiatan Ujian/Evaluasi Hasil Pembelajaran",
        "honorarium_penguji": {
            "penguji_osce_rik":                  {"uraian": "Penguji OSCE pada Fakultas dalam RIK",                                "satuan": "O/Sesi",       "besaran": 730_000},
            "penguji_kasuistik_psikologi":       {"uraian": "Penguji Kasuistik program Profesi (Fak Psikologi)",                   "satuan": "O/K",          "besaran": 350_000},
            "penguji_pemahaman_kasus_psikologi": {"uraian": "Penguji Pemahaman Kasus Internal program Profesi (Psikologi)",        "satuan": "O/K",          "besaran": 350_000},
            "penguji_kasus_eksternal_himpsi":    {"uraian": "Penguji Kasus Eksternal dari HIMPSI (Psikologi)",                     "satuan": "O/K",          "besaran": "at cost"},
            "pendamping_penguji_kasus_eksternal":{"uraian": "Pendamping Penguji Kasus Eksternal Program Profesi Psikologi",        "satuan": "O/K",          "besaran": 350_000},
            "honor_pembuat_soal_ppdgs":          {"uraian": "Honor Pembuat Soal Mahasiswa PPDGS",                                  "satuan": "O/K",          "besaran": 200_000},
            "honor_narasumber_pembekalan_ukmp2dg":{"uraian": "Honor Narasumber Pembekalan dan Pembuat Soal ujian UKMP2DG",         "satuan": "O/Pertemuan",  "besaran": 400_000},
            "honor_pembuat_soal_ukmp2dg":        {"uraian": "Honor Pembuat Soal pada ujian UKMP2DG",                               "satuan": "O/K",          "besaran": 400_000},
        },
        "honorarium_lain": {
            "kolokium_s3_narasumber":            {"uraian": "Kolokium Mahasiswa S3 - Honorarium Narasumber", "satuan": "O/J",       "besaran": 300_000},
            "kolokium_s3_reviewer":              {"uraian": "Kolokium Mahasiswa S3 - Honorarium Reviewer",   "satuan": "O/Artikel", "besaran": 200_000},
            "jasa_konseling_psikolog":           {"uraian": "Jasa Konseling Psikolog",                       "satuan": "O/K",       "besaran": 500_000},
        },
        "honorarium_pengawas_ujian": {
            "asisten_dosen_pengawas":            {"uraian": "Asisten Dosen sebagai pengawas kelas",         "satuan": "O/Mata Uji",  "besaran": 125_000},
            "tendik_mahasiswa_pengawas":         {"uraian": "Tenaga Kependidikan/Mahasiswa sebagai pengawas","satuan": "O/Mata Uji",  "besaran": 100_000},
            "pengawas_ujian_lab":                {"uraian": "Pengawas Ujian Lab",                           "satuan": "O/Mata Uji",  "besaran": 240_000},
            "pengawas_ujian_osce":               {"uraian": "Pengawas Ujian OSCE",                          "satuan": "O/Sesi",      "besaran": 350_000},
            "insentif_pengawas_kecurangan":      {"uraian": "Insentif pengawas yang menemukan kecurangan",   "satuan": "O/Kejadian",  "besaran": 350_000},
            "honor_pengawas_keterampilan_ppdgs": {"uraian": "Honor Pengawas Ujian Keterampilan PPDGS",      "satuan": "Mahasiswa/K", "besaran": 125_000},
        },
        "koordinator_pelaksanaan_ujian": {
            "kelas_gt_350":   {"uraian": "Kelas Pengajaran >350 mahasiswa",    "satuan": "O/K", "besaran": 1_800_000},
            "kelas_151_350":  {"uraian": "Kelas Pengajaran 151-350 mahasiswa", "satuan": "O/K", "besaran": 1_250_000},
            "kelas_51_150":   {"uraian": "Kelas Pengajaran 51-150 mahasiswa",  "satuan": "O/K", "besaran":   950_000},
            "kelas_lte_50":   {"uraian": "Kelas Pengajaran s.d. 50 mahasiswa", "satuan": "O/K", "besaran":   750_000},
        },
    },

    "7_pembimbingan_tugas_akhir": {
        "nama": "Kegiatan Pembimbingan Tugas Akhir Mahasiswa",
        "items": {
            "vokasi":                                   {"uraian": "Program Vokasi",                                     "satuan": "Mhs Lulus", "besaran":    550_000},
            "s1_pembimbing_utama":                      {"uraian": "Program S1 - Pembimbing Utama",                      "satuan": "Mhs Lulus", "besaran":    900_000},
            "s1_pembimbing_kedua":                      {"uraian": "Program S1 - Pembimbing Kedua",                      "satuan": "Mhs Lulus", "besaran":    600_000},
            "s1_dosen_luar_negeri":                     {"uraian": "Program S1 - Dosen luar negeri",                     "satuan": "Mhs Lulus", "besaran": "USD 150"},
            "s1_internasional_pembimbing_utama":        {"uraian": "Program S1 Kelas Internasional - Pembimbing Utama",  "satuan": "Mhs Lulus", "besaran":  1_500_000},
            "s1_internasional_pembimbing_kedua":        {"uraian": "Program S1 Kelas Internasional - Pembimbing Kedua",  "satuan": "Mhs Lulus", "besaran":  1_200_000},
            "magister_spesialis_profesi_pembimbing_i":  {"uraian": "Magister/Spesialis/Profesi (S2) - Pembimbing I",     "satuan": "Mhs Lulus", "besaran":  3_000_000},
            "magister_spesialis_profesi_pembimbing_ii": {"uraian": "Magister/Spesialis/Profesi (S2) - Pembimbing II",    "satuan": "Mhs Lulus", "besaran":  1_500_000},
            "magister_spesialis_dosen_luar_negeri":     {"uraian": "Magister/Spesialis - Dosen luar negeri",             "satuan": "Mhs Lulus", "besaran": "USD 200"},
            "spesialis_pembimbing_i":                   {"uraian": "Program Spesialis - Pembimbing I",                   "satuan": "Mhs Lulus", "besaran":    700_000},
            "spesialis_pembimbing_ii":                  {"uraian": "Program Spesialis - Pembimbing II",                  "satuan": "Mhs Lulus", "besaran":    500_000},
            "doktor_promotor":                          {"uraian": "Program Doktor - Pembimbing Utama/Promotor",         "satuan": "Mhs Lulus", "besaran":  7_250_000},
            "doktor_co_promotor":                       {"uraian": "Program Doktor - Pembimbing Pendamping/Co-Promotor", "satuan": "Mhs Lulus", "besaran":  6_000_000},
            "doktor_dosen_luar_negeri":                 {"uraian": "Program Doktor - Dosen luar negeri",                 "satuan": "Mhs Lulus", "besaran": "USD 300"},
        },
        "catatan": [
            "Pembayaran dilakukan setelah mahasiswa dinyatakan lulus.",
            "Dibayarkan bersamaan dengan pembayaran remunerasi rutin Dosen.",
        ],
    },

    "8_ujian_tugas_akhir": {
        "nama": "Kegiatan Ujian Tugas Akhir Mahasiswa",
        "vokasi": {
            "ketua_penguji":   {"satuan": "O/K", "besaran": 240_000},
            "anggota_penguji": {"satuan": "O/K", "besaran": 180_000},
        },
        "sarjana_s1": {
            "ketua_penguji":    {"satuan": "O/K", "besaran": 350_000},
            "anggota_penguji":  {"satuan": "O/K", "besaran": 300_000},
            "dosen_luar_negeri":{"satuan": "O/K", "besaran": "USD 100"},
        },
        "s1_internasional": {
            "ketua_penguji":    {"satuan": "O/K", "besaran": 600_000},
            "anggota_penguji":  {"satuan": "O/K", "besaran": 500_000},
            "dosen_luar_negeri":{"satuan": "O/K", "besaran": "USD 100"},
        },
        "magister_spesialis_profesi_s2": {
            "ketua_penguji":         {"satuan": "O/K", "besaran": 700_000},
            "anggota_penguji":       {"satuan": "O/K", "besaran": 600_000},
            "dosen_luar_negeri_tele":{"satuan": "O/K", "besaran": "USD 150"},
        },
        "doktor_spesialis2": {
            "ujian_proposal_riset": {
                "ketua_penguji":   {"satuan": "O/K", "besaran": 700_000},
                "anggota_penguji": {"satuan": "O/K", "besaran": 600_000},
            },
            "ujian_hasil_riset": {
                "ketua_penguji":         {"satuan": "O/K", "besaran":  950_000},
                "anggota_penguji":       {"satuan": "O/K", "besaran":  700_000},
                "dosen_luar_negeri_tele":{"satuan": "O/K", "besaran": "USD 250"},
            },
            "sidang_pra_promosi": {
                "ketua_penguji":         {"satuan": "O/K", "besaran":  950_000},
                "anggota_penguji":       {"satuan": "O/K", "besaran":  900_000},
                "sekretaris_sidang":     {"satuan": "O/K", "besaran":  450_000},
                "dosen_luar_negeri_tele":{"satuan": "O/K", "besaran": "USD 250"},
            },
            "sidang_promosi": {
                "ketua_penguji":         {"satuan": "O/K", "besaran": 1_200_000},
                "anggota_penguji":       {"satuan": "O/K", "besaran":   950_000},
                "sekretaris_sidang":     {"satuan": "O/K", "besaran":   500_000},
                "dosen_luar_negeri_tele":{"satuan": "O/K", "besaran": "USD 250"},
            },
            "ujian_seminar_topik_berkala": {
                "ketua_penguji":   {"satuan": "O/K", "besaran": 700_000},
                "anggota_penguji": {"satuan": "O/K", "besaran": 600_000},
            },
        },
        "penguji_s3_luar_negeri": {
            "datang_ke_indonesia": {"satuan": "O/Mhs", "besaran": 8_400_000},
            "tele_conference":     {"satuan": "O/Mhs", "besaran": "USD 300"},
        },
        "penguji_dalam_negeri_luar_ui": {
            "s1": {"satuan": "O/Mhs", "besaran":   600_000},
            "s2": {"satuan": "O/Mhs", "besaran": 1_200_000},
            "s3": {"satuan": "O/Mhs", "besaran": 2_300_000},
        },
        "penguji_lintas_fakultas_s3": {"satuan": "O/Mhs", "besaran": 1_200_000},
        "reviewer_shp_jurnal_mahasiswa": {
            "jurnal_s2": {"satuan": "Artikel/mhs", "besaran":   250_000},
            "jurnal_s3": {"satuan": "Artikel/mhs", "besaran": 1_100_000},
        },
    },

    "9_institutional_fee_s1": {
        "nama": "Institutional Fee Lahan Pendidikan Modul S1",
        "uraian": "Lahan Pendidikan Modul S1 RSUD/Puskesmas/Klinik/Sejenis",
        "satuan": "Mhs/K", "besaran": "at cost",
    },

    "10_institutional_fee_penelitian": {
        "nama": "Institutional Fee Puskesmas/Rumah Sakit terkait Kegiatan Penelitian",
        "satuan": "Mhs/K", "besaran": "at cost",
        "catatan": ["Periode kegiatan minimal 2 minggu."],
    },

    "11_wisuda_pra_wisuda": {
        "nama": "Kegiatan Wisuda dan Pra Wisuda",
        "items": {
            "toga":                            {"satuan": "set",    "besaran": 300_000},
            "foto_wisuda":                     {"satuan": "lembar", "besaran":  23_000},
            "konsumsi_wisudawan":              {"satuan": "O/Sesi", "besaran":  50_000},
            "transpor_guru_besar_langsung":    {"uraian": "Pengganti Transpor/Kehadiran Guru Besar langsung", "satuan": "O/Sesi", "besaran": 300_000},
            "transpor_guru_besar_daring":      {"uraian": "Pengganti Transpor/Kehadiran Guru Besar daring",   "satuan": "O/Sesi", "besaran": 250_000},
            "transpor_wartawan":               {"uraian": "Pengganti Transpor/Kehadiran Wartawan",            "satuan": "O/Sesi", "besaran": 200_000},
        },
    },

    "12_pengembangan_pembelajaran": {
        "nama": "Kegiatan Pengembangan Pembelajaran",
        "reviewer": {
            "administratif_proposal":   {"satuan": "O/Dokumen", "besaran":   200_000},
            "substansi_proposal":       {"satuan": "O/Dokumen", "besaran":   500_000},
            "dokumen_kurikulum":        {"satuan": "O/Dokumen", "besaran": 1_000_000},
            "dokumen_brp":              {"satuan": "O/Dokumen", "besaran":   500_000},
            "dokumen_buku_ajar":        {"satuan": "O/Dokumen", "besaran":   300_000},
            "modul_video":              {"satuan": "O/Judul",   "besaran":   400_000},
            "modul_audio":              {"satuan": "O/Judul",   "besaran":   300_000},
            "modul_teks":               {"satuan": "O/Judul",   "besaran":   400_000},
            "naskah_modul_pelatihan":   {"satuan": "O/Judul",   "besaran":   400_000},
            "kelas_daring":             {"satuan": "O/Kelas",   "besaran": 1_000_000},
            "laporan_kemajuan_akhir":   {"satuan": "O/Dokumen", "besaran":   500_000},
        },
        "pengembangan_konten_daring": {
            "skema_kredit":             {"satuan": "O/Judul", "besaran": 40_000_000},
            "skema_non_kredit":         {"satuan": "O/Judul", "besaran": 25_000_000},
            "pengembangan_kelas_lms":   {"satuan": "O/Judul", "besaran":  1_000_000},
        },
        "produksi_video_audio": {
            "naskah_video_audio":       {"uraian": "Pembuatan naskah video/audio pembelajaran",  "satuan": "O/Mata Kuliah", "besaran": 1_000_000},
            "naskah_video_pelatihan":   {"uraian": "Pembuatan naskah video pelatihan",           "satuan": "O/Judul",       "besaran": 1_000_000},
            "penyuntingan_naskah":      {"uraian": "Penyuntingan naskah video/audio",            "satuan": "O/Mata Kuliah", "besaran":   500_000},
            "operator_peralatan":       {"satuan": "O/Judul", "besaran":   500_000},
            "produser_pengarah":        {"uraian": "Produser dan pengarah lapangan",             "satuan": "O/Judul",       "besaran": 1_000_000},
            "penyuntingan_video_audio": {"satuan": "O/Judul", "besaran":   500_000},
            "pengisi_suara":            {"uraian": "Pengisi suara/voice over",                   "satuan": "O/Judul",       "besaran":   500_000},
            "juru_kamera_drone":        {"satuan": "O/Judul", "besaran": 2_000_000},
            "talent_produksi":          {"satuan": "O/Judul", "besaran":   500_000},
        },
    },

    "13_penghargaan_konten_pembelajaran": {
        "nama": "Penghargaan Konten Pengembangan Pembelajaran",
        "pembelajaran_daring": {
            "juara_1": {"satuan": "Orang/Judul", "besaran": 10_000_000},
            "juara_2": {"satuan": "Orang/Judul", "besaran":  7_500_000},
            "juara_3": {"satuan": "Orang/Judul", "besaran":  5_000_000},
        },
        "konten_terbuka": {
            "juara_1": {"satuan": "Orang/Judul", "besaran": 5_000_000},
            "juara_2": {"satuan": "Orang/Judul", "besaran": 3_000_000},
            "juara_3": {"satuan": "Orang/Judul", "besaran": 1_500_000},
        },
    },
}


# =============================================================================
# LAMPIRAN II — KEGIATAN KEMAHASISWAAN  (pages 30-52)
# =============================================================================

LAMPIRAN_II = {
    "nama": "Kegiatan Kemahasiswaan",

    "1_bantuan_organisasi_kemahasiswaan": {
        "nama": "Bantuan Organisasi Kemahasiswaan",
        "items": {
            "bantuan_rutin_bem_dpm":    {"uraian": "Bantuan Rutin BEM/DPM",                                "satuan": "B",   "besaran":     500_000},
            "bantuan_rutin_ukm":        {"uraian": "Bantuan Rutin Operasional Unit Kegiatan Mahasiswa",    "satuan": "U/B", "besaran":     500_000},
            "bantuan_pelatih_ukm":      {"uraian": "Bantuan Pelatih UKM",                                  "satuan": "O/B", "besaran":     750_000},
            "bantuan_kegiatan_unggulan":{"uraian": "Bantuan Kegiatan Unggulan Fakultas/Sekolah/Vokasi",    "satuan": "T",   "besaran": 100_000_000},
        },
    },

    "2_bantuan_pelaksanaan_kegiatan": {
        "nama": "Bantuan Pelaksanaan/Penyelenggaraan Kegiatan Kemahasiswaan (Inisiatif Mahasiswa/Non Dikti)",
        "items": {
            "tingkat_fakultas":       {"satuan": "K", "besaran":  10_000_000},
            "tingkat_universitas":    {"satuan": "K", "besaran":  20_000_000},
            "tingkat_nasional":       {"satuan": "K", "besaran":  50_000_000},
            "tingkat_internasional":  {"satuan": "K", "besaran": 100_000_000},
        },
    },

    "3_penghargaan_mahasiswa_berprestasi": {
        "nama": "Penghargaan Mahasiswa Berprestasi",
        "tingkat_fakultas": {
            "berprestasi_i":    {"satuan": "K", "besaran": 10_000_000},
            "berprestasi_ii":   {"satuan": "K", "besaran":  7_500_000},
            "berprestasi_iii":  {"satuan": "K", "besaran":  5_000_000},
            "penghargaan_lain": {"satuan": "K", "besaran":  2_000_000},
        },
        "tingkat_universitas": {
            "berprestasi_i":    {"satuan": "K", "besaran": 15_000_000},
            "berprestasi_ii":   {"satuan": "K", "besaran": 10_000_000},
            "berprestasi_iii":  {"satuan": "K", "besaran":  7_500_000},
            "finalis":          {"satuan": "K", "besaran":  5_000_000},
            "penghargaan_lain": {"satuan": "K", "besaran":  3_000_000},
        },
    },

    "4_penghargaan_mahasiswa_kompetisi": {
        "nama": "Penghargaan Mahasiswa dalam Kompetisi",
        "perorangan": {
            "nasional": {
                "juara_i":          {"satuan": "K", "besaran": 8_000_000},
                "juara_ii":         {"satuan": "K", "besaran": 7_000_000},
                "juara_iii":        {"satuan": "K", "besaran": 6_000_000},
                "penghargaan_lain": {"satuan": "K", "besaran": 5_000_000},
            },
            "internasional": {
                "juara_i":          {"satuan": "K", "besaran": 10_000_000},
                "juara_ii":         {"satuan": "K", "besaran":  9_000_000},
                "juara_iii":        {"satuan": "K", "besaran":  8_000_000},
                "penghargaan_lain": {"satuan": "K", "besaran":  6_000_000},
            },
        },
        "kelompok": {
            "nasional": {
                "juara_i":          {"satuan": "K", "besaran": 12_000_000},
                "juara_ii":         {"satuan": "K", "besaran": 11_000_000},
                "juara_iii":        {"satuan": "K", "besaran": 10_000_000},
                "penghargaan_lain": {"satuan": "K", "besaran":  8_000_000},
            },
            "internasional": {
                "juara_i":          {"satuan": "K", "besaran": 15_000_000},
                "juara_ii":         {"satuan": "K", "besaran": 14_000_000},
                "juara_iii":        {"satuan": "K", "besaran": 13_000_000},
                "penghargaan_lain": {"satuan": "K", "besaran": 11_000_000},
            },
        },
    },

    "5_penilai_juri_kompetisi": {
        "nama": "Penilai/Juri Kompetisi Mahasiswa dan Mahasiswa Berprestasi",
        "nasional":      {"satuan": "O/K", "besaran": 3_000_000},
        "internasional": {"satuan": "O/K", "besaran": 5_000_000},
    },

    "6_bantuan_mahasiswa_kompetisi": {
        "nama": "Bantuan Mahasiswa dalam Mengikuti Kompetisi",
        "nasional": {"satuan": "O/Cabang/K", "besaran": 5_000_000},
        "internasional": {
            "wilayah_amerika":                  {"satuan": "O/Cabang/K", "besaran": 20_000_000},
            "wilayah_eropa_afrika":             {"satuan": "O/Cabang/K", "besaran": 15_000_000},
            "wilayah_asia_non_asean_australia": {"satuan": "O/Cabang/K", "besaran": 12_000_000},
            "wilayah_asean":                    {"satuan": "O/Cabang/K", "besaran":  6_000_000},
        },
        "catatan": ["Maksimal 50 mahasiswa per cabang lomba."],
    },

    "7_honor_pembimbing_kompetisi_mbkm": {
        "nama": "Honorarium dan Insentif Pembimbing Mahasiswa pada Kompetisi dan MBKM",
        "tingkat_nasional": {
            "dosen_perorangan": {
                "juara_i":          {"satuan": "O/K", "besaran": 5_000_000},
                "juara_ii":         {"satuan": "O/K", "besaran": 4_000_000},
                "juara_iii":        {"satuan": "O/K", "besaran": 3_000_000},
                "penghargaan_lain": {"satuan": "O/K", "besaran": 2_000_000},
            },
            "dosen_kelompok": {
                "juara_i":          {"satuan": "O/K", "besaran": 8_000_000},
                "juara_ii":         {"satuan": "O/K", "besaran": 7_000_000},
                "juara_iii":        {"satuan": "O/K", "besaran": 6_000_000},
                "penghargaan_lain": {"satuan": "O/K", "besaran": 4_000_000},
            },
        },
        "tingkat_internasional": {
            "dosen_perorangan": {
                "juara_i":          {"satuan": "O/K", "besaran": 8_000_000},
                "juara_ii":         {"satuan": "O/K", "besaran": 7_000_000},
                "juara_iii":        {"satuan": "O/K", "besaran": 6_000_000},
                "penghargaan_lain": {"satuan": "O/K", "besaran": 4_000_000},
            },
            "dosen_kelompok": {
                "juara_i":          {"satuan": "O/K", "besaran": 15_000_000},
                "juara_ii":         {"satuan": "O/K", "besaran": 12_000_000},
                "juara_iii":        {"satuan": "O/K", "besaran": 10_000_000},
                "penghargaan_lain": {"satuan": "O/K", "besaran":  8_000_000},
            },
        },
        "pembimbing_pra_seleksi":       {"satuan": "O/Sesi", "besaran": 350_000},
        "pembimbing_booth_camp":        {"satuan": "O/Sesi", "besaran": 350_000},
        "pembimbing_persiapan_lomba":   {"satuan": "O/Sesi", "besaran": 350_000},
    },

    "8_honor_pkm": {
        "nama": "Honorarium dan Insentif Program Kreativitas Mahasiswa (PKM)",
        "items": {
            "reviewer_judul":                  {"uraian": "Reviewer Judul Proposal/Artikel Ilmiah",                "satuan": "O/Judul",      "besaran":   100_000},
            "reviewer_konten":                 {"uraian": "Reviewer Konten Proposal/Konten Artikel Ilmiah",       "satuan": "O/Proposal atau Artikel", "besaran": 250_000},
            "desain_poster_dosen":             {"uraian": "Desain Poster - Dosen UI/Tenaga Ahli",                 "satuan": "O/Poster",     "besaran":   750_000},
            "desain_poster_mahasiswa":         {"uraian": "Desain Poster - Mahasiswa",                            "satuan": "O/Poster",     "besaran":   175_000},
            "monev_drilling_reviewer_internal":{"uraian": "Monev dan Drilling Reviewer Internal",                 "satuan": "O/Tim Presentasi", "besaran": 450_000},
            "volunteer_pkm":                   {"uraian": "Volunteer PKM",                                        "satuan": "O/K",          "besaran":   500_000},
            "bantuan_pkm_8_bidang":            {"uraian": "Bantuan PKM 8 Bidang (didanai Kemendikbudristek)",     "satuan": "Kelompok",     "besaran": 1_500_000},
            "bantuan_pkm_gagasan_futuristik":  {"uraian": "Bantuan PKM Gagasan Futuristik Tertulis/Artikel Ilmiah", "satuan": "Kelompok",   "besaran": 1_500_000},
            "bantuan_pkm_lolos_pimnas":        {"uraian": "Bantuan PKM Lolos PIMNAS",                             "satuan": "Kelompok",     "besaran": 2_500_000},
            "insentif_pembimbing_8_bidang":    {"uraian": "Insentif Pembimbing PKM 8 Bidang didanai",             "satuan": "O/B",          "besaran":   600_000},
            "insentif_pembimbing_gagasan":     {"uraian": "Insentif Pembimbing PKM Gagasan Futuristik",           "satuan": "O/B",          "besaran":   600_000},
            "insentif_pembimbing_pimnas":      {"uraian": "Insentif Pembimbing PKM lolos PIMNAS",                 "satuan": "O/PKM Lolos",  "besaran": 1_500_000},
        },
        "catatan": ["Insentif pembimbing PKM maks 9 bulan dalam 1 tahun."],
    },

    "9_wasit_juri_pertandingan": {
        "nama": "Honorarium Wasit/Juri Pertandingan Olahraga",
        "nasional": {
            "koordinator_wasit":      {"satuan": "O/pertandingan", "besaran": 500_000},
            "wasit":                  {"satuan": "O/pertandingan", "besaran": 400_000},
            "asisten_wasit_hakim_garis":{"satuan": "O/pertandingan", "besaran": 300_000},
            "juri":                   {"satuan": "O/pertandingan", "besaran": 500_000},
            "starter":                {"satuan": "O/pertandingan", "besaran": 200_000},
            "timer":                  {"satuan": "O/pertandingan", "besaran": 200_000},
            "ball_boy":               {"satuan": "O/pertandingan", "besaran": 100_000},
        },
        "internasional": {
            "koordinator_wasit":      {"satuan": "O/pertandingan", "besaran": 600_000},
            "wasit":                  {"satuan": "O/pertandingan", "besaran": 500_000},
            "asisten_wasit_hakim_garis":{"satuan": "O/pertandingan", "besaran": 400_000},
            "juri":                   {"satuan": "O/pertandingan", "besaran": 600_000},
            "starter":                {"satuan": "O/pertandingan", "besaran": 200_000},
            "timer":                  {"satuan": "O/pertandingan", "besaran": 200_000},
            "ball_boy":               {"satuan": "O/pertandingan", "besaran": 100_000},
        },
    },

    "10_bantuan_persiapan_kompetisi": {
        "nama": "Bantuan Khusus Persiapan Kompetisi Prestasi",
        "besaran": 10_000_000, "satuan": "Cabang",
    },

    "11_honor_reviewer_kompetisi_non_pkm": {
        "nama": "Honorarium Reviewer Kegiatan Kompetisi Kemahasiswaan Selain PKM",
        "items": {
            "reviewer_judul":    {"uraian": "Reviewer Judul Proposal",                       "satuan": "O/Judul",     "besaran": 100_000},
            "reviewer_konten":   {"uraian": "Reviewer Konten Teknis Proposal",               "satuan": "O/Proposal",  "besaran": 350_000},
            "monev_sidang_akhir":{"uraian": "Monitoring dan Evaluasi/Sidang laporan akhir",  "satuan": "O/Presentasi","besaran": 450_000},
        },
    },

    "12_bantuan_presentasi_karya_ilmiah": {
        "nama": "Bantuan Presentasi Karya Ilmiah Mahasiswa",
        "nasional": {"satuan": "O/K", "besaran": 3_000_000},
        "internasional": {
            "wilayah_amerika":                  {"satuan": "O/K", "besaran": 16_000_000},
            "wilayah_eropa_afrika":             {"satuan": "O/K", "besaran": 12_000_000},
            "wilayah_asia_non_asean_australia": {"satuan": "O/K", "besaran":  9_600_000},
            "wilayah_asean":                    {"satuan": "O/K", "besaran":  4_800_000},
        },
    },

    "13_penghargaan_publikasi_jurnal": {
        "nama": "Penghargaan Publikasi Karya Ilmiah Mahasiswa S1/Vokasi di Jurnal Ilmiah",
        "items": {
            "internasional_impact_factor":     {"uraian": "Jurnal Internasional terindeks dgn impact factor",   "satuan": "O/K", "besaran": 10_000_000},
            "internasional_tanpa_if":          {"uraian": "Jurnal Internasional terindeks tanpa impact factor", "satuan": "O/K", "besaran":  7_000_000},
            "nasional_terakreditasi_a":        {"uraian": "Jurnal Nasional Terakreditasi A",                    "satuan": "O/K", "besaran":  5_000_000},
            "nasional_terakreditasi_b":        {"uraian": "Jurnal Nasional Terakreditasi B",                    "satuan": "O/K", "besaran":  3_000_000},
        },
        "catatan": ["Diberikan maksimal 1 tahun setelah mahasiswa lulus."],
    },

    "14_pengabdian_masyarakat": {
        "nama": "Bantuan Mahasiswa/Pendamping/Pembimbing dalam Pengabdian kepada Masyarakat",
        "uang_harian_mahasiswa": {
            "bali_papua":       {"satuan": "O/H", "besaran": 100_000},
            "selain_bali_papua":{"satuan": "O/H", "besaran":  80_000},
        },
        "uang_harian_pendamping_lapangan": {
            "bali_papua":       {"satuan": "O/H", "besaran": 200_000},
            "selain_bali_papua":{"satuan": "O/H", "besaran": 150_000},
        },
        "uang_harian_dosen_pembimbing": {
            "bali_papua":       {"satuan": "O/H", "besaran": 400_000},
            "selain_bali_papua":{"satuan": "O/H", "besaran": 300_000},
        },
        "bantuan_rumah_tinggal": {"satuan": "Rumah/B", "besaran": 3_000_000},
        "bantuan_kegiatan_pkm_by_jumlah_mhs": {
            "mhs_5_10":    {"satuan": "K", "besaran":  25_000_000},
            "mhs_11_50":   {"satuan": "K", "besaran":  50_000_000},
            "mhs_51_100":  {"satuan": "K", "besaran":  75_000_000},
            "mhs_gt_100":  {"satuan": "K", "besaran": 100_000_000},
        },
        "honor_dosen_pembimbing_lapangan": {"satuan": "O/B", "besaran": 600_000},
    },

    "15_pengisi_acara_seni_mahasiswa": {
        "nama": "Pengisi Acara Seni Mahasiswa",
        "pengisi_acara": {
            "penyanyi_solois":          {"satuan": "O/K", "besaran":   500_000},
            "penari_pemusik":           {"satuan": "O/K", "besaran":   600_000},
            "pianis":                   {"satuan": "O/K", "besaran": 1_000_000},
            "penampilan_mhs_lainnya":   {"satuan": "O/K", "besaran":   500_000},
            "penampilan_band":          {"satuan": "O/K", "besaran": 1_000_000},
        },
        "pelatih_arranger_koreografer": {"satuan": "O/H", "besaran": 800_000},
    },

    "16_beasiswa_paruh_waktu": {
        "nama": "Beasiswa Paruh Waktu Mahasiswa",
        "besaran": 12_500, "satuan": "O/J",
        "catatan": ["Maks 60 jam per bulan."],
    },

    "17_bantuan_inbound_outbound": {
        "nama": "Bantuan Inbound/Outbound Mahasiswa",
        "items": {
            "bantuan_inbound":                    {"satuan": "O/K", "besaran": 36_000_000},
            "visa_dirjen_imigrasi":               {"uraian": "Persetujuan Visa Direktur Jenderal Imigrasi",             "satuan": "O/K", "besaran": "at cost"},
            "visa_tinggal_terbatas":              {"satuan": "O/K", "besaran": "at cost"},
            "visa_kunjungan_sekali":              {"uraian": "Visa Kunjungan Sekali Perjalanan Paling Lama 60 Hari",    "satuan": "O/K", "besaran": "at cost"},
            "bantuan_outbound":                   {"uraian": "Bantuan Outbound Mahasiswa ke Luar Negeri",               "satuan": "O/K", "besaran": 50_000_000},
            "mbkm_dalam_negeri_jabodetabek":      {"uraian": "MBKM Dalam Negeri (Jabodetabek)",                         "satuan": "O/K", "besaran":  2_400_000},
            "mbkm_dalam_negeri_luar_jabodetabek": {"uraian": "MBKM Dalam Negeri (Luar Jabodetabek)",                    "satuan": "O/K", "besaran":  4_800_000},
            "program_inspire":                    {"uraian": "Bantuan Program INSPIRE",                                 "satuan": "O/K", "besaran": 50_000_000},
        },
    },

    "18_bantuan_alih_penjamin_asing": {
        "nama": "Bantuan Alih Penjamin Mahasiswa Asing",
        "besaran": 6_500_000, "satuan": "O/K",
    },

    "19_beasiswa_mahasiswa_asing_s2_s3": {
        "nama": "Bantuan Beasiswa Mahasiswa Asing (S2 dan S3)",
        "items": {
            "visa_dirjen_imigrasi":   {"satuan": "O/K", "besaran": "at cost"},
            "visa_tinggal_terbatas":  {"satuan": "O/K", "besaran": "at cost"},
            "bantuan_izin_tinggal":   {"satuan": "O/T", "besaran": "at cost"},
            "tiket_kedatangan":       {"satuan": "O/K", "besaran": 10_000_000},
            "tiket_kepulangan":       {"satuan": "O/K", "besaran": 10_000_000},
            "settlement_allowance":   {"satuan": "O/K", "besaran":  1_500_000},
            "asuransi":               {"satuan": "O/B", "besaran":    500_000},
            "biaya_hidup":            {"satuan": "O/B", "besaran":  4_000_000},
            "buku_penelitian":        {"satuan": "O/B", "besaran":    500_000},
            "karantina_kedatangan":   {"satuan": "O/K", "besaran":  5_000_000},
        },
        "catatan": ["Masa studi maksimal 4 semester."],
    },

    "20_pengganti_transportasi_uang_saku": {
        "nama": "Pengganti Transportasi Mahasiswa dan Uang Saku Mahasiswa dalam Kegiatan Kemahasiswaan",
        "items": {
            "transportasi_dalam_luar_kampus": {"uraian": "Transportasi Mahasiswa Dalam/Luar Lingkungan Kampus UI", "satuan": "O/H", "besaran": 125_000},
            "uang_saku_jemput_asing":         {"uraian": "Uang Saku Mahasiswa atas Penjemputan Mahasiswa Asing",   "satuan": "O/H", "besaran": 200_000},
        },
    },

    "21_paket_pelatihan_mahasiswa": {
        "nama": "Paket Pelatihan/Workshop/Pembimbingan Kegiatan Mahasiswa/Pengenalan Budaya Mahasiswa Asing",
        "paket_rapat": {
            "dki_jakarta":      {"satuan": "O/P", "halfday": 354_000, "fullday": 433_000, "fullboard": 1_197_000},
            "selain_dki_jakarta":{"satuan": "O/P","halfday": 414_000, "fullday": 498_000, "fullboard":   822_000},
        },
        "uang_harian": {
            "dki_jakarta":      {"satuan": "O/H", "halfday": 110_000, "fullday": 130_000, "fullboard": 180_000},
            "selain_dki_jakarta":{"satuan": "O/H","halfday": 130_000, "fullday": 150_000, "fullboard": 160_000},
        },
    },

    "22_penginapan_mahasiswa": {
        "nama": "Penginapan Dalam Negeri Mahasiswa",
        "dki_jakarta":        {"satuan": "O/H", "besaran": 730_000},
        "selain_dki_jakarta": {"satuan": "O/H", "besaran": 686_000},
        "catatan": ["Akomodasi 1 kamar untuk 2 orang."],
    },

    "23_pengadaan_kaos_jaket_atribut": {
        "nama": "Pengadaan Kaos/Jaket/Atribut Lainnya Kegiatan Kemahasiswaan",
        "items": {
            "kaos_polo_kemeja_rompi":{"satuan": "O/K", "besaran": 200_000},
            "jaket_hoodie":          {"satuan": "O/K", "besaran": 400_000},
            "topi_atribut_lainnya":  {"satuan": "O/K", "besaran": 150_000},
        },
    },

    "24_bantuan_musibah_mahasiswa": {
        "nama": "Bantuan Mahasiswa yang Mengalami Musibah",
        "besaran": 5_000_000, "satuan": "Orang",
    },

    "25_tiket_pesawat_dalam_negeri_kompetisi": {
        "nama": "Tiket Pesawat Dalam Negeri (PP) Bagi Mahasiswa Mengikuti Kompetisi/Kegiatan Kemahasiswaan",
        "besaran": "at cost",
        "catatan": ["Kelas ekonomi."],
    },

    "26_tiket_pesawat_luar_negeri_kompetisi": {
        "nama": "Tiket Pesawat Luar Negeri (PP) Bagi Mahasiswa Mengikuti Kompetisi/Kegiatan Kemahasiswaan",
        "besaran": "at cost",
        "catatan": ["Kelas ekonomi. Asuransi perjalanan, visa, airport tax at cost."],
    },

    "27_hibah_wirausaha_mahasiswa": {
        "nama": "Hibah Wirausaha Mahasiswa",
        "besaran": 15_000_000, "satuan": "Kelompok",
    },
}


# =============================================================================
# LAMPIRAN III — PENELITIAN/INOVASI/PENGABDIAN MASYARAKAT  (pages 53-67)
# =============================================================================

LAMPIRAN_III = {
    "nama": "Kegiatan Penelitian/Inovasi/Pengabdian kepada Masyarakat/Inkubasi Bisnis/Kekayaan Intelektual",

    "1_pengelolaan_hibah": {
        "nama": "Pengelolaan Kegiatan Hibah Penelitian/Inovasi/Inkubasi Bisnis/Pengabdian kepada Masyarakat",
        "seleksi_proposal": {
            "substansi_penelitian_tkt_1_3":  {"satuan": "O/Proposal", "besaran": 150_000},
            "substansi_penelitian_tkt_4_9":  {"satuan": "O/Proposal", "besaran": 400_000},
            "pengabdian_masyarakat":         {"satuan": "O/Proposal", "besaran": 150_000},
        },
        "review_monev":                       {"uraian": "Review Monitoring & Evaluasi Laporan Kemajuan", "satuan": "Per Laporan", "besaran": 350_000},
        "review_publikasi_fte":               {"uraian": "Review luaran Publikasi Ilmiah Dosen untuk SKS FTE", "satuan": "O/Dokumen", "besaran": 100_000},
        "entry_data_kinerja":                 {"satuan": "O/Data", "besaran": 10_000},
        "pendampingan_tenan":                 {"satuan": "O/B", "besaran": 3_500_000},
        "penilai_tkt":                        {"uraian": "Honorarium Penilai/Pengukur TKT Substansi", "satuan": "O/Judul", "besaran": 700_000},
        "insentif_tkt_4_6":                   {"satuan": "O/Judul", "besaran":  5_000_000},
        "insentif_tkt_7_9":                   {"satuan": "O/Judul", "besaran": 10_000_000},
        "pembuatan_buku_direktori": {
            "penyunting_editor":              {"satuan": "O/Halaman",  "besaran":   200_000},
            "pembuat_kontributor":            {"satuan": "O/Halaman",  "besaran":   250_000},
            "pengolah_data":                  {"satuan": "O/K",        "besaran": 2_500_000},
            "surveyor":                       {"satuan": "O/Kuisioner","besaran":    50_000},
        },
    },

    "2_pelaksanaan_hibah": {
        "nama": "Pelaksanaan Hibah Penelitian/Inovasi/Inkubasi Bisnis/Pengabdian kepada Masyarakat",
        "honorarium_peneliti_pengabdi": {
            "ketua":    {"satuan": "O/J", "besaran": 150_000},
            "anggota":  {"satuan": "O/J", "besaran":  75_000},
        },
        "kelebihan_jam_perekayasaan": {
            "utama":     {"uraian": "Peneliti Utama/Perekayasa Utama",     "satuan": "O/J", "besaran": 60_000},
            "madya":     {"uraian": "Peneliti Madya/Perekayasa Madya",     "satuan": "O/J", "besaran": 50_000},
            "muda":      {"uraian": "Peneliti Muda/Perekayasa Muda",       "satuan": "O/J", "besaran": 40_000},
            "pertama":   {"uraian": "Peneliti Pertama/Perekayasa Pertama", "satuan": "O/J", "besaran": 35_000},
        },
        "penunjang_penelitian": {
            "pembantu_peneliti":      {"satuan": "O/J",         "besaran":    50_000},
            "koordinator_peneliti":   {"satuan": "O/B",         "besaran":   420_000},
            "sekretariat_peneliti":   {"satuan": "O/B",         "besaran":   300_000},
            "pengolah_data":          {"satuan": "Penelitian/Perekayasaan", "besaran": 1_540_000},
            "petugas_survei":         {"satuan": "O/Responden", "besaran":     8_000},
            "pembantu_lapangan":      {"satuan": "O/H",         "besaran":    80_000},
        },
    },

    "3_fasilitasi_hki": {
        "nama": "Fasilitasi Permohonan Hak Kekayaan Intelektual",
        "paten": {
            "honor_drafter":              {"uraian": "Drafter permohonan invensi paten",                             "satuan": "Permohonan",     "besaran": 1_700_000},
            "honor_tim_penilai":          {"uraian": "Tim Penilai Permohonan Invensi Paten",                         "satuan": "O/Permohonan",   "besaran":   500_000},
            "honor_konsultan_hki":        {"uraian": "Konsultan Hak Kekayaan Intelektual",                           "satuan": "Deskripsi Paten","besaran": 1_700_000},
            "honor_asistensi_mediasi":    {"uraian": "Asistensi mediasi permohonan paten",                           "satuan": "Permohonan",     "besaran": 1_700_000},
            "pendaftaran_paten":          {"satuan": "Permohonan",     "besaran": "at cost"},
            "pemeriksaan_substantif":     {"satuan": "Deskripsi Paten","besaran": "at cost"},
            "pemeliharaan_paten":         {"satuan": "Paten/Tahun",    "besaran": "at cost"},
            "percepatan_pengumuman":      {"satuan": "Permohonan",     "besaran": "at cost"},
            "perubahan_data":             {"satuan": "Permohonan",     "besaran": "at cost"},
            "perubahan_jenis":            {"satuan": "Permohonan",     "besaran": "at cost"},
            "pencatatan_lisensi":         {"satuan": "Permohonan",     "besaran": "at cost"},
            "cetak_sertifikat":           {"satuan": "Permohonan",     "besaran": "at cost"},
        },
        "hak_cipta": {
            "honor_tim_penilai":       {"uraian": "Tim Penilai Permohonan Pencatatan Hak Cipta", "satuan": "O/Permohonan", "besaran":   500_000},
            "honor_konsultan_hki":     {"uraian": "Konsultan HKI",                                "satuan": "Permohonan",   "besaran": 1_000_000},
            "pendaftaran_hak_cipta":   {"satuan": "Permohonan", "besaran": "at cost"},
            "salinan_surat_pencatatan":{"satuan": "Permohonan", "besaran": "at cost"},
            "perbaikan_data":          {"satuan": "Permohonan", "besaran": "at cost"},
        },
        "merek": {
            "honor_tim_penilai":          {"uraian": "Tim Penilai Permohonan Pencatatan Merek", "satuan": "O/Permohonan", "besaran":   500_000},
            "permohonan_pendaftaran":     {"satuan": "Permohonan", "besaran":   750_000},
            "perpanjangan_6bln_sebelum":  {"uraian": "Perpanjangan s.d. 6 bulan sebelum/saat berakhirnya perlindungan", "satuan": "Kelas", "besaran": 3_000_000},
            "perpanjangan_6bln_setelah":  {"uraian": "Perpanjangan s.d. 6 bulan setelah berakhirnya perlindungan",      "satuan": "Kelas", "besaran": 6_500_000},
        },
    },

    "4_konferensi_internasional": {
        "nama": "Penyelenggaraan Konferensi Internasional",
        "honorarium_invited_speaker_usd": {
            "kategori_i":   {"satuan": "O/K", "besaran": "USD 770"},
            "kategori_ii":  {"satuan": "O/K", "besaran": "USD 1.100"},
            "kategori_iii": {"satuan": "O/K", "besaran": "USD 1.650"},
        },
        "reviewer_abstrak": {
            "kategori_i":   {"satuan": "O/Artikel", "besaran": 100_000},
            "kategori_ii":  {"satuan": "O/Artikel", "besaran": 150_000},
            "kategori_iii": {"satuan": "O/Artikel", "besaran": 200_000},
        },
        "reviewer_full_paper": {
            "kategori_i":   {"satuan": "O/Artikel", "besaran":   500_000},
            "kategori_ii":  {"satuan": "O/Artikel", "besaran":   750_000},
            "kategori_iii": {"satuan": "O/Artikel", "besaran": 1_000_000},
        },
        "scientific_editor": {
            "head":                      {"uraian": "Head of Scientific Editor",  "satuan": "O/K",       "besaran": 3_500_000},
            "scientific_reviewer":       {"satuan": "O/Artikel", "besaran":   300_000},
            "coordinator_creative":      {"uraian": "Coordinator Creative Editor","satuan": "O/K",       "besaran": 2_000_000},
            "anggota_creative":          {"uraian": "Anggota Creative Editor",    "satuan": "O/Artikel", "besaran":   750_000},
            "scientific_proof":          {"satuan": "O/Artikel", "besaran":   500_000},
        },
        "production_technical_editor": {
            "head":                      {"uraian": "Head of Production/Technical Editor", "satuan": "O/K", "besaran": 3_000_000},
            "coordinator_technical":     {"satuan": "O/K",       "besaran": 2_000_000},
            "reviewer_technical":        {"satuan": "O/Artikel", "besaran":   250_000},
            "technical_editor":          {"satuan": "O/Artikel", "besaran":   400_000},
            "reviewer_bahasa":           {"uraian": "Reviewer Bahasa (Grammar Checking)", "satuan": "O/Artikel", "besaran": 200_000},
            "quality_control":           {"satuan": "O/Artikel", "besaran":   600_000},
        },
        "koordinator_administrator":     {"satuan": "O/Artikel", "besaran": 150_000},
        "moderator": {
            "kategori_i":   {"satuan": "O/K", "besaran":   500_000},
            "kategori_ii":  {"satuan": "O/K", "besaran": 1_000_000},
            "kategori_iii": {"satuan": "O/K", "besaran": 1_500_000},
        },
        "panitia": {
            "ketua":                      {"satuan": "O/K", "besaran": 3_000_000},
            "wakil_ketua":                {"satuan": "O/K", "besaran": 2_000_000},
            "sekretaris_bendahara_koord": {"satuan": "O/K", "besaran": 1_500_000},
            "anggota":                    {"satuan": "O/K", "besaran": 1_000_000},
        },
        "tim_penunjang": {
            "fasilitator": {"satuan": "O/Sesi", "besaran": 1_500_000},
            "mc":          {"satuan": "O/H",    "besaran": 2_000_000},
            "lo":          {"satuan": "O/H",    "besaran":   200_000},
        },
        "publishing_charge":  {"prosiding": "at cost", "jurnal": "at cost"},
        "website_konferensi": {"satuan": "Kegiatan", "besaran": 5_000_000},
        "akomodasi_invited_speaker": {
            "jabodetabek_papua_bali_bunaken": {
                "kategori_i":   {"satuan": "O/H", "besaran": 2_000_000},
                "kategori_ii":  {"satuan": "O/H", "besaran": 2_400_000},
                "kategori_iii": {"satuan": "O/H", "besaran": 2_800_000},
            },
            "kalimantan_riau_lombok_batam": {
                "kategori_i":   {"satuan": "O/H", "besaran": 1_500_000},
                "kategori_ii":  {"satuan": "O/H", "besaran": 1_800_000},
                "kategori_iii": {"satuan": "O/H", "besaran": 2_200_000},
            },
            "daerah_lainnya": {
                "kategori_i":   {"satuan": "O/H", "besaran": 1_000_000},
                "kategori_ii":  {"satuan": "O/H", "besaran": 1_300_000},
                "kategori_iii": {"satuan": "O/H", "besaran": 1_600_000},
            },
        },
        "meeting_package_fullday": {
            "jabodetabek_papua_bali_bunaken":{"satuan": "O/H", "besaran": 800_000},
            "kalimantan_riau_lombok_batam":  {"satuan": "O/H", "besaran": 700_000},
            "daerah_lainnya":                {"satuan": "O/H", "besaran": 600_000},
            "dalam_kampus":                  {"satuan": "O/H", "besaran": 500_000},
        },
        "kategori_h_index": {
            "kategori_i":   {"social_humaniora": "1-3", "health": "1-4", "science_technology":  "2-9"},
            "kategori_ii":  {"social_humaniora": "4-7", "health": "5-8", "science_technology": "10-15"},
            "kategori_iii": {"social_humaniora": ">7",  "health": ">8",  "science_technology":  ">15"},
        },
    },

    "5_pengelolaan_jurnal": {
        "nama": "Pengelolaan Jurnal/Publikasi Ilmiah",
        "reviewer_jurnal": {
            "internasional_scopus_clarivate": {"satuan": "O/Artikel", "besaran": 1_000_000},
            "nasional_sinta":                 {"satuan": "O/Artikel", "besaran":   750_000},
            "lainnya":                        {"satuan": "O/Artikel", "besaran":   500_000},
        },
        "staf_admin_jurnal": {"satuan": "O/B", "besaran": 4_000_000},
        "dewan_editor_seleksi_awal": {
            "internasional_scopus_clarivate": {"satuan": "O/Artikel Masuk", "besaran": 600_000},
            "nasional_sinta":                 {"satuan": "O/Artikel Masuk", "besaran": 400_000},
            "lainnya":                        {"satuan": "O/Artikel Masuk", "besaran": 300_000},
        },
        "dewan_editor": {
            "ketua":                  {"satuan": "O/Artikel Terbit", "besaran": 1_200_000},
            "managing_section_editor":{"satuan": "O/Artikel Terbit", "besaran": 1_100_000},
            "anggota":                {"satuan": "O/Artikel Terbit", "besaran": 1_000_000},
            "rapat_bulanan":          {"satuan": "O/Kedatangan",     "besaran":   250_000},
        },
        "pengelolaan_website_jurnal": {"satuan": "O/B", "besaran": 4_000_000},
        "penyuntingan_bahasa": {
            "terjemahan_artikel": {"satuan": "Halaman",        "besaran": 700_000},
            "english_to_english": {"satuan": "Halaman",        "besaran": 150_000},
            "proofreading":       {"satuan": "Halaman",        "besaran": 450_000},
            "layout_naskah":      {"satuan": "Artikel Terbit", "besaran": 250_000},
            "tim_index_scopus":   {"satuan": "Artikel",        "besaran": 250_000},
        },
        "akselerasi_akreditasi": {
            "borang_sinta":                  {"satuan": "O/Jurnal",     "besaran":  2_000_000},
            "borang_scopus_clarivate":       {"satuan": "O/Jurnal",     "besaran":  3_000_000},
            "pengembangan_scopus_pertama":   {"satuan": "Jurnal",       "besaran": 105_000_000},
            "pengembangan_sinta_pertama":    {"satuan": "Jurnal",       "besaran":  63_000_000},
            "mempertahankan_scopus":         {"satuan": "Jurnal/Tahun", "besaran":  50_000_000},
            "mempertahankan_sinta":          {"satuan": "Jurnal/Tahun", "besaran":  40_000_000},
        },
    },

    "6_fasilitasi_publikasi_dosen": {
        "nama": "Fasilitasi Dosen untuk Publikasi Ilmiah",
        "items": {
            "plafon_submission":    {"uraian": "Plafon Bantuan Submission Artikel",                               "satuan": "Artikel", "besaran": 100_000_000},
            "honor_mentor":         {"uraian": "Honor mentor pendampingan publikasi Internasional",               "satuan": "Artikel", "besaran":  15_000_000},
            "apc_q1_q2":            {"uraian": "Bantuan Article Processing Charge Scopus Q1-Q2",                  "satuan": "Artikel", "besaran":  50_000_000},
        },
    },

    "7_dana_pendamping_eksternal": {
        "nama": "Dana Pendamping/Insentif/Bantuan Penelitian dan Pengabdian Masyarakat Dibiayai Eksternal",
        "proposal_kompetitif_nasional": {"satuan": "Judul", "besaran": 1_500_000},
        "kerja_sama_internasional_by_nilai": {
            "s_d_500jt":   {"uraian": "Nilai s.d. Rp500 juta",                  "satuan": "Kontrak", "besaran":  1_500_000},
            "500jt_1m":    {"uraian": "Nilai di atas Rp500 juta s.d. Rp1 miliar","satuan": "Kontrak", "besaran":  2_000_000},
            "1m_5m":       {"uraian": "Nilai di atas Rp1 miliar s.d. Rp5 miliar","satuan": "Kontrak", "besaran":  5_000_000},
            "5m_10m":      {"uraian": "Nilai di atas Rp5 miliar s.d. Rp10 miliar","satuan": "Kontrak","besaran": 10_000_000},
            "gt_10m":      {"uraian": "Nilai di atas Rp10 miliar",              "satuan": "Kontrak", "besaran": 15_000_000},
        },
        "bantuan_dana_pendampingan": {"uraian": "Maksimal 10% dari Nilai Kontrak", "satuan": "Nilai Kontrak", "besaran": "maksimal 10%"},
    },

    "8_publikasi_bersama_kunjungan_profesor": {
        "nama": "Publikasi Bersama (Mengikuti H-Indeks) - Kunjungan Profesor",
        "honor_dosen_tamu_periset": {"satuan": "O/H", "besaran": 5_500_000},
        "akomodasi_jabodetabek": {
            "kategori_i":   {"satuan": "O/H", "besaran": 2_000_000},
            "kategori_ii":  {"satuan": "O/H", "besaran": 2_400_000},
            "kategori_iii": {"satuan": "O/H", "besaran": 2_800_000},
        },
        "meeting_package_fullday": {
            "jabodetabek_papua_bali_bunaken":{"satuan": "O/H", "besaran": 800_000},
            "dalam_kampus":                  {"satuan": "O/H", "besaran": 500_000},
        },
        "supervisi_bersama_living_cost": {"satuan": "O/H", "besaran": "USD 350"},
    },

    "9_mini_simposium": {
        "nama": "Penyelenggaraan Mini Simposium",
        "nasional": {
            "reviewer_scientific":    {"satuan": "O/Artikel", "besaran":   500_000},
            "seleksi_awal":           {"satuan": "O/Artikel", "besaran":   250_000},
            "panitia": {
                "ketua":                      {"satuan": "O/K", "besaran": 800_000},
                "wakil_ketua":                {"satuan": "O/K", "besaran": 650_000},
                "sekretaris_bendahara_koord": {"satuan": "O/K", "besaran": 500_000},
                "anggota":                    {"satuan": "O/K", "besaran": 300_000},
            },
            "tim_penunjang_lo":       {"satuan": "O/H", "besaran": 100_000},
            "tim_pendukung": {
                "press_conference":       {"satuan": "O/Naskah", "besaran": 250_000},
                "notulen_notulis":        {"satuan": "O/H",      "besaran": 150_000},
                "desainer_publikasi":     {"satuan": "O/K",      "besaran": 500_000},
                "dokumentasi":            {"satuan": "O/K",      "besaran": 700_000},
            },
            "honorarium_rapat":       {"satuan": "O/K",       "besaran":   250_000},
            "insentif_best_paper":    {"satuan": "O/Artikel", "besaran": 2_500_000},
            "jamuan_tamu":            {"satuan": "O/Kali",    "besaran":   150_000},
            "dokumentasi_reward":     {"satuan": "O/K",       "besaran":   700_000},
        },
        "internasional": {
            "reviewer_scientific":    {"satuan": "O/Artikel", "besaran": 750_000},
            "seleksi_awal":           {"satuan": "O/Artikel", "besaran": 300_000},
            "panitia": {
                "ketua":                      {"satuan": "O/K", "besaran": 1_500_000},
                "wakil_ketua":                {"satuan": "O/K", "besaran": 1_100_000},
                "sekretaris_bendahara_koord": {"satuan": "O/K", "besaran":   800_000},
                "anggota":                    {"satuan": "O/K", "besaran":   500_000},
            },
            "tim_penunjang_lo":       {"satuan": "O/H", "besaran": 200_000},
            "tim_pendukung": {
                "press_conference":       {"satuan": "O/Naskah", "besaran":   400_000},
                "notulen_notulis":        {"satuan": "O/H",      "besaran":   250_000},
                "desainer_publikasi":     {"satuan": "O/K",      "besaran":   750_000},
                "dokumentasi":            {"satuan": "O/K",      "besaran": 1_000_000},
            },
            "honorarium_rapat":       {"satuan": "O/K",       "besaran":   250_000},
            "insentif_best_paper":    {"satuan": "O/Artikel", "besaran": 5_000_000},
            "jamuan_tamu":            {"satuan": "O/Kali",    "besaran":   250_000},
        },
    },
}


# =============================================================================
# LAMPIRAN IV — OPERASIONAL MANAJEMEN  (pages 68-95)
# =============================================================================

# Full 34-province table for incidental vehicle rental (sewa kendaraan)
SEWA_KENDARAAN_PER_PROVINSI = {
    # provinsi: {roda_4, roda_6_bus_sedang, roda_6_bus_besar}  IDR per Hari
    "Aceh":                {"roda_4":   930_000, "roda_6_bus_sedang": 3_282_000, "roda_6_bus_besar": 4_638_000},
    "Sumatera Utara":      {"roda_4": 1_111_000, "roda_6_bus_sedang": 2_848_000, "roda_6_bus_besar": 3_475_000},
    "Riau":                {"roda_4":   978_000, "roda_6_bus_sedang": 2_606_000, "roda_6_bus_besar": 3_908_000},
    "Kepulauan Riau":      {"roda_4":   901_000, "roda_6_bus_sedang": 2_373_000, "roda_6_bus_besar": 3_910_000},
    "Jambi":               {"roda_4": 1_005_000, "roda_6_bus_sedang": 4_468_000, "roda_6_bus_besar": 5_752_000},
    "Sumatera Barat":      {"roda_4":   890_000, "roda_6_bus_sedang": 2_124_000, "roda_6_bus_besar": 3_500_000},
    "Sumatera Selatan":    {"roda_4": 1_507_000, "roda_6_bus_sedang": 2_200_000, "roda_6_bus_besar": 4_097_000},
    "Lampung":             {"roda_4":   846_000, "roda_6_bus_sedang": 3_594_000, "roda_6_bus_besar": 5_052_000},
    "Bengkulu":            {"roda_4":   788_000, "roda_6_bus_sedang": 4_763_000, "roda_6_bus_besar": 6_449_000},
    "Bangka Belitung":     {"roda_4": 1_258_000, "roda_6_bus_sedang": 2_781_000, "roda_6_bus_besar": 4_273_000},
    "Banten":              {"roda_4":   972_000, "roda_6_bus_sedang": 2_801_000, "roda_6_bus_besar": 4_120_000},
    "Jawa Barat":          {"roda_4":   932_000, "roda_6_bus_sedang": 2_563_000, "roda_6_bus_besar": 3_519_000},
    "DKI Jakarta":         {"roda_4": 1_139_000, "roda_6_bus_sedang": 2_221_000, "roda_6_bus_besar": 3_439_000},
    "Jawa Tengah":         {"roda_4": 1_270_000, "roda_6_bus_sedang": 2_662_000, "roda_6_bus_besar": 4_237_000},
    "D.I. Yogyakarta":     {"roda_4":   905_000, "roda_6_bus_sedang": 2_207_000, "roda_6_bus_besar": 3_565_000},
    "Jawa Timur":          {"roda_4":   966_000, "roda_6_bus_sedang": 2_446_000, "roda_6_bus_besar": 3_222_000},
    "Bali":                {"roda_4":   925_000, "roda_6_bus_sedang": 2_658_000, "roda_6_bus_besar": 3_536_000},
    "Nusa Tenggara Barat": {"roda_4": 1_103_000, "roda_6_bus_sedang": 2_532_000, "roda_6_bus_besar": 3_369_000},
    "Nusa Tenggara Timur": {"roda_4":   857_000, "roda_6_bus_sedang": 2_548_000, "roda_6_bus_besar": 3_468_000},
    "Kalimantan Barat":    {"roda_4":   868_000, "roda_6_bus_sedang": 3_264_000, "roda_6_bus_besar": 4_289_000},
    "Kalimantan Tengah":   {"roda_4": 1_177_000, "roda_6_bus_sedang": 3_716_000, "roda_6_bus_besar": 5_694_000},
    "Kalimantan Selatan":  {"roda_4":   778_000, "roda_6_bus_sedang": 2_630_000, "roda_6_bus_besar": 3_550_000},
    "Kalimantan Timur":    {"roda_4": 1_100_000, "roda_6_bus_sedang": 2_750_000, "roda_6_bus_besar": 4_829_000},
    "Kalimantan Utara":    {"roda_4": 1_100_000, "roda_6_bus_sedang": 2_713_000, "roda_6_bus_besar": 4_829_000},
    "Sulawesi Utara":      {"roda_4": 1_195_000, "roda_6_bus_sedang": 2_498_000, "roda_6_bus_besar": 3_845_000},
    "Gorontalo":           {"roda_4":   792_000, "roda_6_bus_sedang": 2_504_000, "roda_6_bus_besar": 3_230_000},
    "Sulawesi Barat":      {"roda_4":   850_000, "roda_6_bus_sedang": 2_464_000, "roda_6_bus_besar": 3_282_000},
    "Sulawesi Selatan":    {"roda_4":   796_000, "roda_6_bus_sedang": 2_708_000, "roda_6_bus_besar": 3_434_000},
    "Sulawesi Tengah":     {"roda_4":   824_000, "roda_6_bus_sedang": 2_423_000, "roda_6_bus_besar": 4_212_000},
    "Sulawesi Tenggara":   {"roda_4":   839_000, "roda_6_bus_sedang": 2_609_000, "roda_6_bus_besar": 5_150_000},
    "Maluku":              {"roda_4":   947_000, "roda_6_bus_sedang": 2_872_000, "roda_6_bus_besar": 4_021_000},
    "Maluku Utara":        {"roda_4": 1_061_000, "roda_6_bus_sedang": 3_013_000, "roda_6_bus_besar": 4_170_000},
    "Papua":               {"roda_4": 1_107_000, "roda_6_bus_sedang": 4_082_000, "roda_6_bus_besar": 5_248_000},
    "Papua Barat":         {"roda_4": 1_059_000, "roda_6_bus_sedang": 3_499_000, "roda_6_bus_besar": 4_547_000},
}


LAMPIRAN_IV = {
    "nama": "Kegiatan Operasional Manajemen",

    "1_sewa_kendaraan": {
        "nama": "Sewa Kendaraan Dinas dan Kendaraan Operasional",
        "kendaraan_operasional_kantor": {
            "pick_up":       {"satuan": "B", "besaran":  5_660_000},
            "mini_bus":      {"satuan": "B", "besaran":  6_690_000},
            "double_gardan": {"satuan": "B", "besaran": 14_770_000},
        },
        "sewa_insidentil_per_provinsi": SEWA_KENDARAAN_PER_PROVINSI,
        "catatan": [
            "Sewa insidentil sudah termasuk bahan bakar dan pengemudi (satuan: H).",
            "Roda 4 dimaksud berkapasitas maks 7 seat.",
            "Jika butuh kapasitas >7 seat, dapat 150% dari satuan.",
        ],
    },

    "2_pengadaan_kendaraan": {
        "nama": "Pengadaan Kendaraan Dinas dan Kendaraan Operasional",
        "kendaraan_dinas_pejabat": {
            "kategori_a": {"satuan": "U", "besaran": 700_000_000},
            "kategori_b": {"satuan": "U", "besaran": 500_000_000},
        },
        "kendaraan_operasional": {
            "roda_2":             {"satuan": "U", "besaran":  35_000_000},
            "roda_4_pick_up":     {"satuan": "U", "besaran": 220_000_000},
            "roda_4_mini_bus":    {"satuan": "U", "besaran": 500_000_000},
            "roda_4_double_gardan":{"satuan": "U", "besaran": 500_000_000},
        },
        "kendaraan_bus": {
            "bus_kecil":          {"satuan": "U", "besaran":   360_000_000},
            "bus_sedang":         {"satuan": "U", "besaran":   560_000_000},
            "bus_besar":          {"satuan": "U", "besaran": 1_180_000_000},
        },
    },

    "3_pemeliharaan_operasional_kendaraan": {
        "nama": "Biaya Pemeliharaan dan Operasional Kendaraan Dinas",
        "items": {
            "roda_2":         {"satuan": "U/T", "besaran":  4_500_000},
            "roda_2_patrol":  {"satuan": "U/T", "besaran": 19_000_000},
            "roda_4":         {"satuan": "U/T", "besaran": 36_000_000},
            "roda_4_patrol":  {"satuan": "U/T", "besaran": 76_000_000},
            "roda_6_bus":     {"satuan": "U/T", "besaran": 54_000_000},
            "roda_6_khusus":  {"satuan": "U/T", "besaran": 35_000_000},
        },
    },

    "4_perencanaan_pemeliharaan_fasilitas": {
        "nama": "Perencanaan dan Pemeliharaan Fasilitas",
        "interior_perencanaan": {
            "ahli_madya_harian":     {"uraian": "Ahli Madya - pekerjaan <20 hari kerja (Desain Eksklusif / >10 thn)","satuan": "O/H", "besaran":    850_000},
            "ahli_madya_bulanan":    {"uraian": "Ahli Madya - pekerjaan >=20 hari kerja",                            "satuan": "O/B", "besaran": 15_000_000},
            "ahli_muda_harian":      {"uraian": "Ahli Muda - pekerjaan <20 hari kerja (Standar / 5-10 thn)",          "satuan": "O/H", "besaran":    750_000},
            "ahli_muda_bulanan":     {"uraian": "Ahli Muda - pekerjaan >=20 hari kerja",                              "satuan": "O/B", "besaran": 13_000_000},
            "ahli_pratama_t3_harian":{"uraian": "Ahli Pratama Tingkat 3 (biasa / 4-5 thn)",                          "satuan": "O/H", "besaran":    600_000},
            "ahli_pratama_t2_harian":{"uraian": "Ahli Pratama Tingkat 2 (biasa / 3-4 thn)",                          "satuan": "O/H", "besaran":    500_000},
            "ahli_pratama_t1_harian":{"uraian": "Ahli Pratama Tingkat 1 (biasa / 0-3 thn)",                          "satuan": "O/H", "besaran":    350_000},
            "ahli_pratama_t3_bulanan":{"satuan": "O/B", "besaran": 10_800_000},
            "ahli_pratama_t2_bulanan":{"satuan": "O/B", "besaran":  9_000_000},
            "ahli_pratama_t1_bulanan":{"satuan": "O/B", "besaran":  6_300_000},
        },
        "eksterior_perencanaan": {
            "ahli_madya_harian":  {"uraian": "Desain Infrastruktur/Sipil/Plumbing/ME Eksklusif (>10 thn)","satuan": "O/H", "besaran":    800_000},
            "ahli_madya_bulanan": {"satuan": "O/B", "besaran": 14_000_000},
            "ahli_muda_harian":   {"uraian": "Standar (5-10 thn)",                                       "satuan": "O/H", "besaran":    700_000},
            "ahli_muda_bulanan":  {"satuan": "O/B", "besaran": 12_000_000},
            "ahli_pratama_t3_harian":{"uraian": "Biasa (3-4 thn)", "satuan": "O/H", "besaran": 500_000},
            "ahli_pratama_t2_harian":{"uraian": "Biasa (0-3 thn)", "satuan": "O/H", "besaran": 400_000},
            "ahli_pratama_t1_harian":{"uraian": "Standar (4-5 thn)","satuan": "O/H", "besaran": 250_000},
            "ahli_pratama_t3_bulanan":{"satuan": "O/B", "besaran": 9_000_000},
            "ahli_pratama_t2_bulanan":{"satuan": "O/B", "besaran": 7_200_000},
            "ahli_pratama_t1_bulanan":{"satuan": "O/B", "besaran": 5_000_000},
        },
        "pemeliharaan": {"satuan": "Kegiatan", "besaran": "Maksimal 2,5% dari nilai RAB atau Rp10.000.000"},
        "pelaksana_tpl": {
            "tpl_madya_harian":   {"uraian": "Masa kerja UI >2 thn (termasuk BPJS)", "satuan": "O/H", "besaran": 270_000},
            "tpl_muda_harian":    {"uraian": "Masa kerja UI >1 thn",                 "satuan": "O/H", "besaran": 255_000},
            "tpl_pratama_harian": {"uraian": "Masa kerja UI 0-1 thn",                "satuan": "O/H", "besaran": 240_000},
            "tpl_madya_overtime":   {"satuan": "O/J", "besaran": 30_000},
            "tpl_muda_overtime":    {"satuan": "O/J", "besaran": 28_500},
            "tpl_pratama_overtime": {"satuan": "O/J", "besaran": 27_000},
            "ptpl_harian":         {"uraian": "Pendamping Teknis Pelaksana Lapangan","satuan": "O/H", "besaran": 170_000},
        },
        "pengawas": {
            "lt_30_hari": {"satuan": "O/H", "besaran":   500_000},
            "gte_30_hari":{"satuan": "O/B", "besaran": 9_600_000},
        },
        "perekayasa_alat_mesin": {
            "ahli_madya_harian":  {"satuan": "O/H", "besaran":    800_000},
            "ahli_madya_bulanan": {"satuan": "O/B", "besaran": 14_000_000},
            "ahli_muda_harian":   {"satuan": "O/H", "besaran":    700_000},
            "ahli_muda_bulanan":  {"satuan": "O/B", "besaran": 12_000_000},
            "t5_harian":          {"satuan": "O/H", "besaran": 500_000},
            "t4_harian":          {"satuan": "O/H", "besaran": 400_000},
            "t3_harian":          {"satuan": "O/H", "besaran": 300_000},
            "t2_harian":          {"satuan": "O/H", "besaran": 200_000},
            "t1_harian":          {"satuan": "O/H", "besaran": 170_000},
            "t5_bulanan":         {"satuan": "O/B", "besaran": 10_000_000},
            "t4_bulanan":         {"satuan": "O/B", "besaran":  8_000_000},
            "t3_bulanan":         {"satuan": "O/B", "besaran":  6_000_000},
            "t2_bulanan":         {"satuan": "O/B", "besaran":  5_000_000},
            "t1_bulanan":         {"satuan": "O/B", "besaran":  4_500_000},
        },
        "evaluator": {
            "interior_harian":        {"satuan": "O/H", "besaran":  1_000_000},
            "interior_bulanan":       {"satuan": "O/B", "besaran": 18_000_000},
            "eksterior_harian":       {"satuan": "O/H", "besaran":    850_000},
            "eksterior_bulanan":      {"satuan": "O/B", "besaran": 16_000_000},
            "alat_mesin_harian":      {"satuan": "O/H", "besaran":    700_000},
            "alat_mesin_bulanan":     {"satuan": "O/B", "besaran": 12_000_000},
        },
    },

    "5_pelaksana_konstruksi": {
        "nama": "Kegiatan Pelaksana Konstruksi dan Konstruksi Rancang Bangun",
        "tim_pengelola_teknis": {
            "25m_50m": {
                "pj":      {"satuan": "O/B", "besaran": 750_000},
                "anggota": {"satuan": "O/B", "besaran": 550_000},
            },
            "50m_100m": {
                "pj":      {"satuan": "O/B", "besaran": 1_000_000},
                "anggota": {"satuan": "O/B", "besaran":   750_000},
            },
        },
        "tim_ahli": {
            "10m_25m": {
                "pj":      {"satuan": "O/B", "besaran": 2_500_000},
                "anggota": {"satuan": "O/B", "besaran": 1_500_000},
            },
            "gte_25m": {
                "pj":      {"satuan": "O/B", "besaran": 3_250_000},
                "anggota": {"satuan": "O/B", "besaran": 2_000_000},
            },
        },
        "tim_teknis_pengawas": {
            "10m_25m": {
                "team_leader": {"satuan": "O/B", "besaran": 8_000_000},
                "engineer":    {"satuan": "O/B", "besaran": 7_000_000},
                "pengawas":    {"satuan": "O/B", "besaran": 6_000_000},
                "administrasi":{"satuan": "O/B", "besaran": 1_500_000},
            },
            "gte_25m": {
                "team_leader": {"satuan": "O/B", "besaran": 9_000_000},
                "engineer":    {"satuan": "O/B", "besaran": 8_000_000},
                "pengawas":    {"satuan": "O/B", "besaran": 7_000_000},
                "administrasi":{"satuan": "O/B", "besaran": 2_500_000},
            },
        },
        "tim_penilai_teknis": {"uraian": "Penilai (maks 8 jam per hari)", "satuan": "O/J", "besaran": 1_500_000},
    },

    "6_honor_ketua_sekretaris_anggota": {
        "nama": "Honorarium Ketua/Sekretaris/Anggota (pekerjaan konstruksi lainnya)",
        "besaran": 1_500_000, "satuan": "O/H",
    },

    "7_petugas_eksternal_fasilitas": {
        "nama": "Petugas Eksternal Pemeliharaan, Perbaikan dan Pengamanan Fasilitas",
        "items": {
            "petugas_lt_8jam":     {"uraian": "Petugas PLN/PDAM/Telkom/Pemeliharaan - s.d. 8 jam",   "satuan": "O/H",     "besaran":   250_000},
            "petugas_gt_8jam":     {"uraian": "Petugas PLN/PDAM/Telkom/Pemeliharaan - di atas 8 jam","satuan": "O/H",     "besaran":   400_000},
            "pengamanan_aset":     {"satuan": "O/B", "besaran":   500_000},
            "forum_lpm_beji_depok":{"uraian": "Forum Komunikasi LPM Kecamatan Beji Depok", "satuan": "Organisasi/B", "besaran": 2_000_000},
        },
    },

    "8_tenaga_pendukung_kegiatan": {
        "nama": "Tenaga Pendukung Kegiatan",
        "hari_kerja_gt_8jam": {
            "kebersihan":  {"satuan": "O/H", "besaran":  75_000},
            "pemeliharaan":{"satuan": "O/H", "besaran": 100_000},
        },
        "hari_libur_s_d_8jam": {
            "kebersihan":  {"satuan": "O/H", "besaran": 100_000},
            "pemeliharaan":{"satuan": "O/H", "besaran": 125_000},
        },
        "hari_libur_gt_8jam": {
            "kebersihan":  {"satuan": "O/H", "besaran": 125_000},
            "pemeliharaan":{"satuan": "O/H", "besaran": 150_000},
        },
    },

    "9_swakelola_pengembangan_si": {
        "nama": "Swakelola Pengembangan Sistem Informasi",
        "tenaga_ahli": {
            "ketua_tim_perancangan":  {"satuan": "O/B", "besaran": 5_000_000},
            "ahli_perancangan_si":    {"satuan": "O/B", "besaran": 4_750_000},
            "ahli_perancangan_data":  {"satuan": "O/B", "besaran": 4_750_000},
            "ahli_pemograman":        {"satuan": "O/B", "besaran": 4_000_000},
            "ahli_basis_data":        {"satuan": "O/B", "besaran": 4_000_000},
            "system_analis":          {"satuan": "O/B", "besaran": 4_000_000},
            "software_tester":        {"satuan": "O/B", "besaran": 4_000_000},
            "ahli_web":               {"satuan": "O/B", "besaran": 4_000_000},
            "ahli_jaringan":          {"satuan": "O/B", "besaran": 4_500_000},
        },
        "tenaga_penunjang": {
            "sekretariat":            {"satuan": "O/B", "besaran": 600_000},
            "operator_komputer":      {"satuan": "O/B", "besaran": 550_000},
            "tester_uat":             {"satuan": "O/H", "besaran": 400_000},
        },
    },

    "10_swakelola_tata_kelola_ti": {
        "nama": "Swakelola Penyusunan Tata Kelola Teknologi Informasi",
        "tenaga_ahli": {
            "narasumber":            {"satuan": "O/J", "besaran": 500_000},
            "pendamping_penyusun":   {"satuan": "O/J", "besaran": 400_000},
        },
        "pelaksana_penyusun": {
            "pengarah":          {"satuan": "O/B", "besaran": 1_000_000},
            "pj_penyusun":       {"satuan": "O/B", "besaran":   900_000},
            "ketua_penyusun":    {"satuan": "O/B", "besaran":   800_000},
            "wakil_ketua":       {"satuan": "O/B", "besaran":   700_000},
            "koordinator":       {"satuan": "O/B", "besaran":   600_000},
            "sekretariat":       {"satuan": "O/B", "besaran":   600_000},
            "anggota":           {"satuan": "O/B", "besaran":   550_000},
        },
    },

    "11_duta_baca": {
        "nama": "Duta Baca",
        "mahasiswa": {
            "d3_s1": {"satuan": "O/K", "besaran": 500_000},
            "s2":    {"satuan": "O/K", "besaran": 600_000},
            "s3":    {"satuan": "O/K", "besaran": 750_000},
        },
        "dosen": {
            "s2": {"satuan": "O/K", "besaran": 700_000},
            "s3": {"satuan": "O/K", "besaran": 750_000},
        },
        "tendik": {
            "d3_s1": {"satuan": "O/K", "besaran": 500_000},
            "s2":    {"satuan": "O/K", "besaran": 600_000},
            "s3":    {"satuan": "O/K", "besaran": 700_000},
        },
    },

    "12_pengadaan_seragam": {
        "nama": "Pengadaan Seragam",
        "items": {
            "seragam_pegawai":       {"satuan": "O/Set", "besaran":   750_000},
            "pakaian_kerja_lapangan":{"satuan": "O/Set", "besaran":   650_000},
            "pakaian_satpam":        {"satuan": "O/Set", "besaran":   750_000},
            "jas_almamater":         {"uraian": "Jas Almamater Pejabat/Petugas Protokoler", "satuan": "O/Set", "besaran": 1_500_000},
            "toga_jabatan":          {"satuan": "O/Set", "besaran": 3_500_000},
        },
        "catatan": ["Maks 2 set/tahun untuk seragam pegawai/pakaian kerja. Maks 1 set/tahun untuk jas almamater dan toga jabatan."],
    },

    "13_jamuan_konsumsi": {
        "nama": "Jamuan Tamu Pimpinan dan Konsumsi",
        "jamuan_tamu_kategori_a": {
            "luar_kantor":  {"satuan": "O/K", "besaran": 2_000_000},
            "dalam_kantor": {"satuan": "O/K", "besaran":   500_000},
        },
        "jamuan_tamu_kategori_b": {
            "luar_kantor":  {"satuan": "O/K", "besaran": 500_000},
            "dalam_kantor": {"satuan": "O/K", "besaran": 150_000},
        },
        "konsumsi_kategori_a": {
            "kudapan": {"satuan": "O/K", "besaran":  50_000},
            "makan":   {"satuan": "O/K", "besaran": 100_000},
        },
        "konsumsi_selain_kategori_a": {
            "kudapan": {"satuan": "O/K", "besaran": 35_000},
            "makan":   {"satuan": "O/K", "besaran": 55_000},
        },
    },

    "14_cindera_mata_media_massa": {
        "nama": "Cindera Mata dan Kegiatan Media Massa",
        "items": {
            "cindera_mata_dalam_negeri":   {"satuan": "O/K",         "besaran": 1_500_000},
            "cindera_mata_luar_negeri":    {"satuan": "O/K",         "besaran": 4_000_000},
            "karangan_bunga_parcel":       {"satuan": "O/K",         "besaran": 1_000_000},
            "apresiasi_media_massa":       {"satuan": "O/T",         "besaran":   750_000},
            "bantuan_wartawan_media":      {"satuan": "Institusi/T", "besaran": 5_000_000},
        },
    },

    "15_asuransi_kesehatan": {
        "nama": "Asuransi Kesehatan Pegawai",
        "by_kategori": {
            "kategori_i":   {"satuan": "O/T", "besaran": 7_500_000},
            "kategori_ii":  {"satuan": "O/T", "besaran": 6_500_000},
            "kategori_iii": {"satuan": "O/T", "besaran": 5_500_000},
            "kategori_iv":  {"satuan": "O/T", "besaran": 5_000_000},
            "kategori_v":   {"satuan": "O/T", "besaran": 4_500_000},
        },
        "catatan": ["Maks suami/istri + 2 anak. Sebagai tambahan BPJS Kesehatan."],
    },

    "16_insentif_transpor_kehadiran": {
        "nama": "Insentif dan Transpor Kehadiran",
        "insentif_kehadiran": {"satuan": "O/B", "besaran": 750_000},
        "transpor_kehadiran": {"satuan": "O/H", "besaran":  55_000},
    },

    "17_medical_check_up": {
        "nama": "Medical Check Up",
        "besaran": 4_500_000, "satuan": "O/T",
        "catatan": ["Maks 1x per tahun."],
    },

    "18_bantuan_pernikahan": {
        "nama": "Bantuan Biaya Pernikahan",
        "pegawai":     {"satuan": "K", "besaran": 3_500_000},
        "anak_pegawai":{"satuan": "K", "besaran": 1_200_000},
        "catatan": ["Pegawai tetap UI, pertama kali. Maks 2 anak."],
    },

    "19_bantuan_kelahiran": {
        "nama": "Bantuan Kelahiran Anak",
        "items": {
            "persalinan_normal":      {"satuan": "O/Kelahiran", "besaran": 4_250_000},
            "persalinan_operasi":     {"satuan": "O/Kelahiran", "besaran": 9_000_000},
            "persalinan_penyulit":    {"satuan": "O/Kelahiran", "besaran": 6_000_000},
            "pemeriksaan_kehamilan":  {"satuan": "O/Kelahiran", "besaran": 1_800_000},
            "pemeriksaan_pasca":      {"satuan": "O/Kelahiran", "besaran":   600_000},
        },
        "catatan": ["Anak ke-1 dan ke-2. Sepanjang tidak ditanggung asuransi/BPJS."],
    },

    "20_santunan_duka_cita": {
        "nama": "Santunan Duka Cita",
        "items": {
            "pegawai_tetap":             {"satuan": "O/K", "besaran": 6_000_000},
            "pegawai_tidak_tetap":       {"satuan": "O/K", "besaran": 1_500_000},
            "keluarga_inti_tetap":       {"satuan": "O/K", "besaran": 2_400_000},
            "orang_tua_kandung_tetap":   {"satuan": "O/K", "besaran": 2_100_000},
            "pengantaran_jenazah_luar":  {"uraian": "Bantuan Pengantaran Jenazah Luar Kota", "satuan": "O/K", "besaran": 3_500_000},
        },
    },

    "21_bingkisan_hari_raya": {
        "nama": "Bingkisan Hari Raya Keagamaan",
        "besaran": 1_700_000, "satuan": "O/T",
    },

    "22_bantuan_musibah_pegawai": {
        "nama": "Bantuan atas Musibah (Pegawai)",
        "besaran": 5_000_000, "satuan": "O/K",
    },

    "23_penghargaan_pegawai_berprestasi": {
        "nama": "Penghargaan dan Pembekalan Pegawai Berprestasi",
        "tingkat_universitas": {
            "berprestasi_i":   {"satuan": "K", "besaran": 12_000_000},
            "berprestasi_ii":  {"satuan": "K", "besaran":  9_000_000},
            "berprestasi_iii": {"satuan": "K", "besaran":  6_000_000},
            "berprestasi_iv":  {"satuan": "K", "besaran":  4_000_000},
            "berprestasi_v":   {"satuan": "K", "besaran":  3_000_000},
        },
        "tingkat_fakultas": {
            "berprestasi_i":   {"satuan": "K", "besaran": 6_000_000},
            "berprestasi_ii":  {"satuan": "K", "besaran": 5_000_000},
            "berprestasi_iii": {"satuan": "K", "besaran": 3_500_000},
        },
        "pembekalan_tingkat_nasional": {
            "peserta":    {"satuan": "K", "besaran": 6_000_000},
            "pendamping": {"satuan": "K", "besaran": 2_400_000},
        },
    },

    "24_bantuan_olahraga_seni": {
        "nama": "Bantuan Kegiatan Olahraga dan Seni",
        "kegiatan_rutin":                     {"satuan": "Cabang OR/B", "besaran": 2_500_000},
        "pertandingan_tingkat_universitas":   {"satuan": "K",           "besaran": 25_000_000},
        "pertandingan_tingkat_fakultas":      {"satuan": "K",           "besaran": 10_000_000},
        "beregu_gt_10_orang": {
            "internasional":                  {"satuan": "Kelompok", "besaran": 50_000_000},
            "nasional":                       {"satuan": "Kelompok", "besaran": 10_000_000},
            "universitas_fakultas":           {"satuan": "Kelompok", "besaran":  6_000_000},
        },
        "beregu_6_10_orang": {
            "internasional":                  {"satuan": "Kelompok", "besaran": 30_000_000},
            "nasional":                       {"satuan": "Kelompok", "besaran":  7_500_000},
            "universitas_fakultas":           {"satuan": "Kelompok", "besaran":  4_000_000},
        },
        "perorangan_beregu_2_5_orang": {
            "internasional":                  {"satuan": "Kelompok", "besaran": 10_000_000},
            "nasional":                       {"satuan": "Kelompok", "besaran":  5_000_000},
            "universitas_fakultas":           {"satuan": "Kelompok", "besaran":  2_500_000},
        },
    },

    "25_pengukuhan_guru_besar": {
        "nama": "Bantuan Biaya Pengukuhan Guru Besar",
        "besaran": 10_000_000, "satuan": "O/K",
    },

    "26_publikasi_buku": {
        "nama": "Bantuan Biaya Publikasi Buku",
        "besaran": 20_000_000, "satuan": "O/K",
    },
}


# =============================================================================
# LAMPIRAN V — HONORARIUM KEGIATAN  (pages 96-112)
# =============================================================================

LAMPIRAN_V = {
    "nama": "Honorarium Kegiatan",

    "1_honorarium_kepanitiaan": {
        "nama": "Honorarium Kepanitiaan/Tim Ad Hoc",
        "panitia_inti": {
            "pengarah":                   {"satuan": "O/B", "besaran": 1_000_000},
            "penanggung_jawab":           {"satuan": "O/B", "besaran":   900_000},
            "ketua_pelaksana":            {"satuan": "O/B", "besaran":   800_000},
            "wakil_ketua":                {"satuan": "O/B", "besaran":   700_000},
            "bendahara_sekretaris_koord": {"satuan": "O/B", "besaran":   600_000},
            "anggota":                    {"satuan": "O/B", "besaran":   550_000},
        },
        "tenaga_pendukung": {
            "mc_profesional_offline":   {"satuan": "O/K", "besaran": 5_000_000},
            "mc_profesional_online":    {"satuan": "O/K", "besaran": 2_000_000},
            "mc_pegawai_ui_offline":    {"satuan": "O/K", "besaran": 2_500_000},
            "mc_pegawai_ui_online":     {"satuan": "O/K", "besaran": 1_000_000},
            "mc_mahasiswa_alumni_offline":{"satuan": "O/K", "besaran": 1_500_000},
            "mc_mahasiswa_alumni_online": {"satuan": "O/K", "besaran":   500_000},
            "orasi_ilmiah_internal":    {"satuan": "O/K", "besaran": 3_000_000},
            "orasi_ilmiah_eksternal":   {"satuan": "O/K", "besaran": 5_000_000},
            "penceramah_internal":      {"satuan": "O/K", "besaran": 1_600_000},
            "penceramah_eksternal":     {"satuan": "O/K", "besaran": 2_600_000},
            "pembaca_doa_wisuda":       {"satuan": "O/K", "besaran":   700_000},
            "pembaca_doa_lainnya":      {"satuan": "O/K", "besaran":   400_000},
            "rohaniawan":               {"satuan": "O/K", "besaran":   630_000},
            "petugas_pedel":            {"satuan": "O/K", "besaran": 1_500_000},
            "conductor_utama":          {"satuan": "O/K", "besaran": 1_500_000},
            "co_conductor":             {"satuan": "O/K", "besaran": 1_000_000},
            "penyanyi_pemusik_profesional":{"satuan": "O/K", "besaran": 1_500_000},
            "penyanyi":                 {"satuan": "O/K", "besaran":   750_000},
            "pianis_organis":           {"satuan": "O/K", "besaran": 1_000_000},
            "pelatih_paduan_suara":     {"satuan": "O/K", "besaran":   600_000},
            "asisten_pelatih_paduan":   {"satuan": "O/K", "besaran":   350_000},
            "penyanyi_paduan_mhs":      {"satuan": "O/K", "besaran":   250_000},
            "pemain_orkestra_mhs":      {"satuan": "O/K", "besaran":   300_000},
            "editor_video_audio_lagu":  {"satuan": "O/Lagu", "besaran": 2_500_000},
            "editor_naskah_tata_upacara":{"satuan": "O/K", "besaran":   350_000},
            "pemandu_pembawa_tabung":   {"satuan": "O/K", "besaran":   300_000},
            "koordinator_mc_doa_pemandu":{"satuan": "O/K", "besaran": 1_000_000},
            "sound_engineer_luar":      {"satuan": "O/K", "besaran": 1_500_000},
            "sound_pendukung_luar":     {"satuan": "O/K", "besaran": 1_500_000},
            "liaison_officer":          {"satuan": "O/K", "besaran":   500_000},
        },
        "petugas_lapangan": {
            "koordinator_pengamanan":   {"satuan": "O/Sesi", "besaran": 260_000},
            "petugas_pengamanan":       {"satuan": "O/Sesi", "besaran": 160_000},
            "petugas_kebersihan":       {"satuan": "O/Sesi", "besaran": 160_000},
            "petugas_perlengkapan":     {"satuan": "O/Sesi", "besaran": 160_000},
            "teknisi":                  {"satuan": "O/Sesi", "besaran": 160_000},
            "pemadam_kebakaran_k3l":    {"satuan": "O/Sesi", "besaran": 160_000},
            "protokol_vip_humas":       {"satuan": "O/Sesi", "besaran": 210_000},
            "petugas_konsumsi":         {"satuan": "O/Sesi", "besaran": 260_000},
        },
        "tenaga_medis": {
            "dokter_staf_klinik":       {"satuan": "O/J",      "besaran": 175_000},
            "dokter_non_staf_klinik":   {"satuan": "O/J",      "besaran": 200_000},
            "dokter_spesialis":         {"satuan": "O/J",      "besaran": 300_000},
            "konselor_psikolog_klinis": {"satuan": "O/J",      "besaran": 175_000},
            "ners":                     {"satuan": "O/J",      "besaran": 150_000},
            "perawat_terapis_gigi":     {"satuan": "O/J",      "besaran": 125_000},
            "apoteker":                 {"satuan": "O/J",      "besaran": 175_000},
            "tenaga_teknis_farmasi":    {"satuan": "O/J",      "besaran": 125_000},
            "ahli_lab_medik":           {"satuan": "O/J",      "besaran": 150_000},
            "asisten_ahli_lab_medik":   {"satuan": "O/J",      "besaran": 125_000},
            "pengemudi_ambulance":      {"satuan": "O/5 jam",  "besaran": 225_000},
            "bidan":                    {"satuan": "O/J",      "besaran": 150_000},
            "petugas_rekam_medik":      {"satuan": "O/J",      "besaran": 125_000},
            "medical_administration":   {"satuan": "O/J",      "besaran": 125_000},
            "data_entry_rekam_medik":   {"satuan": "O/J",      "besaran":  75_000},
        },
        "tenaga_pendukung_lainnya": {
            "campus_tour_guide":        {"satuan": "O/H",       "besaran":    55_000},
            "stand_guide_pameran":      {"satuan": "O/H",       "besaran":   210_000},
            "kontributor_berita":       {"satuan": "O/Artikel", "besaran":    80_000},
            "pendataan_employer_survey":{"satuan": "O/Data",    "besaran":    50_000},
            "editor_tracer_study":      {"satuan": "O/B",       "besaran":   600_000},
            "reminder_surveyor_telepon":{"satuan": "O/Responden","besaran":    8_000},
            "reminder_surveyor_langsung":{"satuan": "O/Responden","besaran": 150_000},
            "pemasang_baliho":          {"satuan": "O/H",       "besaran":   150_000},
            "petugas_webinar_job_fair": {"satuan": "O/H",       "besaran":   300_000},
            "petugas_marketing_job_fair":{"satuan": "O/B",      "besaran": 1_000_000},
        },
    },

    "2_kegiatan_kesenian": {
        "nama": "Kegiatan Kesenian",
        "biaya_produksi": {
            "kelompok_nasional":               {"satuan": "O/K", "besaran": 20_000_000},
            "seniman_budayawan_nasional":      {"satuan": "O/K", "besaran": 10_000_000},
            "kelompok_internasional":          {"satuan": "O/K", "besaran": 25_000_000},
            "seniman_budayawan_internasional": {"satuan": "O/K", "besaran": 15_000_000},
        },
        "biaya_penyelenggaraan": {
            "artistic_director": {"satuan": "O/K", "besaran": 2_000_000},
            "curator":           {"satuan": "O/K", "besaran": 1_500_000},
            "sound_engineer":    {"satuan": "O/H", "besaran":   750_000},
            "lighting_designer": {"satuan": "O/H", "besaran":   750_000},
            "stage_manager":     {"satuan": "O/H", "besaran":   750_000},
            "house_manager":     {"satuan": "O/H", "besaran":   500_000},
            "stage_crew":        {"satuan": "O/H", "besaran":   150_000},
            "usher":             {"satuan": "O/H", "besaran":   150_000},
        },
        "kompetisi_seni_budaya": {
            "honor_juri":       {"satuan": "O/K", "besaran": 5_000_000},
            "juara_1_nasional": {"satuan": "O/K", "besaran": 5_000_000},
            "juara_2_nasional": {"satuan": "O/K", "besaran": 3_000_000},
            "juara_3_nasional": {"satuan": "O/K", "besaran": 2_000_000},
        },
    },

    "3_hospitality_tamu_asing": {
        "nama": "Kegiatan Pendampingan/Hospitality Tamu/Mitra Asing",
        "tiket_masuk_wisata": {"satuan": "O/Tiket", "besaran": "at cost"},
        "guide_wisata":       {"satuan": "O/Jam",   "besaran": "at cost"},
    },

    "4_hospitality_mahasiswa_asing": {
        "nama": "Hospitality dalam Pengenalan Budaya dan Pelepasan untuk Mahasiswa Asing",
        "tiket_masuk_wisata":           {"satuan": "O/Tiket", "besaran": "at cost"},
        "bantuan_pengenalan_budaya":    {"satuan": "O/K",     "besaran": 350_000},
    },

    "5_seminar_dan_sejenisnya": {
        "nama": "Seminar dan Sejenisnya",
        "nasional_universitas_fakultas": {
            "narasumber": {
                "menteri_pejabat_setingkat":    {"satuan": "O/J", "besaran": 2_600_000},
                "eselon_i_guru_besar":          {"satuan": "O/J", "besaran": 1_600_000},
                "eselon_ii_s3":                 {"satuan": "O/J", "besaran": 1_300_000},
                "eselon_iii_s2":                {"satuan": "O/J", "besaran": 1_100_000},
                "pakar_dalam_negeri":           {"satuan": "O/J", "besaran": 1_600_000},
                "pakar_luar_negeri":            {"satuan": "O/J", "besaran": 2_600_000},
                "lainnya":                      {"satuan": "O/J", "besaran":   900_000},
            },
            "moderator":   {"satuan": "O/Sesi", "besaran": 750_000},
            "fasilitator": {"satuan": "O/Sesi", "besaran": 650_000},
        },
        "internasional": {
            "narasumber": {
                "menteri_pejabat_setingkat":    {"satuan": "O/J", "besaran":  3_700_000},
                "eselon_i_guru_besar":          {"satuan": "O/J", "besaran":  3_200_000},
                "eselon_ii_s3":                 {"satuan": "O/J", "besaran":  2_600_000},
                "eselon_iii_s2":                {"satuan": "O/J", "besaran":  1_600_000},
                "pakar_dalam_negeri":           {"satuan": "O/J", "besaran":  3_200_000},
                "pakar_luar_negeri":            {"satuan": "O/K", "besaran": 25_000_000},
            },
            "moderator":   {"satuan": "O/Sesi", "besaran": 1_700_000},
            "fasilitator": {"satuan": "O/Sesi", "besaran": 1_100_000},
        },
    },

    "6_rapat_mwa_sa_dgb": {
        "nama": "Rapat MWA/SA/DGB",
        "items": {
            "mwa":             {"satuan": "O/K", "besaran": 500_000},
            "sa_dgb_univ":     {"satuan": "O/K", "besaran": 500_000},
            "sa_fakultas":     {"satuan": "O/K", "besaran": 400_000},
            "dgb_fakultas":    {"satuan": "O/K", "besaran": 400_000},
            "transkriptor":    {"satuan": "O/K", "besaran": 400_000},
        },
        "catatan": ["Honorarium rapat merupakan nilai netto setelah pajak penghasilan."],
    },

    "7_pelatihan_internal": {
        "nama": "Pelatihan Internal",
        "narasumber": {
            "guru_besar":         {"satuan": "O/J", "besaran": 1_400_000},
            "doktor":             {"satuan": "O/J", "besaran": 1_300_000},
            "magister_spesialis": {"satuan": "O/J", "besaran": 1_100_000},
            "sarjana_non_gelar":  {"satuan": "O/J", "besaran":   900_000},
        },
        "fasilitator": {
            "dosen":      {"satuan": "O/J", "besaran": 400_000},
            "tendik":     {"satuan": "O/J", "besaran": 340_000},
            "mahasiswa":  {"satuan": "O/H", "besaran": 230_000},
        },
        "catatan": ["Peserta min 10 orang. Peserta tidak diberi honor/uang harian."],
    },

    "8_penilai_reviewer_pewawancara": {
        "nama": "Penilai/Reviewer/Pewawancara",
        "items": {
            "penilai_publikasi_kenaikan_pangkat": {"uraian": "Penilai publikasi ilmiah untuk kenaikan pangkat/jabatan", "satuan": "O/K", "besaran":   800_000},
            "penilai_kenaikan_fungsional":        {"satuan": "O/K", "besaran":   800_000},
            "penilai_ak_asisten_lektor":          {"uraian": "Angka Kredit Asisten Ahli/Lektor", "satuan": "O/K", "besaran":   800_000},
            "penilai_ak_lektor_kepala_gb_ui":     {"uraian": "Angka Kredit Lektor Kepala/Guru Besar UI", "satuan": "O/K", "besaran": 2_100_000},
        },
        "ak_nasional_by_kategori": {
            "a_jurnal_internasional_bereputasi":  {"uraian": "Jurnal Internasional Bereputasi/Scopus/Nasional Terakreditasi 1-2", "satuan": "O/Judul", "besaran": 150_000},
            "b_book_chapter_nasional_tidak":      {"uraian": "Book Chapter Internasional/Buku Referensi/Nasional <peringkat 2",   "satuan": "O/Judul", "besaran": 100_000},
            "c_selain_a_b":                       {"satuan": "O/Judul", "besaran":  50_000},
        },
        "asesor_bkd":                             {"satuan": "O/K", "besaran": 1_000_000},
        "juri_kegiatan_ketua":                    {"satuan": "O/K", "besaran": 2_300_000},
        "juri_kegiatan_anggota":                  {"satuan": "O/K", "besaran": 2_100_000},
        "auditor_internal_ketua":                 {"satuan": "O/K", "besaran": 4_500_000},
        "auditor_internal_anggota":               {"satuan": "O/K", "besaran": 4_000_000},
        "reviewer_akreditasi_nasional":           {"satuan": "O/Dokumen", "besaran": 6_000_000},
        "reviewer_akreditasi_internasional":      {"satuan": "O/Dokumen", "besaran": 7_500_000},
        "review_evaluasi_internal":               {"satuan": "O/Dokumen", "besaran": 4_000_000},
        "review_monev_elearning":                 {"satuan": "O/Kelas",   "besaran":   600_000},
        "seleksi_bopb_bidikmisi": {
            "verifikasi_berkas": {"satuan": "O/Berkas",    "besaran": 13_000},
            "validasi_berkas":   {"satuan": "O/Berkas",    "besaran": 13_000},
            "wawancara":         {"satuan": "O/Mahasiswa", "besaran": 52_500},
        },
        "wawancara_sasakawa": {
            "s2": {"satuan": "O/Mahasiswa", "besaran": 130_000},
            "s3": {"satuan": "O/Mahasiswa", "besaran": 260_000},
        },
        "wawancara_seleksi_calon_mhs": {
            "s2_profesi":          {"satuan": "O/Mahasiswa", "besaran": 260_000},
            "s1_kelas_internasional":{"satuan": "O/Mahasiswa", "besaran": 370_000},
            "s3":                  {"satuan": "O/Mahasiswa", "besaran": 470_000},
        },
    },

    "9_penerjemahan_pengetikan": {
        "nama": "Penerjemahan dan Pengetikan Dokumen",
        "dari_asing_ke_indonesia_atau_sebaliknya": {
            "bahasa_inggris":       {"satuan": "Halaman", "besaran": 250_000},
            "bahasa_asing_lainnya": {"satuan": "Halaman", "besaran": 400_000},
        },
        "interpreter_lisan": {
            "bahasa_inggris":   {"satuan": "O/K", "besaran": 5_000_000},
            "bahasa_indonesia": {"satuan": "O/K", "besaran": 3_000_000},
        },
        "indonesia_ke_bahasa_daerah": {"satuan": "Halaman", "besaran": 120_000},
    },

    "10_tim_buletin_website": {
        "nama": "Honorarium Tim Penyusunan Buletin/Majalah dan Pengelola Website",
        "buletin_majalah": {
            "penanggung_jawab": {"satuan": "O/B",      "besaran": 400_000},
            "redaktur":         {"satuan": "O/B",      "besaran": 300_000},
            "editor":           {"satuan": "O/Naskah", "besaran": 260_000},
            "desainer_grafis":  {"satuan": "O/Terbit", "besaran": 525_000},
            "fotografer":       {"satuan": "O/Terbit", "besaran": 210_000},
            "peer_reviewer":    {"satuan": "O/Naskah", "besaran": 260_000},
        },
        "tim_website": {
            "penanggung_jawab": {"satuan": "O/B", "besaran": 550_000},
            "redaktur":         {"satuan": "O/B", "besaran": 500_000},
            "penyunting_editor":{"satuan": "O/B", "besaran": 450_000},
        },
        "kontributor_artikel":  {"satuan": "Halaman", "besaran": 125_000},
    },

    "11_pemeriksaan_psikologis": {
        "nama": "Pemeriksaan Psikologis",
        "items": {
            "pemeriksaan":               {"satuan": "O/Peserta", "besaran": 3_000_000},
            "konseling_terapi":          {"satuan": "O/Peserta", "besaran": 2_000_000},
            "wawancara_fgd":             {"satuan": "O/Peserta", "besaran":   750_000},
            "second_opinion":            {"satuan": "O/Laporan", "besaran":   150_000},
            "instruktur_tes":            {"satuan": "O/Sesi",    "besaran":   500_000},
            "pengembangan_materi_simulasi":{"satuan": "O/Materi Simulasi", "besaran": 3_000_000},
            "korektor_master_entry":     {"satuan": "O/Laporan", "besaran":    20_000},
            "finishing_rekapitulasi":    {"satuan": "O/Laporan", "besaran":    15_000},
            "presentasi_hasil":          {"satuan": "O/Sesi",    "besaran": 2_000_000},
        },
    },
}


# =============================================================================
# LAMPIRAN VI — PERJALANAN DINAS  (pages 113-133)
# =============================================================================

# Uang Harian Perjalanan Dinas Dalam Negeri - 34 provinces, 3 columns (IDR per O/H)
UANG_HARIAN_DN_PER_PROVINSI = {
    # provinsi: {luar_kota, dalam_kota_gt_8jam, diklat}
    "Aceh":                {"luar_kota": 360_000, "dalam_kota_gt_8jam": 140_000, "diklat": 110_000},
    "Sumatera Utara":      {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Riau":                {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Kepulauan Riau":      {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Jambi":               {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Sumatera Barat":      {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Sumatera Selatan":    {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Lampung":             {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Bengkulu":            {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Bangka Belitung":     {"luar_kota": 410_000, "dalam_kota_gt_8jam": 160_000, "diklat": 120_000},
    "Banten":              {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Jawa Barat":          {"luar_kota": 430_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Jawa Barat Bogor Depok Bekasi": {"luar_kota": None, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "DKI Jakarta":         {"luar_kota": 530_000, "dalam_kota_gt_8jam": 210_000, "diklat": 160_000},
    "Jawa Tengah":         {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "D.I. Yogyakarta":     {"luar_kota": 420_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Jawa Timur":          {"luar_kota": 410_000, "dalam_kota_gt_8jam": 160_000, "diklat": 120_000},
    "Bali":                {"luar_kota": 480_000, "dalam_kota_gt_8jam": 190_000, "diklat": 140_000},
    "Nusa Tenggara Barat": {"luar_kota": 440_000, "dalam_kota_gt_8jam": 180_000, "diklat": 130_000},
    "Nusa Tenggara Timur": {"luar_kota": 430_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Kalimantan Barat":    {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Kalimantan Tengah":   {"luar_kota": 360_000, "dalam_kota_gt_8jam": 140_000, "diklat": 110_000},
    "Kalimantan Selatan":  {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Kalimantan Timur":    {"luar_kota": 430_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Kalimantan Utara":    {"luar_kota": 430_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Sulawesi Utara":      {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Gorontalo":           {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Sulawesi Barat":      {"luar_kota": 410_000, "dalam_kota_gt_8jam": 160_000, "diklat": 120_000},
    "Sulawesi Selatan":    {"luar_kota": 430_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Sulawesi Tengah":     {"luar_kota": 370_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Sulawesi Tenggara":   {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Maluku":              {"luar_kota": 380_000, "dalam_kota_gt_8jam": 150_000, "diklat": 110_000},
    "Maluku Utara":        {"luar_kota": 430_000, "dalam_kota_gt_8jam": 170_000, "diklat": 130_000},
    "Papua":               {"luar_kota": 580_000, "dalam_kota_gt_8jam": 230_000, "diklat": 170_000},
    "Papua Barat":         {"luar_kota": 480_000, "dalam_kota_gt_8jam": 190_000, "diklat": 140_000},
}

# Penginapan Dalam Negeri per-provinsi by kategori A/B/C&D/E (IDR per O/H)
PENGINAPAN_DN_PER_PROVINSI = {
    "Aceh":                {"A": 4_420_000, "B": 3_526_000, "C_D": 1_294_000, "E": 616_000},
    "Sumatera Utara":      {"A": 4_960_000, "B": 2_195_000, "C_D": 1_100_000, "E": 663_000},
    "Riau":                {"A": 3_820_000, "B": 3_119_000, "C_D": 1_650_000, "E": 852_000},
    "Kepulauan Riau":      {"A": 5_344_000, "B": 2_318_000, "C_D": 1_297_000, "E": 792_000},
    "Jambi":               {"A": 5_000_000, "B": 4_102_000, "C_D": 1_225_000, "E": 580_000},
    "Sumatera Barat":      {"A": 5_236_000, "B": 3_332_000, "C_D": 1_353_000, "E": 701_000},
    "Sumatera Selatan":    {"A": 5_850_000, "B": 3_083_000, "C_D": 1_571_000, "E": 861_000},
    "Lampung":             {"A": 4_491_000, "B": 2_488_000, "C_D": 1_140_000, "E": 580_000},
    "Bengkulu":            {"A": 2_140_000, "B": 1_628_000, "C_D": 1_546_000, "E": 692_000},
    "Bangka Belitung":     {"A": 3_827_000, "B": 2_838_000, "C_D": 1_957_000, "E": 622_000},
    "Banten":              {"A": 5_725_000, "B": 2_373_000, "C_D": 1_080_000, "E": 718_000},
    "Jawa Barat":          {"A": 5_381_000, "B": 2_755_000, "C_D": 1_201_000, "E": 686_000},
    "DKI Jakarta":         {"A": 8_720_000, "B": 2_063_000, "C_D":   992_000, "E": 730_000},
    "Jawa Tengah":         {"A": 4_242_000, "B": 1_850_000, "C_D": 1_024_000, "E": 600_000},
    "D.I. Yogyakarta":     {"A": 5_017_000, "B": 2_695_000, "C_D": 1_384_000, "E": 845_000},
    "Jawa Timur":          {"A": 4_449_000, "B": 2_007_000, "C_D": 1_076_000, "E": 814_000},
    "Bali":                {"A": 5_478_000, "B": 1_946_000, "C_D": 1_348_000, "E": 1_138_000},
    "Nusa Tenggara Barat": {"A": 3_500_000, "B": 2_648_000, "C_D": 1_418_000, "E": 907_000},
    "Nusa Tenggara Timur": {"A": 3_750_000, "B": 2_133_000, "C_D": 1_355_000, "E": 688_000},
    "Kalimantan Barat":    {"A": 2_654_000, "B": 1_923_000, "C_D": 1_125_000, "E": 538_000},
    "Kalimantan Tengah":   {"A": 4_901_000, "B": 3_391_000, "C_D": 1_160_000, "E": 659_000},
    "Kalimantan Selatan":  {"A": 4_797_000, "B": 3_316_000, "C_D": 1_500_000, "E": 697_000},
    "Kalimantan Timur":    {"A": 4_000_000, "B": 2_188_000, "C_D": 1_507_000, "E": 804_000},
    "Kalimantan Utara":    {"A": 4_000_000, "B": 2_735_000, "C_D": 1_507_000, "E": 904_000},
    "Sulawesi Utara":      {"A": 4_919_000, "B": 2_290_000, "C_D": 1_170_000, "E": 978_000},
    "Gorontalo":           {"A": 4_168_000, "B": 3_107_000, "C_D": 1_606_000, "E": 955_000},
    "Sulawesi Barat":      {"A": 4_076_000, "B": 3_098_000, "C_D": 1_075_000, "E": 704_000},
    "Sulawesi Selatan":    {"A": 4_820_000, "B": 1_938_000, "C_D": 1_138_000, "E": 745_000},
    "Sulawesi Tengah":     {"A": 2_309_000, "B": 2_027_000, "C_D": 1_567_000, "E": 951_000},
    "Sulawesi Tenggara":   {"A": 2_475_000, "B": 2_574_000, "C_D": 1_297_000, "E": 786_000},
    "Maluku":              {"A": 3_467_000, "B": 3_240_000, "C_D": 1_048_000, "E": 667_000},
    "Maluku Utara":        {"A": 3_440_000, "B": 3_843_000, "C_D": 1_160_000, "E": 600_000},
    "Papua":               {"A": 3_859_000, "B": 3_318_000, "C_D": 2_521_000, "E": 1_038_000},
    "Papua Barat":         {"A": 3_872_000, "B": 3_341_000, "C_D": 2_056_000, "E": 967_000},
}

# Tiket Pesawat Dalam Negeri PP per kota tujuan (IDR)
TIKET_PESAWAT_DN_PER_KOTA = {
    "Ambon":           {"bisnis": 13_285_000, "ekonomi": 7_081_000},
    "Balikpapan":      {"bisnis":  7_412_000, "ekonomi": 3_797_000},
    "Banda Aceh":      {"bisnis":  7_519_000, "ekonomi": 4_492_000},
    "Bandar Lampung":  {"bisnis":  2_407_000, "ekonomi": 1_583_000},
    "Banjarmasin":     {"bisnis":  5_252_000, "ekonomi": 2_995_000},
    "Batam":           {"bisnis":  4_867_000, "ekonomi": 2_888_000},
    "Bengkulu":        {"bisnis":  4_364_000, "ekonomi": 2_621_000},
    "Biak":            {"bisnis": 14_065_000, "ekonomi": 7_519_000},
    "Denpasar":        {"bisnis":  5_305_000, "ekonomi": 3_262_000},
    "Gorontalo":       {"bisnis":  7_231_000, "ekonomi": 4_824_000},
    "Jambi":           {"bisnis":  4_065_000, "ekonomi": 2_460_000},
    "Jayapura":        {"bisnis": 14_568_000, "ekonomi": 8_193_000},
    "Yogyakarta":      {"bisnis":  4_107_000, "ekonomi": 2_268_000},
    "Kendari":         {"bisnis":  7_658_000, "ekonomi": 4_182_000},
    "Kupang":          {"bisnis":  9_413_000, "ekonomi": 5_081_000},
    "Makassar":        {"bisnis":  7_444_000, "ekonomi": 3_829_000},
    "Malang":          {"bisnis":  4_599_000, "ekonomi": 2_695_000},
    "Mamuju":          {"bisnis":  7_295_000, "ekonomi": 4_867_000},
    "Manado":          {"bisnis": 10_824_000, "ekonomi": 5_102_000},
    "Manokwari":       {"bisnis": 16_226_000, "ekonomi": 10_824_000},
    "Mataram":         {"bisnis":  5_316_000, "ekonomi": 3_230_000},
    "Medan":           {"bisnis":  7_252_000, "ekonomi": 3_808_000},
    "Padang":          {"bisnis":  5_530_000, "ekonomi": 2_952_000},
    "Palangkaraya":    {"bisnis":  4_984_000, "ekonomi": 2_984_000},
    "Palembang":       {"bisnis":  3_861_000, "ekonomi": 2_268_000},
    "Palu":            {"bisnis":  9_348_000, "ekonomi": 5_113_000},
    "Pangkal Pinang":  {"bisnis":  3_412_000, "ekonomi": 2_139_000},
    "Pekanbaru":       {"bisnis":  5_583_000, "ekonomi": 3_016_000},
    "Pontianak":       {"bisnis":  4_353_000, "ekonomi": 2_781_000},
    "Semarang":        {"bisnis":  3_861_000, "ekonomi": 2_182_000},
    "Solo":            {"bisnis":  3_861_000, "ekonomi": 2_342_000},
    "Surabaya":        {"bisnis":  5_466_000, "ekonomi": 2_674_000},
    "Ternate":         {"bisnis": 10_001_000, "ekonomi": 6_664_000},
    "Timika":          {"bisnis": 13_830_000, "ekonomi": 7_487_000},
    "Tanjung Selor":   {"bisnis":  7_424_000, "ekonomi": 4_057_000},
}

# Tiket Pesawat Luar Negeri PP per kota (USD)
TIKET_PESAWAT_LN_PER_KOTA = {
    # Amerika Utara
    "Chicago":         {"bisnis": 6_891, "ekonomi": 3_662, "wilayah": "Amerika Utara"},
    "Houston":         {"bisnis": 6_487, "ekonomi": 3_591, "wilayah": "Amerika Utara"},
    "Los Angeles":     {"bisnis": 5_925, "ekonomi": 3_242, "wilayah": "Amerika Utara"},
    "New York":        {"bisnis": 6_179, "ekonomi": 3_839, "wilayah": "Amerika Utara"},
    "Ottawa":          {"bisnis": 6_924, "ekonomi": 4_083, "wilayah": "Amerika Utara"},
    "San Fransisco":   {"bisnis": 7_138, "ekonomi": 2_987, "wilayah": "Amerika Utara"},
    "Toronto":         {"bisnis": 8_564, "ekonomi": 3_201, "wilayah": "Amerika Utara"},
    "Vancouver":       {"bisnis": 7_458, "ekonomi": 3_277, "wilayah": "Amerika Utara"},
    "Washington":      {"bisnis": 8_652, "ekonomi": 3_930, "wilayah": "Amerika Utara"},
    # Amerika Selatan
    "Bogota":          {"bisnis":  9_426, "ekonomi":  7_713, "wilayah": "Amerika Selatan"},
    "Brazilia":        {"bisnis": 11_518, "ekonomi":  5_970, "wilayah": "Amerika Selatan"},
    "Boenos Aires":    {"bisnis": 15_300, "ekonomi": 10_400, "wilayah": "Amerika Selatan"},
    "Caracas":         {"bisnis": 13_837, "ekonomi":  6_825, "wilayah": "Amerika Selatan"},
    "Paramaribo":      {"bisnis":  9_494, "ekonomi":  7_353, "wilayah": "Amerika Selatan"},
    "Santiago de Chile":{"bisnis":15_539, "ekonomi":  8_900, "wilayah": "Amerika Selatan"},
    "Quito":           {"bisnis": 16_269, "ekonomi": 12_127, "wilayah": "Amerika Selatan"},
    "Lima":            {"bisnis":  8_263, "ekonomi":  5_038, "wilayah": "Amerika Selatan"},
    # Amerika Tengah
    "Meksiko":         {"bisnis":  7_831, "ekonomi": 3_966, "wilayah": "Amerika Tengah"},
    "Havana":          {"bisnis": 11_223, "ekonomi": 7_335, "wilayah": "Amerika Tengah"},
    "Panama City":     {"bisnis":  9_306, "ekonomi": 6_195, "wilayah": "Amerika Tengah"},
    # Eropa Barat
    "Vienna":          {"bisnis": 4_177, "ekonomi": 3_357, "wilayah": "Eropa Barat"},
    "Brussels":        {"bisnis": 5_994, "ekonomi": 3_870, "wilayah": "Eropa Barat"},
    "Marseilles":      {"bisnis": 5_074, "ekonomi": 3_541, "wilayah": "Eropa Barat"},
    "Paris":           {"bisnis": 6_085, "ekonomi": 3_331, "wilayah": "Eropa Barat"},
    "Berlin":          {"bisnis": 6_126, "ekonomi": 3_959, "wilayah": "Eropa Barat"},
    "Bern":            {"bisnis": 6_778, "ekonomi": 4_355, "wilayah": "Eropa Barat"},
    "Bonn":            {"bisnis": 5_023, "ekonomi": 3_753, "wilayah": "Eropa Barat"},
    "Hamburg":         {"bisnis": 7_639, "ekonomi": 4_108, "wilayah": "Eropa Barat"},
    "Geneva":          {"bisnis": 5_370, "ekonomi": 4_333, "wilayah": "Eropa Barat"},
    "Amsterdam":       {"bisnis": 5_898, "ekonomi": 3_331, "wilayah": "Eropa Barat"},
    "Den Haag":        {"bisnis": 5_898, "ekonomi": 3_331, "wilayah": "Eropa Barat"},
    "Frankfurt":       {"bisnis": 4_037, "ekonomi": 1_065, "wilayah": "Eropa Barat"},
    # Eropa Utara
    "Copenhagen":      {"bisnis": 4_920, "ekonomi": 3_730, "wilayah": "Eropa Utara"},
    "Helsinki":        {"bisnis": 5_931, "ekonomi": 3_681, "wilayah": "Eropa Utara"},
    "Stockholm":       {"bisnis": 5_506, "ekonomi": 3_433, "wilayah": "Eropa Utara"},
    "London":          {"bisnis": 7_293, "ekonomi": 4_153, "wilayah": "Eropa Utara"},
    "Oslo":            {"bisnis": 4_773, "ekonomi": 4_049, "wilayah": "Eropa Utara"},
    # Eropa Selatan
    "Sarajevo":        {"bisnis":  7_129, "ekonomi": 6_033, "wilayah": "Eropa Selatan"},
    "Zagreb":          {"bisnis": 10_177, "ekonomi": 5_182, "wilayah": "Eropa Selatan"},
    "Athens":          {"bisnis":  9_256, "ekonomi": 8_041, "wilayah": "Eropa Selatan"},
    "Lisbon":          {"bisnis":  4_746, "ekonomi": 3_383, "wilayah": "Eropa Selatan"},
    "Madrid":          {"bisnis":  4_767, "ekonomi": 3_631, "wilayah": "Eropa Selatan"},
    "Rome":            {"bisnis":  6_000, "ekonomi": 4_500, "wilayah": "Eropa Selatan"},
    "Beograd":         {"bisnis":  6_404, "ekonomi": 5_564, "wilayah": "Eropa Selatan"},
    "Vatican":         {"bisnis":  6_000, "ekonomi": 4_500, "wilayah": "Eropa Selatan"},
    # Eropa Timur
    "Bratislava":      {"bisnis":  4_423, "ekonomi": 3_842, "wilayah": "Eropa Timur"},
    "Bucharest":       {"bisnis":  4_982, "ekonomi": 4_113, "wilayah": "Eropa Timur"},
    "Kiev":            {"bisnis":  6_029, "ekonomi": 5_193, "wilayah": "Eropa Timur"},
    "Moscow":          {"bisnis":  7_206, "ekonomi": 5_143, "wilayah": "Eropa Timur"},
    "Praha":           {"bisnis": 11_848, "ekonomi": 6_748, "wilayah": "Eropa Timur"},
    "Sofia":           {"bisnis":  6_346, "ekonomi": 3_612, "wilayah": "Eropa Timur"},
    "Warsawa":         {"bisnis":  5_052, "ekonomi": 3_447, "wilayah": "Eropa Timur"},
    "Budapest":        {"bisnis":  5_979, "ekonomi": 2_187, "wilayah": "Eropa Timur"},
    # Afrika Barat
    "Dakkar":          {"bisnis": 9_848, "ekonomi": 8_555, "wilayah": "Afrika Barat"},
    "Abuja":           {"bisnis": 7_848, "ekonomi": 6_818, "wilayah": "Afrika Barat"},
    # Afrika Timur
    "Addis Ababa":     {"bisnis": 5_808, "ekonomi": 5_552, "wilayah": "Afrika Timur"},
    "Nairobi":         {"bisnis": 7_966, "ekonomi": 6_081, "wilayah": "Afrika Timur"},
    "Antananarive":    {"bisnis": 9_000, "ekonomi": 8_282, "wilayah": "Afrika Timur"},
    "Dar Es Salaam":   {"bisnis": 6_599, "ekonomi": 5_733, "wilayah": "Afrika Timur"},
    "Harare":          {"bisnis":10_600, "ekonomi": 5_747, "wilayah": "Afrika Timur"},
    # Afrika Selatan
    "Windhoek":        {"bisnis":11_774, "ekonomi": 7_510, "wilayah": "Afrika Selatan"},
    "Cape Town":       {"bisnis": 9_703, "ekonomi": 8_429, "wilayah": "Afrika Selatan"},
    "Johannesburg":    {"bisnis": 9_802, "ekonomi": 7_216, "wilayah": "Afrika Selatan"},
    "Maputo":          {"bisnis": 8_524, "ekonomi": 6_275, "wilayah": "Afrika Selatan"},
    "Pretoria":        {"bisnis": 9_802, "ekonomi": 7_216, "wilayah": "Afrika Selatan"},
    # Afrika Utara
    "Algiers":         {"bisnis": 6_593, "ekonomi": 5_710, "wilayah": "Afrika Utara"},
    "Kairo":           {"bisnis": 7_122, "ekonomi": 4_483, "wilayah": "Afrika Utara"},
    "Khartoum":        {"bisnis": 4_507, "ekonomi": 3_915, "wilayah": "Afrika Utara"},
    "Rabbat":          {"bisnis": 7_721, "ekonomi": 5_665, "wilayah": "Afrika Utara"},
    "Tripoli":         {"bisnis": 5_706, "ekonomi": 4_975, "wilayah": "Afrika Utara"},
    "Tunisia":         {"bisnis": 5_018, "ekonomi": 3_619, "wilayah": "Afrika Utara"},
    # Asia Barat
    "Manama":          {"bisnis": 6_154, "ekonomi": 4_827, "wilayah": "Asia Barat"},
    "Baghdad":         {"bisnis": 4_148, "ekonomi": 3_545, "wilayah": "Asia Barat"},
    "Amman":           {"bisnis": 6_431, "ekonomi": 3_545, "wilayah": "Asia Barat"},
    "Kuwait":          {"bisnis": 4_273, "ekonomi": 3_110, "wilayah": "Asia Barat"},
    "Beirut":          {"bisnis": 4_490, "ekonomi": 3_730, "wilayah": "Asia Barat"},
    "Doha":            {"bisnis": 3_639, "ekonomi": 2_745, "wilayah": "Asia Barat"},
    "Damascus":        {"bisnis": 5_390, "ekonomi": 3_325, "wilayah": "Asia Barat"},
    "Ankara":          {"bisnis": 6_643, "ekonomi": 3_581, "wilayah": "Asia Barat"},
    "Abu Dhabi":       {"bisnis": 4_976, "ekonomi": 2_727, "wilayah": "Asia Barat"},
    "Sanaa":           {"bisnis": 5_878, "ekonomi": 3_679, "wilayah": "Asia Barat"},
    "Jeddah":          {"bisnis": 3_785, "ekonomi": 3_321, "wilayah": "Asia Barat"},
    "Muscat":          {"bisnis": 5_156, "ekonomi": 3_727, "wilayah": "Asia Barat"},
    "Riyadh":          {"bisnis": 3_510, "ekonomi": 3_000, "wilayah": "Asia Barat"},
    "Istanbul":        {"bisnis": 4_435, "ekonomi": 2_467, "wilayah": "Asia Barat"},
    "Dubai":           {"bisnis": 4_207, "ekonomi": 1_920, "wilayah": "Asia Barat"},
    # Asia Tengah
    "Taskent":         {"bisnis":  8_453, "ekonomi": 7_343, "wilayah": "Asia Tengah"},
    "Astana":          {"bisnis": 12_089, "ekonomi": 8_962, "wilayah": "Asia Tengah"},
    "Baku":            {"bisnis":  8_556, "ekonomi": 2_281, "wilayah": "Asia Tengah"},
    # Asia Timur
    "Beijing":         {"bisnis": 2_140, "ekonomi": 1_623, "wilayah": "Asia Timur"},
    "Hongkong":        {"bisnis": 2_633, "ekonomi": 1_257, "wilayah": "Asia Timur"},
    "Osaka":           {"bisnis": 2_686, "ekonomi": 1_864, "wilayah": "Asia Timur"},
    "Tokyo":           {"bisnis": 2_675, "ekonomi": 1_835, "wilayah": "Asia Timur"},
    "Pyongyang":       {"bisnis": 2_220, "ekonomi": 1_660, "wilayah": "Asia Timur"},
    "Seoul":           {"bisnis": 2_966, "ekonomi": 1_737, "wilayah": "Asia Timur"},
    "Shanghai":        {"bisnis": 2_749, "ekonomi": 1_304, "wilayah": "Asia Timur"},
    "Guangzhou":       {"bisnis": 2_749, "ekonomi": 1_304, "wilayah": "Asia Timur"},
    # Asia Selatan
    "Kaboul":          {"bisnis": 3_905, "ekonomi": 3_208, "wilayah": "Asia Selatan"},
    "Teheran":         {"bisnis": 4_600, "ekonomi": 3_200, "wilayah": "Asia Selatan"},
    "Colombo":         {"bisnis": 2_562, "ekonomi": 1_628, "wilayah": "Asia Selatan"},
    "Dhaka":           {"bisnis": 2_417, "ekonomi": 1_092, "wilayah": "Asia Selatan"},
    "Islamabad":       {"bisnis": 3_333, "ekonomi": 2_501, "wilayah": "Asia Selatan"},
    "Karachi":         {"bisnis": 3_633, "ekonomi": 2_321, "wilayah": "Asia Selatan"},
    "New Delhi":       {"bisnis": 2_500, "ekonomi": 1_500, "wilayah": "Asia Selatan"},
    "Mumbai":          {"bisnis": 2_417, "ekonomi": 1_092, "wilayah": "Asia Selatan"},
    # Asia Tenggara
    "Bandar Seri Begawan":{"bisnis": 1_147, "ekonomi": 919, "wilayah": "Asia Tenggara"},
    "Bangkok":         {"bisnis": 1_155, "ekonomi":   823, "wilayah": "Asia Tenggara"},
    "Davao City":      {"bisnis": 2_558, "ekonomi": 1_641, "wilayah": "Asia Tenggara"},
    "Dilli":           {"bisnis":   491, "ekonomi":   350, "wilayah": "Asia Tenggara"},
    "Hanoi":           {"bisnis": 1_833, "ekonomi": 1_656, "wilayah": "Asia Tenggara"},
    "Ho Chi Minh":     {"bisnis": 1_503, "ekonomi": 1_235, "wilayah": "Asia Tenggara"},
    "Johor Bahru":     {"bisnis":   911, "ekonomi":   525, "wilayah": "Asia Tenggara"},
    "Kota Kinabalu":   {"bisnis": 1_427, "ekonomi":   694, "wilayah": "Asia Tenggara"},
    "Kuala Lumpur":    {"bisnis":   659, "ekonomi":   585, "wilayah": "Asia Tenggara"},
    "Kuching":         {"bisnis": 1_900, "ekonomi":   364, "wilayah": "Asia Tenggara"},
    "Manila":          {"bisnis": 1_614, "ekonomi": 1_150, "wilayah": "Asia Tenggara"},
    "Penang":          {"bisnis":   766, "ekonomi":   545, "wilayah": "Asia Tenggara"},
    "Phnom Penh":      {"bisnis": 1_981, "ekonomi": 1_627, "wilayah": "Asia Tenggara"},
    "Singapore":       {"bisnis":   673, "ekonomi":   403, "wilayah": "Asia Tenggara"},
    "Vientiane":       {"bisnis": 2_025, "ekonomi": 1_420, "wilayah": "Asia Tenggara"},
    "Yangon":          {"bisnis": 1_212, "ekonomi": 1_053, "wilayah": "Asia Tenggara"},
    "Tawau":           {"bisnis": 1_427, "ekonomi":   694, "wilayah": "Asia Tenggara"},
    "Songkhla":        {"bisnis": 1_155, "ekonomi":   823, "wilayah": "Asia Tenggara"},
    # Asia Pasifik
    "Canberra":        {"bisnis":  6_304, "ekonomi": 2_500, "wilayah": "Asia Pasifik"},
    "Darwin":          {"bisnis":  4_900, "ekonomi": 3_964, "wilayah": "Asia Pasifik"},
    "Melbourne":       {"bisnis":  3_814, "ekonomi": 2_858, "wilayah": "Asia Pasifik"},
    "Noumea":          {"bisnis":  5_917, "ekonomi": 1_916, "wilayah": "Asia Pasifik"},
    "Perth":           {"bisnis":  1_801, "ekonomi": 1_525, "wilayah": "Asia Pasifik"},
    "Port Moresby":    {"bisnis": 13_835, "ekonomi": 8_252, "wilayah": "Asia Pasifik"},
    "SUVA":            {"bisnis":  4_461, "ekonomi": 2_669, "wilayah": "Asia Pasifik"},
    "Sydney":          {"bisnis":  4_237, "ekonomi": 2_557, "wilayah": "Asia Pasifik"},
    "Vanimo":          {"bisnis":  2_740, "ekonomi": 2_380, "wilayah": "Asia Pasifik"},
    "Wellington":      {"bisnis":  9_830, "ekonomi": 4_120, "wilayah": "Asia Pasifik"},
}

# Transportasi ke/dari bandara per provinsi (IDR per O/Kali)
TRANSPOR_BANDARA_PER_PROVINSI = {
    "Aceh":                123_000, "Sumatera Utara":     256_000, "Riau":               101_000,
    "Kepulauan Riau":      165_000, "Jambi":              147_000, "Sumatera Barat":     190_000,
    "Sumatera Selatan":    179_000, "Lampung":            167_000, "Bengkulu":           109_000,
    "Bangka Belitung":      90_000, "Banten":             536_000, "Jawa Barat":         200_000,
    "DKI Jakarta":         256_000, "Jawa Tengah":         90_000, "D.I. Yogyakarta":    222_000,
    "Jawa Timur":          194_000, "Bali":               189_000, "Nusa Tenggara Barat":231_000,
    "Nusa Tenggara Timur": 116_000, "Kalimantan Barat":   171_000, "Kalimantan Tengah":  134_000,
    "Kalimantan Selatan":  150_000, "Kalimantan Timur":   533_000, "Kalimantan Utara":   218_000,
    "Sulawesi Utara":      138_000, "Gorontalo":          240_000, "Sulawesi Barat":     313_000,
    "Sulawesi Selatan":    166_000, "Sulawesi Tengah":    165_000, "Sulawesi Tenggara":  171_000,
    "Maluku":              240_000, "Maluku Utara":       215_000, "Papua":              431_000,
    "Papua Barat":         236_000,
}

# Uang Harian Luar Negeri per negara, 4 kategori (USD per O/H)
UANG_HARIAN_LN_PER_NEGARA = {
    "Amerika Serikat":    {"A": 659, "B": 563, "C_D": 505, "E": 447},
    "Kanada":             {"A": 552, "B": 467, "C_D": 416, "E": 365},
    "Argentina":          {"A": 534, "B": 402, "C_D": 351, "E": 349},
    "Venezuela":          {"A": 557, "B": 388, "C_D": 344, "E": 343},
    "Brazil":             {"A": 436, "B": 396, "C_D": 378, "E": 351},
    "Chili":              {"A": 434, "B": 370, "C_D": 332, "E": 294},
    "Kolombia":           {"A": 466, "B": 413, "C_D": 405, "E": 365},
    "Peru":               {"A": 459, "B": 352, "C_D": 320, "E": 280},
    "Suriname":           {"A": 398, "B": 364, "C_D": 268, "E": 268},
    "Ekuador":            {"A": 416, "B": 355, "C_D": 319, "E": 283},
    "Meksiko":            {"A": 553, "B": 468, "C_D": 417, "E": 366},
    "Kuba":               {"A": 453, "B": 385, "C_D": 345, "E": 305},
    "Panama":             {"A": 418, "B": 357, "C_D": 320, "E": 283},
    "Austria":            {"A": 504, "B": 453, "C_D": 347, "E": 317},
    "Belgia":             {"A": 538, "B": 456, "C_D": 406, "E": 357},
    "Perancis":           {"A": 548, "B": 464, "C_D": 413, "E": 381},
    "Jerman":             {"A": 485, "B": 415, "C_D": 368, "E": 324},
    "Belanda":            {"A": 485, "B": 416, "C_D": 368, "E": 324},
    "Swiss":              {"A": 636, "B": 570, "C_D": 444, "E": 401},
    "Denmark":            {"A": 569, "B": 491, "C_D": 428, "E": 375},
    "Finlandia":          {"A": 521, "B": 442, "C_D": 394, "E": 346},
    "Norwegia":           {"A": 621, "B": 559, "C_D": 389, "E": 386},
    "Swedia":             {"A": 615, "B": 519, "C_D": 461, "E": 403},
    "Inggris":            {"A": 792, "B": 774, "C_D": 583, "E": 582},
    "Bosnia Herzegovina": {"A": 456, "B": 420, "C_D": 334, "E": 333},
    "Kroasia":            {"A": 555, "B": 506, "C_D": 406, "E": 405},
    "Spanyol":            {"A": 457, "B": 413, "C_D": 335, "E": 296},
    "Yunani":             {"A": 427, "B": 379, "C_D": 327, "E": 289},
    "Italia":             {"A": 702, "B": 637, "C_D": 446, "E": 427},
    "Portugal":           {"A": 425, "B": 382, "C_D": 308, "E": 273},
    "Serbia":             {"A": 417, "B": 375, "C_D": 326, "E": 288},
    "Bulgaria":           {"A": 406, "B": 367, "C_D": 320, "E": 284},
    "Czech":              {"A": 618, "B": 526, "C_D": 447, "E": 367},
    "Hongaria":           {"A": 485, "B": 438, "C_D": 390, "E": 345},
    "Polandia":           {"A": 478, "B": 415, "C_D": 363, "E": 320},
    "Rumania":            {"A": 416, "B": 381, "C_D": 313, "E": 277},
    "Rusia":              {"A": 556, "B": 512, "C_D": 407, "E": 406},
    "Slovakia":           {"A": 437, "B": 394, "C_D": 341, "E": 303},
    "Ukraina":            {"A": 485, "B": 436, "C_D": 375, "E": 331},
    "Nigeria":            {"A": 468, "B": 428, "C_D": 405, "E": 370},
    "Senegal":            {"A": 461, "B": 393, "C_D": 336, "E": 311},
    "Ethiopia":           {"A": 420, "B": 374, "C_D": 330, "E": 285},
    "Kenya":              {"A": 457, "B": 418, "C_D": 344, "E": 308},
    "Madagascar":         {"A": 396, "B": 366, "C_D": 286, "E": 252},
    "Tanzania":           {"A": 458, "B": 386, "C_D": 357, "E": 303},
    "Zimbabwe":           {"A": 430, "B": 400, "C_D": 330, "E": 316},
    "Mozambique":         {"A": 472, "B": 436, "C_D": 356, "E": 319},
    "Namibia":            {"A": 442, "B": 376, "C_D": 312, "E": 269},
    "Afrika Selatan":     {"A": 440, "B": 400, "C_D": 363, "E": 317},
    "Aljazair":           {"A": 394, "B": 361, "C_D": 319, "E": 290},
    "Mesir":              {"A": 481, "B": 426, "C_D": 405, "E": 361},
    "Maroko":             {"A": 403, "B": 353, "C_D": 310, "E": 272},
    "Tunisia":            {"A": 379, "B": 300, "C_D": 266, "E": 237},
    "Sudan":              {"A": 443, "B": 408, "C_D": 358, "E": 280},
    "Libya":              {"A": 456, "B": 393, "C_D": 340, "E": 320},
    "Azerbaijan":         {"A": 498, "B": 459, "C_D": 365, "E": 364},
    "Bahrain":            {"A": 475, "B": 424, "C_D": 284, "E": 217},
    "Irak":               {"A": 461, "B": 392, "C_D": 351, "E": 310},
    "Yordania":           {"A": 504, "B": 428, "C_D": 382, "E": 336},
    "Kuwait":             {"A": 581, "B": 491, "C_D": 437, "E": 383},
    "Libanon":            {"A": 457, "B": 389, "C_D": 348, "E": 307},
    "Qatar":              {"A": 506, "B": 448, "C_D": 349, "E": 290},
    "Arab Suriah":        {"A": 358, "B": 301, "C_D": 272, "E": 243},
    "Turki":              {"A": 456, "B": 364, "C_D": 311, "E": 276},
    "Uni Emirat Arab":    {"A": 594, "B": 502, "C_D": 446, "E": 391},
    "Yaman":              {"A": 353, "B": 249, "C_D": 226, "E": 204},
    "Saudi Arabia":       {"A": 468, "B": 398, "C_D": 356, "E": 314},
    "Kesultanan Oman":    {"A": 516, "B": 437, "C_D": 390, "E": 343},
    "Rep. Rakyat Tiongkok":{"A": 411,"B": 351, "C_D": 315, "E": 279},
    "Hongkong":           {"A": 601, "B": 507, "C_D": 451, "E": 395},
    "Jepang":             {"A": 519, "B": 428, "C_D": 382, "E": 336},
    "Korea Selatan":      {"A": 515, "B": 467, "C_D": 425, "E": 421},
    "Korea Utara":        {"A": 494, "B": 321, "C_D": 300, "E": 278},
    "Afganistan":         {"A": 385, "B": 262, "C_D": 238, "E": 214},
    "Bangladesh":         {"A": 339, "B": 313, "C_D": 243, "E": 238},
    "India":              {"A": 422, "B": 329, "C_D": 327, "E": 325},
    "Pakistan":           {"A": 343, "B": 277, "C_D": 251, "E": 225},
    "Srilangka":          {"A": 388, "B": 332, "C_D": 299, "E": 266},
    "Iran":               {"A": 421, "B": 332, "C_D": 299, "E": 266},
    "Uzbekistan":         {"A": 392, "B": 352, "C_D": 287, "E": 254},
    "Kazakhstan":         {"A": 456, "B": 420, "C_D": 334, "E": 333},
    "Philipina":          {"A": 412, "B": 367, "C_D": 266, "E": 226},
    "Singapura":          {"A": 615, "B": 519, "C_D": 461, "E": 403},
    "Malaysia":           {"A": 394, "B": 304, "C_D": 274, "E": 244},
    "Thailand":           {"A": 392, "B": 330, "C_D": 297, "E": 264},
    "Myanmar":            {"A": 368, "B": 250, "C_D": 210, "E": 196},
    "Laos":               {"A": 380, "B": 277, "C_D": 251, "E": 225},
    "Vietnam":            {"A": 383, "B": 292, "C_D": 244, "E": 219},
    "Brunei Darussalam":  {"A": 374, "B": 278, "C_D": 252, "E": 226},
    "Kamboja":            {"A": 296, "B": 223, "C_D": 201, "E": 196},
    "Timor Leste":        {"A": 392, "B": 354, "C_D": 236, "E": 212},
    "Australia":          {"A": 636, "B": 585, "C_D": 424, "E": 393},
    "Selandia Baru":      {"A": 545, "B": 461, "C_D": 411, "E": 361},
    "Kaledonia Baru":     {"A": 425, "B": 387, "C_D": 299, "E": 266},
    "Papua Nugini":       {"A": 520, "B": 476, "C_D": 429, "E": 376},
    "Fiji":               {"A": 363, "B": 329, "C_D": 221, "E": 179},
}


LAMPIRAN_VI = {
    "nama": "Perjalanan Dinas",

    "1_paket_rapat_luar_kantor": {
        "nama": "Paket Rapat/Pertemuan di Luar Kantor",
        "paket_rapat": {
            "kategori_a": {
                "dki_jakarta":             {"satuan": "O/P", "halfday": 742_000, "fullday": 993_000, "fullboard": 2_257_000},
                "bali_papua":              {"satuan": "O/P", "halfday": 737_000, "fullday": 907_000, "fullboard": 2_523_000},
                "selain_dki_bali_papua":   {"satuan": "O/P", "halfday": 514_000, "fullday": 799_000, "fullboard": 1_914_000},
            },
            "kategori_b": {
                "dki_jakarta":             {"satuan": "O/P", "halfday": 542_000, "fullday": 667_000, "fullboard": 1_347_000},
                "bali_papua":              {"satuan": "O/P", "halfday": 488_000, "fullday": 652_000, "fullboard": 1_569_000},
                "selain_dki_bali_papua":   {"satuan": "O/P", "halfday": 474_000, "fullday": 692_000, "fullboard": 1_110_000},
            },
            "kategori_c_d_e": {
                "dki_jakarta":             {"satuan": "O/P", "halfday": 354_000, "fullday": 433_000, "fullboard": 1_197_000},
                "bali_papua":              {"satuan": "O/P", "halfday": 362_000, "fullday": 441_000, "fullboard": 1_419_000},
                "selain_dki_bali_papua":   {"satuan": "O/P", "halfday": 414_000, "fullday": 498_000, "fullboard":   822_000},
            },
        },
        "uang_harian": {
            "dki_jakarta":           {"satuan": "O/H", "halfday": 110_000, "fullday": 130_000, "fullboard": 180_000},
            "bali_papua":            {"satuan": "O/H", "halfday": 140_000, "fullday": 160_000, "fullboard": 200_000},
            "selain_dki_bali_papua": {"satuan": "O/H", "halfday": 130_000, "fullday": 150_000, "fullboard": 160_000},
        },
        "capacity_building": {
            "doorprize_souvenir": {"satuan": "O/K", "besaran":    100_000},
            "kaos_atribut":       {"satuan": "O/K", "besaran":    150_000},
            "pendukung_acara":    {"satuan": "K",   "besaran": 10_000_000},
        },
        "panitia_sekretariat": {
            "penanggung_jawab": {"satuan": "O/K", "besaran": 750_000},
            "ketua":            {"satuan": "O/K", "besaran": 600_000},
            "anggota":          {"satuan": "O/K", "besaran": 500_000},
        },
    },

    "2_transportasi_darat": {
        "nama": "Transportasi Darat",
        "transpor_lokal_dalam_kota": {
            "dalam_kampus_depok":  {"satuan": "O/Kali", "besaran":  30_000},
            "dalam_kota_depok":    {"satuan": "O/K",    "besaran":  50_000},
            "dalam_kota_jakarta":  {"satuan": "O/K",    "besaran": 100_000},
            "jakarta_depok_one_way":{"satuan": "O/K",   "besaran": 150_000},
        },
        "transpor_luar_batas_kota_one_way": {
            "kota_bogor":          {"satuan": "O/K", "besaran": 200_000},
            "kab_bogor":           {"satuan": "O/K", "besaran": 250_000},
            "tangerang":           {"satuan": "O/K", "besaran": 250_000},
            "bekasi":              {"satuan": "O/K", "besaran": 250_000},
            "kepulauan_seribu":    {"satuan": "O/K", "besaran": 300_000},
            "kota_bandung":        {"satuan": "O/K", "besaran": 300_000},
            "kab_bandung":         {"satuan": "O/K", "besaran": 300_000},
            "banten":              {"satuan": "O/K", "besaran": 300_000},
            "cirebon":             {"satuan": "O/K", "besaran": 300_000},
            "jawa_barat_lainnya":  {"satuan": "O/K", "besaran": 350_000},
        },
        "transpor_wartawan_event_ui": {"satuan": "O/H", "besaran": 200_000},
    },

    "3_tiket_pesawat_dalam_negeri": {
        "nama": "Tiket Pesawat Dalam Negeri (PP)",
        "per_kota": TIKET_PESAWAT_DN_PER_KOTA,
        "satuan": "IDR (estimasi, at cost)",
        "catatan": ["Kategori A: kelas Bisnis. Selain Kategori A: kelas Ekonomi."],
    },

    "4_tiket_pesawat_luar_negeri": {
        "nama": "Tiket Pesawat Luar Negeri (PP)",
        "per_kota": TIKET_PESAWAT_LN_PER_KOTA,
        "satuan": "USD (estimasi, at cost)",
    },

    "5_biaya_pemeriksaan_rapid_swab_pcr": {
        "nama": "Biaya Pemeriksaan Rapid Test, Swab, dan PCR",
        "besaran": "at cost",
        "catatan": ["Maksimal sesuai penetapan standar harga oleh Kementerian Kesehatan."],
    },

    "6_transportasi_bandara": {
        "nama": "Transportasi ke dan dari Bandara/Pelabuhan/Terminal/Stasiun",
        "per_provinsi": TRANSPOR_BANDARA_PER_PROVINSI,
        "satuan": "O/Kali (IDR)",
    },

    "7_penginapan_dalam_negeri": {
        "nama": "Penginapan Dalam Negeri",
        "per_provinsi_kategori": PENGINAPAN_DN_PER_PROVINSI,
        "satuan": "O/H (IDR)",
        "catatan": [
            "Kategori A & B: 1 kamar untuk 1 orang.",
            "Kategori C, D, E: 1 kamar untuk 2 orang.",
        ],
    },

    "8_uang_harian_dalam_negeri": {
        "nama": "Uang Harian Perjalanan Dinas Dalam Negeri",
        "per_provinsi": UANG_HARIAN_DN_PER_PROVINSI,
        "satuan": "O/H (IDR)",
        "catatan": [
            "Komponen uang saku = 40% dari uang harian.",
            "Dalam kota <8 jam: 80% dari dalam_kota_gt_8jam, min 5 jam maks 8 jam.",
            "Mahasiswa penugasan UI: maks 50% dari standar.",
        ],
    },

    "9_uang_harian_luar_negeri": {
        "nama": "Uang Harian Perjalanan Dinas Luar Negeri",
        "per_negara_kategori": UANG_HARIAN_LN_PER_NEGARA,
        "satuan": "O/H (USD)",
        "catatan": [
            "Akomodasi/penginapan ditanggung pengundang: uang harian maks 30%.",
            "Penambahan waktu perjalanan 1 hari sebelum/sesudah: 50% dari standar.",
        ],
    },
}


# =============================================================================
# LAMPIRAN VII — PENYELENGGARAAN PENERIMAAN MAHASISWA BARU  (pages 134-141)
# =============================================================================

LAMPIRAN_VII = {
    "nama": "Penyelenggaraan Penerimaan Mahasiswa Baru",

    "1_pembuatan_naskah_soal": {
        "nama": "Pembuatan Naskah dan Penilaian Soal",
        "penulisan_soal": {
            "soal_utama_sesuai_pedoman":       {"satuan": "O/Butir Soal", "besaran": 100_000},
            "soal_utama_lolos_seleksi":        {"satuan": "O/Butir Soal", "besaran": 120_000},
            "soal_kelas_internasional_pedoman":{"satuan": "O/Butir Soal", "besaran": 120_000},
            "soal_kelas_internasional_lolos":  {"satuan": "O/Butir Soal", "besaran": 100_000},
        },
        "seleksi_rakit": {
            "seleksi_soal": {"satuan": "O/Butir Soal", "besaran": 120_000},
            "rakit_soal":   {"satuan": "O/Butir Soal", "besaran": 120_000},
        },
        "validasi_materi_bahasa": {
            "soal_teknis_matematis":     {"satuan": "O/Butir Soal", "besaran": 65_000},
            "soal_non_teknis_matematis": {"satuan": "O/Butir Soal", "besaran": 40_000},
            "soal_divalidasi_bahasa":    {"satuan": "O/Butir Soal", "besaran": 50_000},
        },
        "pengacakan_validasi_set":       {"satuan": "O/Butir Soal", "besaran": 10_000},
        "tim_pendukung": {
            "it_pengolah_data":          {"satuan": "O/Butir Soal", "besaran": 25_000},
            "entri_edit_soal":           {"satuan": "O/Butir Soal", "besaran": 10_000},
        },
        "peka_bahasa_inggris": {
            "peka_lolos":                {"satuan": "O/Butir Soal", "besaran": 200_000},
            "reading_lolos":             {"satuan": "O/Butir Soal", "besaran": 175_000},
            "structure_lolos":           {"satuan": "O/Butir Soal", "besaran": 175_000},
            "review_soal":               {"satuan": "O/Butir Soal", "besaran":  75_000},
            "validasi_materi":           {"satuan": "O/Butir Soal", "besaran":  80_000},
            "validasi_bahasa":           {"satuan": "O/Butir Soal", "besaran":  10_000},
        },
    },

    "2_pengolahan_data_seleksi": {
        "nama": "Pengolahan Data Seleksi Masuk",
        "pengembangan_it": {
            "programmer":             {"satuan": "O/B", "besaran": 5_000_000},
            "pengelola_data":         {"satuan": "O/B", "besaran": 3_000_000},
            "narasumber_mata_uji":    {"satuan": "O/B", "besaran": 4_000_000},
        },
        "validasi_penilaian_lju": {
            "penerimaan_lju":              {"satuan": "O/LJU", "besaran": 1_000},
            "validasi_lju":                {"satuan": "O/LJU", "besaran": 6_000},
            "pemindaian_lju":              {"satuan": "O/LJU", "besaran": 2_000},
            "validasi_kunci_kecurangan":   {"satuan": "O/LJU", "besaran": 1_000},
            "penilaian_alokasi":           {"satuan": "O/LJU", "besaran": 1_000},
        },
    },

    "3_panitia_lokal_pengawas_ujian": {
        "nama": "Honorarium Panitia Lokal dan Pengawas Ujian",
        "panitia_lokal": {
            "ketua_panlok":                  {"satuan": "O/K", "besaran": 30_000_000},
            "sekretaris_panlok":             {"satuan": "O/K", "besaran": 25_000_000},
            "bendahara_panlok":              {"satuan": "O/K", "besaran": 25_000_000},
            "koordinator_lapangan":          {"satuan": "O/K", "besaran": 10_000_000},
            "anggota_panlok":                {"satuan": "O/K", "besaran":  5_000_000},
            "sekretariat_panlok":            {"satuan": "O/K", "besaran":  6_000_000},
            "pjs_jakarta_depok":             {"satuan": "O/K", "besaran":  2_700_000},
            "tim_material_jakarta_depok":    {"satuan": "O/K", "besaran":  1_700_000},
        },
        "petugas_luar_jakarta_depok": {
            "pjw": {"satuan": "O/H", "besaran": 1_700_000},
            "pjl": {"satuan": "O/H", "besaran": 1_500_000},
            "pjs": {"satuan": "O/H", "besaran": 1_100_000},
            "tm_mahasiswa":   {"satuan": "O/H", "besaran": 1_000_000},
            "tm_karyawan":    {"satuan": "O/H", "besaran": 1_000_000},
            "pembuka_peti":   {"satuan": "O/Peti", "besaran": 100_000},
        },
        "pengawas_tulis_cetak": {
            "pjl":                    {"satuan": "O/K",   "besaran": 1_400_000},
            "wpjl":                   {"satuan": "O/K",   "besaran": 1_200_000},
            "bl":                     {"satuan": "O/K",   "besaran":   800_000},
            "krg_krpt":               {"satuan": "O/K",   "besaran":   700_000},
            "pengawas_guru":          {"satuan": "O/K",   "besaran":   600_000},
            "pengawas_mahasiswa":     {"satuan": "O/K",   "besaran":   500_000},
            "tk":                     {"satuan": "O/K",   "besaran":   200_000},
            "pam":                    {"satuan": "O/K",   "besaran":   200_000},
            "sewa_ruang":             {"satuan": "Ruang", "besaran":   150_000},
        },
        "pengawas_tulis_komputer": {
            "pjl":                    {"satuan": "O/H",   "besaran":   800_000},
            "wpjl":                   {"satuan": "O/K",   "besaran": 1_200_000},
            "bl":                     {"satuan": "O/K",   "besaran":   800_000},
            "krg_krpt":               {"satuan": "O/K",   "besaran":   700_000},
            "pengawas_guru":          {"satuan": "O/K",   "besaran":   600_000},
            "pengawas_mahasiswa":     {"satuan": "O/K",   "besaran":   500_000},
            "teknisi_server":         {"satuan": "O/H",   "besaran":   500_000},
            "teknisi_jaringan":       {"satuan": "O/H",   "besaran":   500_000},
            "teknisi_lab":            {"satuan": "O/H",   "besaran":   500_000},
            "teknisi_listrik":        {"satuan": "O/K",   "besaran":   600_000},
            "teknisi_genset":         {"satuan": "O/K",   "besaran":   600_000},
            "teknisi_pln":            {"satuan": "O/K",   "besaran":   600_000},
            "tk":                     {"satuan": "O/K",   "besaran":   200_000},
            "pam":                    {"satuan": "O/K",   "besaran":   200_000},
            "sewa_ruang":             {"satuan": "Ruang", "besaran":   300_000},
            "sewa_komputer":          {"satuan": "U/H",   "besaran":   150_000},
        },
    },

    "4_ppkb_talent_scouting": {
        "nama": "Seleksi Jalur Prestasi dan PPKB / Talent Scouting",
        "tim_evaluasi": {
            "perumusan_indeks_sekolah":    {"satuan": "O/K",         "besaran":  8_000_000},
            "perbaikan_pengujian_sistem":  {"satuan": "O/K",         "besaran": 20_000_000},
            "evaluasi_prodi":              {"satuan": "O/Pendaftar", "besaran":     30_000},
            "evaluasi_fakultas":           {"satuan": "O/Pendaftar", "besaran":     30_000},
            "evaluasi_universitas":        {"satuan": "O/Pendaftar", "besaran":     15_000},
        },
        "tim_validasi_penetapan": {
            "validasi_hasil_evaluasi":     {"satuan": "O/Pendaftar",   "besaran":    15_000},
            "penentu_penerimaan_final":    {"satuan": "O/K",           "besaran": 5_000_000},
            "verifikasi_rapor":            {"satuan": "O/Maba Diterima","besaran":   100_000},
        },
        "panitia_inti": {
            "pengarah":          {"satuan": "O/K", "besaran": 2_500_000},
            "pengarah_2":        {"satuan": "O/K", "besaran": 2_200_000},
            "ketua":             {"satuan": "O/K", "besaran": 2_000_000},
            "sekretaris":        {"satuan": "O/K", "besaran": 1_500_000},
            "anggota":           {"satuan": "O/K", "besaran": 1_000_000},
        },
    },

    "5_panitia_inti_pmb": {
        "nama": "Honorarium Panitia Inti Penerimaan Mahasiswa Baru",
        "items": {
            "pengarah":             {"satuan": "O/B", "besaran": 5_000_000},
            "penanggung_jawab":     {"satuan": "O/B", "besaran": 4_750_000},
            "ketua_pelaksana":      {"satuan": "O/B", "besaran": 4_500_000},
            "wakil_ketua":          {"satuan": "O/B", "besaran": 4_250_000},
            "sekretaris_pj_bidang": {"satuan": "O/B", "besaran": 4_000_000},
            "koordinator_subbidang":{"satuan": "O/B", "besaran": 3_500_000},
            "anggota":              {"satuan": "O/B", "besaran": 3_000_000},
        },
    },

    "6_panitia_pelaksana_lokal": {
        "nama": "Honorarium Panitia Pelaksana/Panitia Lokal",
        "items": {
            "penanggung_jawab":  {"satuan": "O/B", "besaran": 1_000_000},
            "koordinator":       {"satuan": "O/B", "besaran":   800_000},
            "anggota":           {"satuan": "O/B", "besaran":   700_000},
        },
    },

    "7_penilai_esai_simak": {
        "nama": "Honorarium Penilai Esai SIMAK",
        "items": {
            "penilai_esai":     {"satuan": "O/Pendaftar", "besaran": 50_000},
            "pengembang_it":    {"satuan": "O/Pendaftar", "besaran": 30_000},
        },
    },

    "8_registrasi_obm": {
        "nama": "Honorarium Panitia Registrasi Mahasiswa Baru dan Orientasi Belajar Mahasiswa",
        "registrasi_maba": {
            "pengarah":                    {"satuan": "O/H", "besaran": 400_000},
            "penanggung_jawab":            {"satuan": "O/H", "besaran": 350_000},
            "ketua_pelaksana":             {"satuan": "O/H", "besaran": 325_000},
            "wakil_ketua":                 {"satuan": "O/H", "besaran": 300_000},
            "bendahara":                   {"satuan": "O/H", "besaran": 275_000},
            "koord_verifikasi_data":       {"satuan": "O/H", "besaran": 275_000},
            "koord_berkas_registrasi":     {"satuan": "O/H", "besaran": 275_000},
            "koord_dsti":                  {"satuan": "O/H", "besaran": 275_000},
            "koord_keuangan":              {"satuan": "O/H", "besaran": 275_000},
            "koord_fasilitas":             {"satuan": "O/H", "besaran": 225_000},
            "anggota_direktorat_pendidikan":{"satuan": "O/H", "besaran": 225_000},
            "anggota_dsti":                {"satuan": "O/H", "besaran": 225_000},
            "anggota_fasilitas":           {"satuan": "O/H", "besaran": 175_000},
            "anggota_keuangan":            {"satuan": "O/H", "besaran": 225_000},
            "anggota_fakultas":            {"satuan": "O/H", "besaran": 225_000},
            "anggota_kemahasiswaan":       {"satuan": "O/H", "besaran": 175_000},
            "anggota_k3l":                 {"satuan": "O/H", "besaran": 175_000},
            "anggota_berkas_registrasi":   {"satuan": "O/H", "besaran": 225_000},
            "anggota_keamanan":            {"satuan": "O/H", "besaran": 100_000},
            "anggota_kebersihan":          {"satuan": "O/H", "besaran":  75_000},
            "samaba":                      {"uraian": "Sahabat Mahasiswa Baru", "satuan": "O/H", "besaran": 75_000},
            "pengemudi_bus":               {"satuan": "O/H", "besaran": 100_000},
            "verifikator_pra_registrasi":  {"satuan": "O/Mhs","besaran":  2_000},
        },
        "orientasi_belajar_obm": {
            "pengarah":             {"satuan": "O/K", "besaran": 2_900_000},
            "penanggung_jawab":     {"satuan": "O/K", "besaran": 2_800_000},
            "ketua_pelaksanaan":    {"satuan": "O/K", "besaran": 2_800_000},
            "koordinator_pusat":    {"satuan": "O/K", "besaran": 2_600_000},
            "wakil_koord_pusat":    {"satuan": "O/K", "besaran": 2_250_000},
            "koordinator_lokasi":   {"satuan": "O/K", "besaran": 2_000_000},
            "anggota_koord_pusat":  {"satuan": "O/K", "besaran": 1_600_000},
            "teknisi_lab":          {"satuan": "O/H", "besaran":   150_000},
            "petugas_administrasi": {"satuan": "O/H", "besaran":   175_000},
            "petugas_ruang_kebersihan":{"satuan": "O/H", "besaran":120_000},
            "narasumber_obm":       {"satuan": "O/H", "besaran":   595_000},
            "asisten_narasumber":   {"satuan": "O/H", "besaran":   350_000},
        },
    },
}


# =============================================================================
# MASTER TREE
# =============================================================================

SBM_UI_2024 = {
    "metadata": METADATA,
    "kategori_pegawai": KATEGORI_PEGAWAI,
    "satuan": SATUAN,
    "lampiran": {
        "I":   LAMPIRAN_I,
        "II":  LAMPIRAN_II,
        "III": LAMPIRAN_III,
        "IV":  LAMPIRAN_IV,
        "V":   LAMPIRAN_V,
        "VI":  LAMPIRAN_VI,
        "VII": LAMPIRAN_VII,
    },
}


# =============================================================================
# QUERY HELPERS
# =============================================================================

def format_rupiah(amount):
    """Format number as Indonesian Rupiah, or pass through strings."""
    if isinstance(amount, str):
        return amount
    if amount is None:
        return "-"
    return f"Rp{amount:,.0f}".replace(",", ".")


def search_rules(keyword: str) -> list:
    """Recursively search all lampiran for entries whose key/uraian matches keyword.
    Returns a list of (path, node) tuples.
    """
    keyword = keyword.lower()
    results = []

    def _search(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                cp = f"{path} > {key}" if path else key
                if keyword in key.lower():
                    results.append((cp, value))
                elif isinstance(value, dict) and "uraian" in value and keyword in str(value["uraian"]).lower():
                    results.append((cp, value))
                _search(value, cp)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                _search(item, f"{path}[{i}]")

    for lamp_key, lamp_data in SBM_UI_2024["lampiran"].items():
        _search(lamp_data, f"Lampiran {lamp_key}")
    return results


def lookup_rate(lampiran: str, *path):
    """Direct lookup. Example: lookup_rate('I', '1_honorarium_dosen_tamu', 'dosen_tamu_luar_negeri')."""
    try:
        node = SBM_UI_2024["lampiran"][lampiran]
        for p in path:
            node = node[p]
        return node
    except (KeyError, TypeError) as e:
        return {"error": f"Not found: {e}"}


# --- specific-domain helpers ------------------------------------------------

def get_sewa_kendaraan(provinsi: str, jenis: str = "roda_4"):
    """jenis: roda_4, roda_6_bus_sedang, roda_6_bus_besar (per H)."""
    data = SEWA_KENDARAAN_PER_PROVINSI.get(provinsi)
    if not data: return f"Provinsi '{provinsi}' tidak ditemukan."
    return format_rupiah(data.get(jenis, None))


def get_uang_harian_dalam_negeri(provinsi: str, tipe: str = "luar_kota"):
    """tipe: luar_kota, dalam_kota_gt_8jam, diklat (per O/H)."""
    data = UANG_HARIAN_DN_PER_PROVINSI.get(provinsi)
    if not data: return f"Provinsi '{provinsi}' tidak ditemukan."
    return format_rupiah(data.get(tipe, None))


def get_penginapan_dalam_negeri(provinsi: str, kategori: str):
    """kategori: A, B, C_D, E (per O/H)."""
    data = PENGINAPAN_DN_PER_PROVINSI.get(provinsi)
    if not data: return f"Provinsi '{provinsi}' tidak ditemukan."
    return format_rupiah(data.get(kategori, None))


def get_uang_harian_luar_negeri(negara: str, kategori: str):
    """kategori: A, B, C_D, E (per O/H, USD)."""
    data = UANG_HARIAN_LN_PER_NEGARA.get(negara)
    if not data: return f"Negara '{negara}' tidak ditemukan."
    val = data.get(kategori, None)
    return f"USD {val}" if val is not None else "-"


def get_tiket_pesawat_dn(kota: str, kelas: str = "ekonomi"):
    """kelas: bisnis atau ekonomi (IDR, estimasi at cost)."""
    data = TIKET_PESAWAT_DN_PER_KOTA.get(kota)
    if not data: return f"Kota '{kota}' tidak ditemukan."
    return format_rupiah(data.get(kelas, None))


def get_tiket_pesawat_ln(kota: str, kelas: str = "ekonomi"):
    """kelas: bisnis atau ekonomi (USD, estimasi at cost)."""
    data = TIKET_PESAWAT_LN_PER_KOTA.get(kota)
    if not data: return f"Kota '{kota}' tidak ditemukan."
    val = data.get(kelas, None)
    return f"USD {val:,}" if val is not None else "-"


def get_transpor_bandara(provinsi: str):
    val = TRANSPOR_BANDARA_PER_PROVINSI.get(provinsi)
    if val is None: return f"Provinsi '{provinsi}' tidak ditemukan."
    return format_rupiah(val)


def get_pembimbingan_ta(program: str):
    """program: key di LAMPIRAN_I['7_pembimbingan_tugas_akhir']['items']."""
    data = LAMPIRAN_I["7_pembimbingan_tugas_akhir"]["items"]
    if program not in data: return f"Program '{program}' tidak ditemukan."
    return format_rupiah(data[program]["besaran"])


def get_kepanitiaan_rate(group: str, jabatan: str):
    """group: panitia_inti / tenaga_pendukung / petugas_lapangan / tenaga_medis / tenaga_pendukung_lainnya."""
    data = LAMPIRAN_V["1_honorarium_kepanitiaan"]
    grp = data.get(group)
    if not grp or jabatan not in grp:
        return f"Not found: {group}/{jabatan}"
    return format_rupiah(grp[jabatan]["besaran"])


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("STANDAR BIAYA UNIVERSITAS INDONESIA 2024 - RULES ENGINE")
    print("Peraturan Rektor No. 16 Tahun 2024")
    print("=" * 70)

    print("\n--- Uang Harian DKI Jakarta (luar kota) ---")
    print(f"  {get_uang_harian_dalam_negeri('DKI Jakarta', 'luar_kota')}")

    print("\n--- Penginapan DKI Jakarta per Kategori ---")
    for k in ["A", "B", "C_D", "E"]:
        print(f"  Kategori {k}: {get_penginapan_dalam_negeri('DKI Jakarta', k)}")

    print("\n--- Sewa Kendaraan Bali ---")
    for j in ["roda_4", "roda_6_bus_sedang", "roda_6_bus_besar"]:
        print(f"  {j}: {get_sewa_kendaraan('Bali', j)}")

    print("\n--- Uang Harian Luar Negeri Jepang ---")
    for k in ["A", "B", "C_D", "E"]:
        print(f"  Kategori {k}: {get_uang_harian_luar_negeri('Jepang', k)}")

    print("\n--- Tiket Pesawat Denpasar ---")
    print(f"  Bisnis:  {get_tiket_pesawat_dn('Denpasar', 'bisnis')}")
    print(f"  Ekonomi: {get_tiket_pesawat_dn('Denpasar', 'ekonomi')}")

    print("\n--- Tiket Pesawat Singapore ---")
    print(f"  Bisnis:  {get_tiket_pesawat_ln('Singapore', 'bisnis')}")
    print(f"  Ekonomi: {get_tiket_pesawat_ln('Singapore', 'ekonomi')}")

    print("\n--- Pembimbingan TA Doktor Promotor ---")
    print(f"  {get_pembimbingan_ta('doktor_promotor')}")

    print("\n--- Kepanitiaan Ketua Pelaksana ---")
    print(f"  {get_kepanitiaan_rate('panitia_inti', 'ketua_pelaksana')}")

    print("\n--- Search 'wisuda' ---")
    for path, item in search_rules("wisuda")[:5]:
        if isinstance(item, dict) and "besaran" in item:
            print(f"  {path} -> {format_rupiah(item['besaran'])} per {item.get('satuan','')}")

    print("\n" + "=" * 70)
    print("Loaded 7 Lampiran:")
    for key, lamp in SBM_UI_2024["lampiran"].items():
        sections = sum(1 for k in lamp.keys() if k not in ("nama", "catatan"))
        print(f"  {key:5}. {lamp['nama']} — {sections} sections")
    print("=" * 70)
