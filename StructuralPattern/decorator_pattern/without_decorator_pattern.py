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
    
class CheesePizza(BasicPizza):
    def get_description(self) -> str:
        return f"{super().get_description()}, Cheese"
    
    def get_cost(self):
        return super().get_cost() + 5
    
class CheeseOlivePizza(CheesePizza):
    def get_description(self):
        return f"{super().get_description()}, Olive"
    
    def get_cost(self):
        return super().get_cost() + 3
    
class WithoutDecoratorPattern:
    def main(self):
        pizza: Pizza = CheeseOlivePizza()
        print(pizza.get_description())
        print(pizza.get_cost())


if __name__ == "__main__":
    obj: WithoutDecoratorPattern = WithoutDecoratorPattern()
    obj.main()