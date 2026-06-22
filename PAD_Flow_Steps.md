# Power Automate Desktop Flow Steps

Flow name: `Automated Invoice Data Entry`

1. Set invoice folder path.
2. Get all PDF files in the folder.
3. Launch Excel and open the tracker workbook.
4. Loop through each invoice file.
5. Extract text from PDF using PDF text extraction or OCR.
6. Parse invoice number, vendor, dates, PO number, subtotal, tax, and total.
7. Validate required fields.
8. Validate that subtotal + tax equals total.
9. Write each invoice row into Excel.
10. Mark status as `Ready for Entry` or `Needs Review`.
11. Save and close Excel.

## RPA Concepts Demonstrated

- Folder monitoring
- PDF text extraction
- Pattern matching
- Excel data entry
- Data validation
- Exception handling
- Human-in-the-loop review
