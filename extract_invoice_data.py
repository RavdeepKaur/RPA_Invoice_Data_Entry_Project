import csv
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
INVOICE_DIR = ROOT / "sample_invoices"
OUTPUT_CSV = ROOT / "extracted_invoice_data.csv"

PATTERNS = {
    "invoice_no": r"Invoice Number:\s*(INV-\d+)",
    "vendor": r"Vendor:\s*(.+)",
    "invoice_date": r"Invoice Date:\s*(\d{4}-\d{2}-\d{2})",
    "due_date": r"Due Date:\s*(\d{4}-\d{2}-\d{2})",
    "po_number": r"PO Number:\s*(PO-\d+)",
    "subtotal": r"Subtotal:\s*\$([\d,]+\.\d{2})",
    "tax": r"HST:\s*\$([\d,]+\.\d{2})",
    "total": r"Total:\s*\$([\d,]+\.\d{2})",
}


def read_pdf(path):
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def money(value):
    return float(value.replace(",", ""))


def extract(path):
    text = read_pdf(path)
    row = {"source_file": path.name}
    errors = []
    for field, pattern in PATTERNS.items():
        match = re.search(pattern, text, flags=re.MULTILINE)
        if not match:
            row[field] = ""
            errors.append(field)
            continue
        value = match.group(1).strip()
        row[field] = money(value) if field in {"subtotal", "tax", "total"} else value

    expected = round(float(row.get("subtotal") or 0) + float(row.get("tax") or 0), 2)
    actual = round(float(row.get("total") or 0), 2)
    if expected != actual:
        errors.append("total_validation")

    row["validation_status"] = "Needs Review" if errors else "Ready for Entry"
    row["validation_notes"] = ", ".join(errors) if errors else "All required fields extracted and total validated"
    return row


def main():
    rows = [extract(path) for path in sorted(INVOICE_DIR.glob("*.pdf"))]
    fields = [
        "source_file", "invoice_no", "vendor", "invoice_date", "due_date", "po_number",
        "subtotal", "tax", "total", "validation_status", "validation_notes",
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Extracted {len(rows)} invoices to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
