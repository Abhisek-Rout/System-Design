"""
This file gathers meal components from user input and constructs full and simple meals using the Builder design pattern.
"""
from meal_builder import MealBuilder

class Exercise:
    def main(self):
        main_dish = input("Enter the main dish: ")
        side_dish = input("Enter the side dish: ")
        drink = input("Enter the drink: ")
        dessert = input("Enter the dessert: ")
        appetizer = input("Enter the appetizer: ")

        meal = (
                MealBuilder(
                    main_dish=main_dish,
                    side_dish=side_dish,
                    drink=drink
                )
                .set_appetizer(appetizer)
                .set_dessert(dessert)
                .build()
        )

        print("Full meal summary: ")
        meal.print_meal_summary()

        main_dish = input("Enter the main dish: ")
        side_dish = input("Enter the side dish: ")
        drink = input("Enter the drink: ")

        meal = (
                MealBuilder(
                    main_dish=main_dish,
                    side_dish=side_dish,
                    drink=drink
                )
                .build()
        )

        print("Simple meal summary: ")
        meal.print_meal_summary()

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()