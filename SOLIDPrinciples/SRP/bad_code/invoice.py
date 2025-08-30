class Invoice:
    def __init__(self, amount):
        self.__amount: float = amount

    @property
    def amount(self):
        return self.__amount

    def generated_invoice(self):
        print(f"Invoice generated & printed for amount {self.amount}")

    def save_to_database(self):
        print(f"Saving to Database")

    def send_email_notification(self):
        print(f"Sending email notification for invoice")