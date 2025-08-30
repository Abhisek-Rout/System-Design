from payment_gateway import PaymentGateway

class Upi(PaymentGateway):
    def __init__(self, upi_id: str):
        self.__upi_id = upi_id

    def pay(self):
        print(f"Making payment via UPI ID", self.__upi_id)