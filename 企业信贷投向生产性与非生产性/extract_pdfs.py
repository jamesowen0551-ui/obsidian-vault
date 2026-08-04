import sys
from pathlib import Path
from pypdf import PdfReader

papers_dir = Path("papers")
extract_dir = Path("papers_extracted")
extract_dir.mkdir(exist_ok=True)

pdfs = [
    ("Werner_1997_Quantity_Theorem_Disaggregated_Credit.pdf", "werner_1997"),
    ("BIS_WP381_Cecchetti_Kharroubi_2012.pdf", "bis_wp381"),
    ("BIS_WP490_Cecchetti_Kharroubi_2015.pdf", "bis_wp490"),
    ("King_Levine_1993_Finance_Growth_Schumpeter.pdf", "king_levine_1993"),
    ("Rajan_Zingales_1998_Financial_Dependence_Growth.pdf", "rajan_zingales_1998"),
]

for pdf_name, out_name in pdfs:
    pdf_path = papers_dir / pdf_name
    if not pdf_path.exists():
        print(f"SKIP: {pdf_name} not found")
        continue
    try:
        reader = PdfReader(str(pdf_path))
        total_pages = len(reader.pages)
        # Extract first ~15 pages and last 5 pages for references
        pages_to_extract = min(15, total_pages)
        text_parts = []
        for i in range(pages_to_extract):
            try:
                page_text = reader.pages[i].extract_text()
                if page_text:
                    text_parts.append(f"\n--- Page {i+1} ---\n{page_text}")
            except Exception as e:
                text_parts.append(f"\n--- Page {i+1} [ERROR: {e}] ---\n")
        
        # Also extract references section (last few pages)
        if total_pages > 15:
            for i in range(max(15, total_pages - 5), total_pages):
                try:
                    page_text = reader.pages[i].extract_text()
                    if page_text:
                        text_parts.append(f"\n--- Page {i+1} ---\n{page_text}")
                except Exception:
                    pass
        
        full_text = "\n".join(text_parts)
        out_path = extract_dir / f"{out_name}.txt"
        out_path.write_text(full_text, encoding="utf-8")
        print(f"OK: {pdf_name} -> {out_name}.txt ({total_pages} pages)")
    except Exception as e:
        print(f"ERROR: {pdf_name}: {e}")
