# Composition is a strong "has-a" relationship where one class owns objects of another class.
# If the container object is destroyed, the contained objects are destroyed as well
# It is an example of strong association
from typing import List

class Room:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return self.name
    
class House:
    def __init__(self):
        # Here u can see the rooms cannot exist independent of House
        self.__rooms: List[Room] = list()
        self.rooms.append(Room("Living Room"))
        self.rooms.append(Room("Bed Room"))
        self.rooms.append(Room("Drawing Room"))

    @property
    def rooms(self):
        return self.__rooms

    def add_room(self, room: Room):
        self.rooms.append(room)

    def show_rooms(self):
        for room in self.rooms:
            print(f"{room}")


class CompositionExample:
    def main(self):
        house: House = House()

        house.show_rooms()

if __name__ == "__main__":
    comp_example: CompositionExample = CompositionExample()
    comp_example.main()