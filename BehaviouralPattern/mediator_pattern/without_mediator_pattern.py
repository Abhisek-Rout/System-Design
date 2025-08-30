class User:
    def __init__(self, name: str):
        self.__name: str = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value

    def send_message(self, msg: str, recipient: "User"):
        print(f"{self.name} sending msg to {recipient.name}")


class WithoutMediatorPattern:
    def main(self):
        rahul: User = User("Rahul")
        amit: User = User("Amit")
        neha: User = User("Neha")

        rahul.send_message("Hello", amit)
        rahul.send_message("Hello", neha)

if __name__ == "__main__":
    obj: WithoutMediatorPattern =   WithoutMediatorPattern()
    obj.main()