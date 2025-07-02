from fpdf import FPDF, XPos, YPos
from datetime import datetime
import os

# === 1. USER INPUT ===
client_name = input("Enter client name: ")

items = []
while True:
    item_name = input("Enter item name (or press Enter to finish): ")
    if item_name == "":
        break
    qty = int(input(f"Enter quantity for '{item_name}': "))
    price = float(input(f"Enter price for '{item_name}': "))
    items.append({"name": item_name, "qty": qty, "price": price})

# === 2. CREATE PDF ===
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font("helvetica", style='B', size=16)
pdf.cell(200, 10, text="INVOICE", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.ln(10)

# Client Info
pdf.set_font("helvetica", size=12)
pdf.cell(100, 10, text=f"Client Name: {client_name}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(100, 10, text=f"Date: {datetime.today().strftime('%d-%m-%Y')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(10)

# Table Header
pdf.set_font("helvetica", style='B', size=12)
pdf.cell(80, 10, text="Item", border=1)
pdf.cell(30, 10, text="Qty", border=1)
pdf.cell(40, 10, text="Price", border=1)
pdf.cell(40, 10, text="Total", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Table Rows
pdf.set_font("helvetica", size=12)
total_amount = 0
for item in items:
    total = item['qty'] * item['price']
    total_amount += total
    pdf.cell(80, 10, text=item['name'], border=1)
    pdf.cell(30, 10, text=str(item['qty']), border=1)
    pdf.cell(40, 10, text=f"Rs. {item['price']:.2f}", border=1)
    pdf.cell(40, 10, text=f"Rs. {total:.2f}", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Final Total
pdf.set_font("helvetica", style='B', size=12)
pdf.cell(150, 10, text="Total Amount", border=1)
pdf.cell(40, 10, text=f"Rs. {total_amount:.2f}", border=1)

# === 3. AUTO-NAMING OUTPUT FILE ===
base_filename = f"Invoice_{client_name.replace(' ', '_')}"
filename = f"{base_filename}.pdf"
counter = 1

while os.path.exists(filename):
    filename = f"{base_filename}_{counter}.pdf"
    counter += 1

pdf.output(filename)
print(f"\n✅ Invoice generated successfully: {filename}")
