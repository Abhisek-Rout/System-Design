"""
The InvestorB class implements the Observer interface and receives stock price updates.
"""

from observer import Observer

class InverstorB(Observer):
    def update(self, stock_symbol: str, new_price: float):
        print(f"Investor B notified: Stock {stock_symbol} has a new price: {new_price}")