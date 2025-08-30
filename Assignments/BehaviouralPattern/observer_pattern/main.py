"""
The Exercise class simulates stock price updates, registers investors, and removes an observer after the 4th update.
"""
from stock_market import StockMarket
from investorA import InverstorA
from investorB import InverstorB

class Exercise:
    def main(self):
        price_change_threshold: float = float(input("Enter the price change threshold: "))

        # Initialisation of stock market
        stock_market: StockMarket = StockMarket(price_change_threshold)

        # Initialisation of investors
        investor_A: InverstorA = InverstorA()
        investor_B: InverstorB = InverstorB()

        # Register Investor A and Inverstor B as an observer to receive stock updates.
        stock_market.register_observer(investor_A)
        stock_market.register_observer(investor_B)

        updates: int = int(input("Enter the updates u want to perform: "))

        for i in range(updates):
            if i == 5:
                # Remove Investor B from receiving notifications after the 4th update.
                stock_market.remove_observer(investor_B)

            stock_symbol: str = input("Enter the new stock symbol: ")
            new_price: float = float(input("Enter the new price: "))
            old_price: float = float(input("Enter the old price: "))

            # Update the stock price
            stock_market.set_stock_price(stock_symbol=stock_symbol, new_price=new_price, old_price=old_price)


if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()
