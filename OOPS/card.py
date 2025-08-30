from payment_gateway import PaymentGateway

class Card(PaymentGateway):
    def __init__(self, card_number: str, card_name: str):
        self.__card_number = card_number
        self.__card_name = card_name

    @property
    def card_number(self):
        return self.__card_number
    
    @property
    def card_name(self):
        return self.__card_name
    