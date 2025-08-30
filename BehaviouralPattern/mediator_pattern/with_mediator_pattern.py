from abc import ABC, abstractmethod
from typing import List


class ChatUser:
    def __init__(self, name: str, chat_mediator: "ChatMediator"):
        self.__name: str = name
        self.chat_mediator: ChatMediator = chat_mediator

    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self, value: str):
        self.__name = value

    def send_message(self, msg: str):
        print(f"{self.name} sending a message: {msg}")
        self.chat_mediator.send_message(msg, self)

    def receive_message(self, msg: str, sender: "ChatUser"):
        print(f"{self.name} received message: {msg} from {sender.name}")


class ChatMediator(ABC):
    def send_message(self, msg: str, user: ChatUser):
        pass

    def add_user(self, user: ChatUser):
        pass


class ChatRoom(ChatMediator):
    def __init__(self):
        self.__users: List[ChatUser] = list()

    def add_user(self, user: ChatUser):
        self.__users.append(user)

    def send_message(self, msg:str, sender: ChatUser):
        for user in self.__users:
            if user != sender:
                user.receive_message(msg, sender)



class WithMediatorPattern:
    def main(self):
        # Create a chat romm
        chat_room: ChatRoom = ChatRoom()

        # Create users
        rahul: ChatUser = ChatUser("Rahul", chat_room)
        amit: ChatUser = ChatUser("Amit", chat_room)
        neha: ChatUser = ChatUser("Neha", chat_room)

        # Add the users to the chat room
        chat_room.add_user(rahul)
        chat_room.add_user(amit)
        chat_room.add_user(neha)

        # Send messages to everyone
        amit.send_message("Hi Everyone!")

if __name__ == "__main__":
    obj: WithMediatorPattern =  WithMediatorPattern()
    obj.main()