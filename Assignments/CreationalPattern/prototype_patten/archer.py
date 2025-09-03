"""
This class represents a Archer character in the Prototype Design Pattern.
"""
from character import Character

class Archer(Character):
    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        self.__defense = defense

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value: int):
        self.__health = value

    @property
    def attack_power(self):
        return self.__attack_power
    
    @attack_power.setter
    def attack_power(self, value: int):
        self.__attack_power = value
    
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self, value: int):
        self.__defense = value

    def clone(self):
        return Archer(self.name, self.health, self.attack_power, self.defense)
    
    def __str__(self):
        return (
            f"""
            Archer - Name: {self.name},
            Health: {self.health},
            Attack Power: {self.attack_power},
            Defense: {self.defense}
            """
        )