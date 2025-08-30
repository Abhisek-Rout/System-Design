from card import Card

class CreditCard(Card):
    def __init__(self, card_number: str, card_name: str):
        super().__init__(card_number, card_name)

    def pay(self):
        print("Making payment via Credit card.")