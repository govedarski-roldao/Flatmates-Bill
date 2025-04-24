import webbrowser
from fpdf import FPDF


class PdfReport:
    """
    Calculates the amount that each flatmate should pay for the month
    """

    def __init__(self, filename):
        self.filename = filename + ".pdf"

    def generate(self, flatmate1, flatmate2, bill):
        border = 0
        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate1))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add icon
        pdf.image("./files/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=border, align="C", ln=1)

        # Insert Period
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=border)
        pdf.cell(w=150, h=40, txt=bill.period, border=border, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=border)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=border, ln=1)

        # Insert second and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=border)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=border, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)
