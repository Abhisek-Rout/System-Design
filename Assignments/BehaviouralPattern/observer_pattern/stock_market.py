"""
The StockMarket class tracks stock price changes and notifies observers if the change exceeds a threshold.
"""
from typing import List

from subject import Subject
from observer import Observer

class StockMarket(Subject):
    def __init__(self, price_change_threshold: float):
        # Initialize the list of observers to keep track of registered observers.
        self.__observers: List[Observer] = list()
        self.__price_change_threshold: float = price_change_threshold


    def register_observer(self, observer: Observer):
        # Add observer to the list of observers
        self.__observers.append(observer)

    
    def remove_observer(self, observer: Observer):
        # Remove observer from the list of observers
        self.__observers.remove(observer)

    
    def notify_observers(self, stock_symbol: str, new_price: float):
        # Inform each observer about the updated stock price.
        for observer in self.__observers:
            observer.update(stock_symbol=stock_symbol, new_price=new_price)

    
    def set_stock_price(self, stock_symbol: str, new_price: float, old_price: float):
        price_change = ((new_price - old_price)/old_price)*100
        if price_change >= self.__price_change_threshold:
            # Notify observers if the price change exceeds the threshold
            self.notify_observers(stock_symbol=stock_symbol, new_price=new_price)