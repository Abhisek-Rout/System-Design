from payment_gateway import PaymentGateway
from typing import Dict

class PaymentService:
    def __init__(self):
        self.payment_methods: Dict[str, PaymentGateway] = {}

    def add_payment_method(self, name: str, pm: PaymentGateway) -> None:
        self.payment_methods[name] = pm

    def make_payment(self, name: str) -> None:
        pm = self.payment_methods.get(name)
        if pm:
            pm.pay()  # Runtime Polymorphism
        else:
            print(f"No payment method found with name: {name}")