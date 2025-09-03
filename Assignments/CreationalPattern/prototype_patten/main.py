"""
This class demonstrates the use of the Prototype Design Pattern for cloning characters.
"""
from archer import Archer
from warrior import Warrior
from mage import Mage

class Exercise:
    def main(self):
        warrior_name: str = input("Enter warrior name: ")
        health: int = input("Enter warrior health: ")
        attack_power: int = input("Enter warrior attack power: ")
        defense: int = input("Enter warrior defense: ")

        warrior: Warrior = Warrior(warrior_name, health, attack_power, defense)

        # Clone the original warrior character to create a new instance.
        cloned_warrior: Warrior = warrior.clone()

        health: int = input("Enter warrior health: ")
        cloned_warrior.health = health

        attack_power: int = input("Enter warrior attack power: ")
        cloned_warrior.attack_power = attack_power

        defense: int = input("Enter warrior defense: ")
        cloned_warrior.defense = defense

        print("Original Character: ")
        print(warrior)

        print("Cloned Character: ")
        print(cloned_warrior)

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()