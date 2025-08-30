# Inheritance defines an "is-a" relationship where a subclass inherits properties and behaviours (methods)
# from a superclass

class Animal:
    def eat(self):
        print(f"This animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class InheritanceExample:
    def main(self):
        dog: Dog = Dog()
        dog.bark()
        dog.eat()

if __name__ == "__main__":
    inherit_example: InheritanceExample = InheritanceExample()
    inherit_example.main()