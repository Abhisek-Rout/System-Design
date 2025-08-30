## Mediator Pattern
We want to build a chat system with multiple participants where each user can send messages to all other users. If users send messages to each other directly, the complexity inceases as more users are added. Each user must know about other user, creating a complex web of communication and dependencies.

## Solution using mediator pattern
1. Scenario: In a chat system, multiple participantscommunicate through a central *chat mediator* reducing the need for each participant to be aware of the others.

## Example:
1. *Mediator*: Chat server
2. *Colleagues*: Chat participants send messages to the mediator, which distributes them to others.

## How to implement the solution?
1. ChatMediator Interface: Declares the send_message method, which all mediators must implement.
2. Concrete Mediator: The ChatRoom class implements the ChatMediator interface. It holds a list of users and handles message broadcasting.
3. User Class: Each User object represents a participant in the chat. When a user sends a message, the send_message method in the ChatRoom mediator is called, which distributes the message to all users except the sender.
4. Communication: Users interact only with the ChatRoom (mediator), which facilitates communication between them, removing direct descrepancies between individual users.

## Benefits of Mediator Pattern
1. Reduces complexity: The mediator centralizes communication, reducing direct dependencies between objects.
2. Losse Coupling: Collegues only interact with the mediator, making them easier to manage, extend and maintain.
3. Single Responsibility: The mediator handles complex communication logic, allowing collegues to focus on their own behaviour.
4. Centralied Control: Changes to communication rules can be made in mediator without affecting the collegues.

## Use-cases of Mediator pattern in real world
1. Air Traffic Control:
    Airplanes communicate through a central tower (mediator) instead of coordinating directly with each other.

2. GUI Component Coordination:
    In GUI applications, multiple UI compoenents may need to interact. For example, when a dropdown changes it may trigger updates to text fields, buttons etc. A mediator can handle this interaction logic instead of having the components know about each other directly.

3. Workflow Systems:
    In a business process management system, a mediator can coordinate various activities across multiple systems or departments.