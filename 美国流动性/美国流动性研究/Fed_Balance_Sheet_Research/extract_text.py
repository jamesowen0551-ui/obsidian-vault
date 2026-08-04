import sys, os, re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pypdf import PdfReader
from bs4 import BeautifulSoup

root = Path(__file__).parent
outdir = root / "_extracted"
outdir.mkdir(exist_ok=True)

for f in sorted(root.rglob("*")):
    if f.parent.name == "_extracted" or f.name.startswith("extract") :
        continue
    if f.suffix.lower() == ".pdf":
        try:
            r = PdfReader(str(f))
            pages = []
            for i, p in enumerate(r.pages):
                try:
                    pages.append(f"\n===== PAGE {i+1} =====\n" + (p.extract_text() or ""))
                except Exception as e:
                    pages.append(f"\n===== PAGE {i+1} [extract error: {e}] =====\n")
            txt = "".join(pages)
        except Exception as e:
            txt = f"[PDF open error: {e}]"
    elif f.suffix.lower() in (".html", ".htm"):
        soup = BeautifulSoup(f.read_text(encoding="utf-8", errors="ignore"), "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer"]):
            tag.decompose()
        txt = soup.get_text("\n")
        txt = re.sub(r"\n{3,}", "\n\n", txt)
    else:
        continue
    out = outdir / (f.stem + ".txt")
    out.write_text(txt, encoding="utf-8")
    print(f"{f.name}: {len(txt)} chars -> {out.name}")
