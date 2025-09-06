"""
Concrete decorator class that adds Milk to a Coffee object, modifying its description and cost accordingly.
"""
from coffee_decorator import CoffeeDecorator

class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_description(self):
        return f"{super().get_description()}, Milk"
    
    def get_cost(self):
        return super().get_cost() + 0.50