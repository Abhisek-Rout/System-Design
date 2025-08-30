from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class PaymentService:
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self):
        # Polymorphic behaviour
        self.strategy.process_payment()


class CreditCard(PaymentStrategy):
    def process_payment(self):
        print(f"Making payment via Credit Card")


class DebitCard(PaymentStrategy):
    def process_payment(self):
        print(f"Making payment via Debit Card")


class StrategyPattern:
    def main(self):
        payment_service: PaymentService = PaymentService()

        # Debit card
        debit_card_payment: DebitCard = DebitCard()
        payment_service.set_payment_strategy(debit_card_payment)
        payment_service.pay()

        cedit_card_payment: CreditCard = CreditCard()
        payment_service.set_payment_strategy(cedit_card_payment)
        payment_service.pay()


if __name__ == "__main__":
    obj: StrategyPattern = StrategyPattern()
    obj.main()