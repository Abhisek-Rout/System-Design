from payment_method import PaymentMethod

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Making payment via PayPal {amount}")
