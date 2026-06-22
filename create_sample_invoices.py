from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
INVOICE_DIR = ROOT / "sample_invoices"

INVOICES = [
    ("INV-1001", "Maple Office Supplies", "2026-06-10", "2026-07-10", "PO-88421", 842.50, 109.53, 952.03),
    ("INV-1002", "Northstar IT Services", "2026-06-12", "2026-07-12", "PO-88444", 1250.00, 162.50, 1412.50),
    ("INV-1003", "Learning Labs Canada", "2026-06-14", "2026-07-14", "PO-88472", 675.25, 87.78, 763.03),
    ("INV-1004", "Cedar Cloud Hosting", "2026-06-16", "2026-07-16", "PO-88501", 2100.00, 273.00, 2373.00),
]


def draw_invoice(path, row):
    invoice_no, vendor, date, due_date, po_number, subtotal, tax, total = row
    c = canvas.Canvas(str(path), pagesize=letter)
    width, height = letter
    y = height - 72

    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, y, "INVOICE")
    y -= 40

    c.setFont("Helvetica", 10)
    fields = [
        ("Invoice Number", invoice_no),
        ("Vendor", vendor),
        ("Invoice Date", date),
        ("Due Date", due_date),
        ("PO Number", po_number),
    ]
    for label, value in fields:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(72, y, f"{label}:")
        c.setFont("Helvetica", 10)
        c.drawString(190, y, value)
        y -= 20

    y -= 24
    c.setFont("Helvetica-Bold", 11)
    c.drawString(72, y, "Description")
    c.drawString(410, y, "Amount")
    y -= 18
    c.line(72, y, width - 72, y)
    y -= 24
    c.setFont("Helvetica", 10)
    c.drawString(72, y, "Services / supplies as per purchase order")
    c.drawRightString(470, y, f"${subtotal:,.2f}")
    y -= 36

    for label, value in [("Subtotal", subtotal), ("HST", tax), ("Total", total)]:
        c.setFont("Helvetica-Bold" if label == "Total" else "Helvetica", 10)
        c.drawString(340, y, f"{label}:")
        c.drawRightString(470, y, f"${value:,.2f}")
        y -= 20

    y -= 24
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(72, y, "Synthetic invoice created for an RPA portfolio demonstration.")
    c.save()


def main():
    INVOICE_DIR.mkdir(parents=True, exist_ok=True)
    for row in INVOICES:
        draw_invoice(INVOICE_DIR / f"{row[0]}.pdf", row)
    print(f"Created {len(INVOICES)} invoices in {INVOICE_DIR}")


if __name__ == "__main__":
    main()
