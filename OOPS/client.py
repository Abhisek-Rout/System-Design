from payment_service import PaymentService
from debit_card import DebitCard
from credit_card import CreditCard
from upi import Upi
from wallet import Wallet

class Client:
    def main(self):
        ps: PaymentService = PaymentService()
        ps.add_payment_method("AbhisekDebitCard", DebitCard("123", "Abhisek Rout"))
        ps.add_payment_method("AbhisekCreditCard", CreditCard("456", "Abhisek Rout"))
        ps.add_payment_method("AbhisekUPI", Upi("123@abhis"))
        ps.add_payment_method("AbhisekWallet", Wallet("123@paytmwallet"))

        ps.make_payment("AbhisekUPI")
        ps.make_payment("AbhisekDebitCard")
        ps.make_payment("AbhisekCreditCard")
        ps.make_payment("AbhisekWallet")

if __name__ == "__main__":
    client = Client()
    client.main()