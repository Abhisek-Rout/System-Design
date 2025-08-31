# Creational Pattern
1. *Purpose*: Creational patterns are focused on *object creation mechanisms*, aiming to optimize the creation process while ensuring flexibility.

2. *Goal*: They abstract the instantiation process to make systems *more flexible and resusable*.

3. *Problem they solve*: Prevent tight coupling between code and object creation logic, simplifying the management of new object creation, especially in complex systems.

E.g: In a system where different types of documents (PDF, Word, Excel) are created, instead of using new everywhere, a Factory pattern can centralize the object creation.

4. *Application*: They are applied in scenarios where:
    a. You want to *separate the instantiation* process from usage.
    b. The exact type of object needed can vary depending on runtime conditions.

## Various types of creational pattern
1. Singleton Pattern
2. Builder Pattern
3. Prototype Pattern
4. Factory Pattern
5. Abstract Factory Pattern