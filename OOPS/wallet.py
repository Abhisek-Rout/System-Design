from payment_gateway import PaymentGateway

class Wallet(PaymentGateway):
    def __init__(self, wallet_id: str):
        self.__wallet_id = wallet_id

    def pay(self):
        print(f"Making payment via wallet", self.__wallet_id)