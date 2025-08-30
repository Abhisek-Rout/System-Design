from payment_processor import PaymentProcessor
from credit_card import CreditCard
from upi import Upi

class Main:
    def main(self):
        self.processor: PaymentProcessor = PaymentProcessor()
        self.credit_card: CreditCard = CreditCard()
        self.upi: Upi = Upi()

        self.processor.process_payment(self.credit_card, 100)
        self.processor.process_payment(self.upi, 200)

if __name__ == "__main__":
    main_obj: Main = Main()
    main_obj.main()