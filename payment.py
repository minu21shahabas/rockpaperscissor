from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_receipt(output_filename, transaction_details):
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1 * inch, height - 1 * inch, "Payment Receipt")
    
    c.setFont("Helvetica", 12)
    y_position = height - 1.5 * inch
    for key, value in transaction_details.items():
        c.drawString(1 * inch, y_position, f"{key}: {value}")
        y_position -= 0.3 * inch
    
    c.drawString(1 * inch, 0.5 * inch, "Thank you for your purchase!")
    
    c.showPage()
    c.save()

transaction_details = {
    "Date": "2024-06-20",
    "Transaction ID": "123456789",
    "Customer Name": "John Doe",
    "Amount": "$100.00",
    "Payment Method": "Credit Card"
}

create_receipt("payment_receipt.pdf", transaction_details)
