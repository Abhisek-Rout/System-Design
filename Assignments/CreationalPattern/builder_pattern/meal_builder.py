"""
This file constructs a Meal object by setting mandatory components (main dish, side dish, drink) and optional components (dessert, appetizer) using the Builder design pattern.
"""
from meal import Meal

class MealBuilder:
    def __init__(self, main_dish, side_dish, drink):
        self.main_dish = main_dish
        self.side_dish = side_dish
        self.drink = drink
        self.dessert = "Default Dessert"
        self.appetizer = "Default Appetizer"

    def set_dessert(self, dessert: str):
        self.dessert = dessert
        return self

    def set_appetizer(self, appetizer: str):
        self.appetizer = appetizer
        return self
    
    def build(self):
        return Meal.get_instance(self)
