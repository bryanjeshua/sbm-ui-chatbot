import os
import json
import time
from pathlib import Path
import google.generativeai as genai
from PIL import Image

PAGES_DIR = Path("sbm_pages")
OUTPUT_FILE = Path("sbm_extracted_text.json")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

DELAY_BETWEEN_REQUESTS = 1  # seconds between requests
MAX_RETRIES = 5

PROMPT = """Extract all text from this document page exactly as it appears.
Preserve table structure using | as column separators.
Keep numbers, formatting, and Indonesian text accurate.
Output only the extracted text, no commentary."""

def extract_page(model, image_path: Path) -> str:
    image = Image.open(image_path)
    for attempt in range(MAX_RETRIES):
        try:
            response = model.generate_content([PROMPT, image])
            return response.text
        except Exception as e:
            if "429" in str(e) and attempt < MAX_RETRIES - 1:
                wait = 60 * (attempt + 1)
                print(f"rate limited, waiting {wait}s...", end=" ", flush=True)
                time.sleep(wait)
            else:
                raise

def main():
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    pages = sorted(PAGES_DIR.glob("*.png"))
    print(f"Found {len(pages)} pages")

    results = {}
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            results = json.load(f)
        good = sum(1 for v in results.values() if not v.startswith("ERROR"))
        print(f"Resuming — {good} pages already extracted successfully")

    for page_path in pages:
        page_name = page_path.stem
        if page_name in results and not results[page_name].startswith("ERROR"):
            print(f"  Skipping {page_name} (already done)")
            continue

        print(f"  Extracting {page_name}...", end=" ", flush=True)
        try:
            text = extract_page(model, page_path)
            results[page_name] = text
            print("OK")
        except Exception as e:
            print(f"ERROR: {e}")
            results[page_name] = f"ERROR: {e}"

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        time.sleep(DELAY_BETWEEN_REQUESTS)

    good = sum(1 for v in results.values() if not v.startswith("ERROR"))
    print(f"\nDone. {good}/{len(pages)} pages extracted. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
