"""
This file defines the Meal class, representing a meal's components and providing a method to print the summary.
"""

class Meal:
    def __init__(self, builder):
        self.main_dish = builder.main_dish
        self.side_dish = builder.side_dish
        self.drink = builder.drink
        self.dessert = builder.dessert
        self.appetizer = builder.appetizer

    @staticmethod
    def get_instance(builder):
        return Meal(builder)

    def print_meal_summary(self):
        print(f"""
              Main Dish: {self.main_dish}
              Side Dish: {self.side_dish}
              Drink: {self.drink}
              Dessert: {self.dessert}
              Appetizer: {self.appetizer}
              """)