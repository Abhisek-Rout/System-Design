from payment_method import PaymentMethod

class Upi(PaymentMethod):
    def pay(self, amount):
        print(f"Making payment via UPI {amount}")