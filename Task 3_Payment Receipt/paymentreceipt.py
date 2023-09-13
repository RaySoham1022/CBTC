from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import uuid

def generate_receipts(data_list, pdf_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []
    # Define table data
    tdata = [["Transaction ID", "Customer Name",
                 "Transaction Type", "Amount", "Date"]]
    for data in data_list:
        tdata.append([data["tid"], data["cname"],
                          data["type"], f" {data['amount']:.2f}", data["date"]])

    # Create table and set style
    table = Table(tdata, colWidths=[120, 180, 120, 80, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.yellow),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"\nReceipt '{pdf_filename}' has been saved ")


def main():
    num_receipts = int(input("\nHow many Receipts you want to Generate : "))
    data_list = []

    for i in range(num_receipts):
        cname = input(f"\nReceipt {i+1} Customer Name : ")
        type = input(f"Receipt {i+1} Transaction Type : ")
        amount = float(input(f"Receipt {i+1} Amount: "))
        date = input(f"Receipt {i+1} Date of Transaction: ")

        # Generating a random 8-character transaction ID
        tid = str(uuid.uuid4())[:8]

        data_list.append({
            "tid": tid,
            "cname": cname,
            "type": type,
            "amount": amount,
            "date": date
        })

    print("\nReceipt will be saved as a PDF File")
    pdf_filename = input("Enter File Name for Receipt : ")
    pdf_filename = str(pdf_filename) + '.pdf' 
    generate_receipts(data_list, pdf_filename)

if __name__ == "__main__":
    main()
















# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# import uuid

# def generate_receipts(data_list, pdf_filename):
#     doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
#     elements = []
#     # Define table data
#     data = [["Transaction ID", "Customer Name",
#                  "Transaction Type", "Amount", "Date"]]
#     for data in data_list:
#         data.append([data["tid"], data["cname"],
#                           data["type"], f"₹ {data['amount']:.2f}", data["date"]])

#     # Create table and set style
#     table = Table(data, colWidths=[120, 180, 120, 80, 100])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.black),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.yellow),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     elements.append(table)
#     doc.build(elements)
#     print(f"Receipt'{pdf_filename}' has been saved ")


# def main():
#     num_receipts = int(input("How many Receipts you want to Generate : "))
#     data_list = []

#     for i in range(num_receipts):
#         cname = input(f"Receipt {i+1} Customer Name : ")
#         type = input(f"Receipt {i+1} Transaction Type : ")
#         amount = float(input(f"Receipt {i+1} Amount: "))
#         date = input(f"Receipt {i+1} Date of Transaction: ")

#         # Generating a random 8-character transaction ID
#         tid = str(uuid.uuid4())[:8]

#         data_list.append({
#             "tid": tid,
#             "cname": cname,
#             "type": type,
#             "amount": amount,
#             "date": date
#         })

#     print("\nReceipt will be saved as a PDF File")
#     pdf_filename = input("Enter File Name for Receipt : ")
#     generate_receipts(data_list, pdf_filename)

# if __name__ == "__main__":
#     main()
