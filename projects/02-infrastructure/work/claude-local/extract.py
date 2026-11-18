"""Extract text for local document analysis."""
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile

source = Path(sys.argv[1])
suffix = source.suffix.lower()

if suffix in {".md", ".txt", ".csv", ".tsv"}:
    text = source.read_text(encoding="utf-8-sig")
elif suffix == ".docx":
    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with ZipFile(source) as archive:
        document = ElementTree.fromstring(archive.read("word/document.xml"))
    text = "\n".join(
        "".join(element.text or "" for element in paragraph.iter(namespace + "t"))
        for paragraph in document.iter(namespace + "p")
    )
elif suffix == ".pdf":
    text = subprocess.check_output(["pdftotext", "-enc", "UTF-8", str(source), "-"], text=True)
else:
    raise SystemExit(f"Unsupported document format: {suffix}")

sys.stdout.write(text)
