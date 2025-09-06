"""
The Exercise class facilitates user interaction to create a customized coffee by allowing the selection of various ingredients and then outputs the final coffee description and total cost.
"""
from coffee import Coffee
from basic_coffee import BasicCoffee
from milk import Milk
from sugar import Sugar
from whipped_cream import WhippedCream

class Exercise:
    def main(self):
        coffee: Coffee = BasicCoffee()
        add_more_ingredients: bool = True
        user_input_manual = """
        1: Add Milk
        2: Add Sugar
        3: Add WhippedCream
        4: No more ingredients to add
        """
        print(user_input_manual)

        while add_more_ingredients:
            choices: str = input("Enter your choices: ")
            choice_list: list = choices.split()

            for choice in choice_list:
                match choice:
                    case "1":
                        coffee = Milk(coffee)
                    case "2":
                        coffee = Sugar(coffee)
                    case "3":
                        coffee = WhippedCream(coffee)
                    case "4":
                        add_more_ingredients = False
                        break
                    case _:
                        print(f"Invalid choice: {choice}")
                        break
            
            if not add_more_ingredients:
                break

        print(f"Final Coffee Description: {coffee.get_description()}")
        print(f"Total Cost: {coffee.get_cost()}")


if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()