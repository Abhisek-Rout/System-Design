"""
Concrete decorator class that adds Whipped Cream to a Coffee object, enhancing its description and adjusting its cost.
"""
from coffee_decorator import CoffeeDecorator

class WhippedCream(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_description(self):
        return f"{super().get_description()}, Whipped Cream"
    
    def get_cost(self):
        return super().get_cost() + 0.70
