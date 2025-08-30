from payment_method import PaymentMethod

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Making payment via Credit Card {amount}")