# Association represents a relationship between two or more classes.
# In this case, each object in one class is associated with one or more objects of another class

class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
class Teacher:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def teach(self, student: Student):
        print(f"{self.name} is teaching {student.name}")
    
class AssociationExample:
    def main(self):
        teacher: Teacher = Teacher('Miss Neha')
        student: Student = Student('Govind')

        teacher.teach(student)

if __name__ == "__main__":
    association_example: AssociationExample = AssociationExample()
    association_example.main()