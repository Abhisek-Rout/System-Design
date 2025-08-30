"""
The InvestorA class implements the Observer interface and receives stock price updates.
"""

from observer import Observer

class InverstorA(Observer):
    def update(self, stock_symbol: str, new_price: float):
        print(f"Investor A notified: Stock {stock_symbol} has a new price: {new_price}")