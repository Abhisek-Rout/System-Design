from payment_method import PaymentMethod

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount: float):
        payment_method.pay(amount)