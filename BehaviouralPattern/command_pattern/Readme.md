# Command Pattern
Imagin you're developing a basic text editor with buttons for bold, italic and underline text formatting.

Without the Command Pattern, the buttons directly interact with the TextEditor class, and you end up hardcoding behaviour into the UI classes, making them tightly coupled.

## Resolution 
By introducing the Command Pattern, we can decouple the actions (bold, italic, underline) from the UI components (buttons), making the design more flexible and maintainabe. The buttons no longer need to know about the editor directly but instead work with generic Command objects.


## Structure
1. Command: Interface for executing operations.
2. Invoker: Sends the command.
3. Receiver: Performs the operation.


# Command Pattern Benefits
1. Decoupling of Invoker and Receiver: The button (invoker) doesn't know the details of the TextEditor (receiver), making the system more flexible and reusable.
2. Command History and Undo: Commands can be logged for undo/redo functionality.
3. Task Queuing: Commands can be stored in a queue and executed later, making it useful for task scheduling.
4. Extensibility: New commands can be added easily without modifying existing code. For example, adding a ChangeColorCommand only requires creating a new command class. (Open-close principle is followed here)


## Use Cases
1. GUI Applicatons:
    Commands can be associated with buttons, menus andd keyboard shortcuts in applications like text editors, spreadsheets or drawing software.

2. Task Scheduling:
    Commands can be placed in a queue and executed later, useful in batch processing or deferred task execution.

3. Undo/Redo Functionality:
    Commands can be stored and rolled back to provide undo and redo capabilities, especially in application like IDEs, word processors, or graphics softwarre.

4. Macro Recording:
    Actions performed by the user can be recorded as a series of commands which can then be played back as macros.