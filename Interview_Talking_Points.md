# Interview Talking Points

## Project Overview

I built an invoice data-entry automation workflow that reads invoice PDFs, extracts invoice details, validates totals, and writes the results into an Excel tracker. The workflow also flags records that need human review.

## Why This Project Matters

Invoice processing is a good RPA use case because it is repetitive, rules-based, and depends on consistent data entry. Automating the first pass reduces manual copying, improves consistency, and helps staff focus on exceptions.

## Key Steps

1. Generate sample invoices for workflow testing.
2. Extract invoice text from PDF files.
3. Parse invoice number, vendor, dates, PO number, subtotal, tax, and total.
4. Validate required fields and invoice totals.
5. Write clean results into Excel.
6. Mark each invoice as `Ready for Entry` or `Needs Review`.

## Technologies Used

- Python
- ReportLab
- PyPDF
- OpenPyXL
- Power Automate Desktop flow design
- Excel

## Interview Answer

One project I can discuss is an invoice data-entry automation workflow. I designed the process so invoice PDFs are read from a folder, key fields are extracted, totals are validated, and the results are written into an Excel tracker. I also added exception handling so incomplete or incorrect invoices are marked for review instead of being treated as ready for entry. This helped me connect process mapping, validation logic, Excel automation, and human-in-the-loop review, which are all important in RPA work.
