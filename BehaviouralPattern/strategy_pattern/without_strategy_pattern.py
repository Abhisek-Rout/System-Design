class PaymentService:
    def process_payment(self, payment_method):
        if payment_method == "CreditCard":
            print("Making payment via credit card")
        elif payment_method == "DebitCard":
            print("Making payment via debit card")
        else:
            print("Unsupported method")


class WithoutStrategyPattern:
    def main(self):
        payment_service = PaymentService()
        payment_service.process_payment("CreditCard")
        payment_service.process_payment("DebitCard")
        payment_service.process_payment("UPI")


if __name__ == "__main__":
    obj: WithoutStrategyPattern = WithoutStrategyPattern()
    obj.main()

        
        