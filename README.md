# Automated Invoice Data Entry RPA Project

This portfolio project demonstrates an RPA-style workflow for invoice processing. It reads invoice PDFs, extracts key invoice fields, validates totals, writes clean records into Excel, and flags exceptions for human review.

## Business Problem

Accounts payable teams often receive invoices as PDFs and manually copy invoice details into spreadsheets, ERP screens, or finance forms. This is repetitive, rules-based work where automation can reduce manual effort and improve consistency.

## What The Automation Does

1. Creates sample invoice PDFs.
2. Extracts invoice number, vendor, dates, PO number, subtotal, tax, and total.
3. Validates required fields.
4. Validates that `subtotal + tax = total`.
5. Writes results into an Excel tracker.
6. Marks each invoice as `Ready for Entry` or `Needs Review`.

## Tools Used

- Python
- ReportLab for sample PDF generation
- PyPDF for PDF text extraction
- OpenPyXL for Excel output
- Power Automate Desktop flow design documented in `PAD_Flow_Steps.md`

## Project Files

- `create_sample_invoices.py` - Generates synthetic invoice PDFs.
- `extract_invoice_data.py` - Extracts and validates invoice data.
- `build_invoice_tracker.py` - Builds the Excel tracker.
- `run_project.ps1` - Runs the full workflow from PowerShell.
- `PAD_Flow_Steps.md` - Explains how the same workflow maps to Power Automate Desktop.
- `Interview_Talking_Points.md` - Interview explanation for RPA-related roles.
- `Invoice_Data_Entry_Tracker.xlsx` - Final Excel output.

## How To Run

Open PowerShell in this folder and run:

```powershell
.\run_project.ps1
```

Or run each step manually:

```powershell
python create_sample_invoices.py
python extract_invoice_data.py
python build_invoice_tracker.py
```

Then open:

```text
Invoice_Data_Entry_Tracker.xlsx
```

## RPA Concepts Demonstrated

- Process analysis
- PDF data extraction
- Pattern matching
- Data validation
- Exception handling
- Excel data entry
- Human-in-the-loop review
- Documentation for maintainability


