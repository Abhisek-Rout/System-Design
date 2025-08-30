from card import Card

class DebitCard(Card):
    def __init__(self, card_number:str, card_name: str):
        super().__init__(card_number, card_name)

    def pay(self):
        print("Making paymeny via Debit Card.")