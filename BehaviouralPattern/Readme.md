# Meaning of Behavioural Pattern
In system design (and more specifically Design Patterns from the "Gang of Four" book),
Behavioral Patterns are a category of design patterns that focus on *how objects interact, communicate, and distribute responsibilities among themselves.*

They don’t emphasize structure (like class composition in Structural Patterns) or object creation (like Creational Patterns).
Instead, they define how objects behave and collaborate at runtime.

# Why is it called “Behavioral”?
1. These patterns capture and model the dynamic behavior of systems.
2. They describe how responsibilities are divided between objects.
3. They define how objects behave together, not just how they are connected.

# Examples of Behavioral Patterns
Some well-known behavioral design patterns:
1. Observer → Defines a one-to-many dependency between objects (publish/subscribe).
2. Strategy → Lets you choose an algorithm’s behavior at runtime.
3. Command → Encapsulates a request as an object.
4. Iterator → Provides a way to sequentially access elements of a collection.
5. Mediator → Defines how objects communicate via a central mediator (avoids direct coupling).
6. Chain of Responsibility → Passes a request along a chain until it’s handled.