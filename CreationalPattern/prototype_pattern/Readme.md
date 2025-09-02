# Prototype pattern
Consider a board game where you need to sage the current state of the game at various checkpoints. Instead of manually creating new board objects and copying all the pieces or their states (which could be costly if the board is large and has many game pieces), we can use the Prototype Pattern to clone the board.

We will use the prototype pattern allows us to make a copy of the current board, including all its pieces and their states, wihtout the need for deeply recreating each part of the board.

## Solution
1. The *Prototype Patter* can be extremely useful in a board game when you want to save the current state of the game (including the board layout and the position of pieces) for undo/redo functionaity, checkpoints or simply making a copy of the board for a new player.
2. Each piece or game element can provide its clone method, allowing the entire board to be easily cloned with all its current state.

By using the Prototype pattern, we decouple the complexity of cloning the board from the client, ensuring that each object knows how to clone itself, making the system flexible and easier to maintain.

1. Shallow copy: Creates a new object but *does not clone the objects* that the original object referes to.
2. Deep copy: Clones the original object and all the objects it referes to (nested objects)

## Examples:
1. Shallow copy: Coning an object with references to other objects (only the outer object is copied)
2. Deep copy: Cloning the entire object graph, including any objects the original refers to.

## Benefits of Prototype pattern:
1. *Simplifies Object Creation*: Instead of manually copying each object, the clone method in each object simplifies the creation of copies.
2. *Avoids Subclassing*: The pattern relies on delegation to the clone method, allowing the class itself to handle object creation, avoiding the need for subclassing.
3. *Shallow or Deep Copy*: Depending on the use case, you can either implement a shallow copy (copying references) or a deep copy (cloning objects) based on the specific requirements.
4. *Efficient Creation*: When creating objects with complex structure or when performance is a concern, the Prototype pattern allows you to efficiently replicate objects.
5. *Consistency*: Ensures that all properties of the object are consistently copied, avoiding errors associated with manual copying.