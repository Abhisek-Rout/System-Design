"""
Abstract class for decorating Coffee objects, allowing additional features to be added while preserving core functionality.
"""
from coffee import Coffee

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.decorated_coffee: Coffee = coffee

    def get_description(self):
        # Work delegation
        return self.decorated_coffee.get_description()
    
    def get_cost(self):
        # Work delegation
        return self.decorated_coffee.get_cost()