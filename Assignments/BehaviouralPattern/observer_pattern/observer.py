"""
The Subject interface defines methods for registering, removing, and notifying observers about stock price changes.
"""

from abc import ABC, abstractmethod

class Observer:
    def update(stock_symbol: str, new_price: float):
        pass