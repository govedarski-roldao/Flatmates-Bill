from fpdf import FPDF


class Bill:
    """
    Object that contains data about the bill such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the apartment and pays a share of the bill.
    """

    def __init__(self, name, days_in_the_house):
        self.name = name
        self.days = days_in_the_house

    def pays(self, bill, flatmate2):
        weight = self.days / (self.days + flatmate2.days)
        to_pay = bill.amount * weight
        return round(to_pay, 2)


class PdfReport:
    """
    Calculates the amount that each flatmate should pay for the month
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        border = 0
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=border, align="C", ln=1)

        # Insert Period
        pdf.cell(w=100, h=40, txt="Period:", border=border)
        pdf.cell(w=150, h=40, txt=bill.period, border=border, ln=1)
        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=border)
        pdf.cell(w=150, h=40, txt=str(john.pays(the_bill, mary)), border=border, ln=1)
        # Insert second and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=border)
        pdf.cell(w=150, h=40, txt=str(mary.pays(the_bill, john)), border=border, ln=1)

        pdf.output(self.filename + ".pdf")


the_bill = Bill(120, "April 2021")

john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)

print("John pays", john.pays(the_bill, mary))
print("Mary pays", mary.pays(the_bill, john))

generate = PdfReport("bills")
generate.generate(john, mary, the_bill)
