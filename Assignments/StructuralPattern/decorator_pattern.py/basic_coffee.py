"""
This class represents implementation of the Coffee interface representing a basic coffee with a fixed description and cost.
"""
from coffee import Coffee

class BasicCoffee(Coffee):
    def get_description(self) -> str:
        return "Basic Coffee"
    
    def get_cost(self) -> str:
        return 3.0