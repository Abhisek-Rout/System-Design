from abc import ABC, abstractmethod

class Pizza(ABC):
    def get_description(self):
        pass

    def get_cost(self):
        pass


class BasicPizza(Pizza):
    def get_description(self) -> str:
        return "Basic Pizza"
    
    def get_cost(self) -> float:
        return 15.0
    

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.decorated_pizza = pizza

    def get_description(self) -> str:
        return self.decorated_pizza.get_description()
    
    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost()
    
# Concrete Decorator class will inherit PizzaDecorator
class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return f"{super().get_description()}, Cheese"
    
    def get_cost(self):
        return super().get_cost() + 5
    

class OliveDecorator(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return f"{super().get_description()}, Olive"
    
    def get_cost(self):
        return super().get_cost() + 3
    
class MushroomDecorator(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return f"{super().get_description()}, Mushroom"
    
    def get_cost(self):
        return super().get_cost() + 8


class WithDecoratorPattern:
    def main(self):
        pizza: Pizza = BasicPizza()
        print(pizza.get_description())
        print(pizza.get_cost())

        pizza: Pizza = OliveDecorator(pizza)
        print(pizza.get_description())
        print(pizza.get_cost())

        pizza: Pizza = MushroomDecorator(pizza)
        print(pizza.get_description())
        print(pizza.get_cost())

        pizza: Pizza = CheeseDecorator(pizza)
        print(pizza.get_description())
        print(pizza.get_cost())

if __name__ == "__main__":
    obj: WithDecoratorPattern = WithDecoratorPattern()
    obj.main()
