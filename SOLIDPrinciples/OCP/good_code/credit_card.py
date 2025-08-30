from payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Making Payment via Credit Card {amount}")
