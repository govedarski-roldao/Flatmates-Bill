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

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Calculates the amount that each flatmate should pay for the month
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)
print(john.pays(the_bill))
