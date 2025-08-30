# Aggregation is a weak "has-a" relationship where once class contains objects of another class.
# However, the contained objects can exists independently of the container object
# This is a weak form of association
from typing import List

class Professor:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return self.__name
    
    
class Department:
    
    def __init__(self, name: str, professors: List[Professor]):
        self.__name = name
        self.__professors = professors

    @property
    def name(self):
        return self.__name
    
    @property
    def professors(self):
        return self.__professors
    
    def show_professors(self):
        print(f"Department: {self.name}")
        for professor in self.professors:
            print(f"{professor}")


class AggregationExample:
    def main(self):
        professor1: Professor = Professor("Mr. Anjan")
        professor2: Professor = Professor("Mr. Arnav")

        professors: List[Professor] = [professor1, professor2]

        # Here u can see professors an exist independent of Department
        department: Department = Department("Mathematics", professors)

        department.show_professors()

if __name__ == "__main__":
    agg_example: AggregationExample = AggregationExample()
    agg_example.main()
