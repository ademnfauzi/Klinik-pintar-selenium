from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(40, 10, 'Hello World!')
pdf.output("hello_world.pdf")