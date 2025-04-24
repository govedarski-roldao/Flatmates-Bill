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
