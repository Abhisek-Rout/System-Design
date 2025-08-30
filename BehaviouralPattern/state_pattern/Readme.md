# State Pattern
You are tasked with building a DirectionService class for a navigation app. This class calcualtes the estimated time of arrival (ETA) and provides directions between two points. The ETA and direction differ based on the mode of transportation, which can be one of the following:

1. Walking
2. Cycling
3. Car
4. Train

## Problems with our Code
1. Tight coupling and complex conditional logic:
    a. The DirectionService likely uses *conditional statements* (if-else or switch-case) based on transportation mode enums to determine how to calculate ETA and provide directions.
    b. As the number of transportation modes increases, the conditional logic becomes more complex and harder to maintain.

2. Violation of the Open/Close Principle:
    a. Adding new transportation modes (e.g Airplane, Boat) requires modifying the existing DirectionService class, which goes against the Open/Close Principle (classes should be open for extension but closed for modification).

3. Code Duplication and Reduced Maintainability:
    a. Similar code bloacks for different transportation modes can lead to code duplication, making the system less maintainable and more error-prone.

4. Scalability Issues:
    a. As more features or transportation modes are added, the class becomes bulky, impacting scalability and readability.


## State pattern structure:
1. *Context*: Holds a reference to the current state.
2. *State*: Interface for state-specific behavior.
3. *Concrete state*: Specific implementations of the State interface that represent a particular state of the context object.


## State Pattern Example
1. UI Navigation:
    Scenario: A mobile app UI where the navigation behaviour changes based on whether the user is logged in or not.
 Example:
    States: LoggedInState, LoggedOutState
    Context: The app's navigation system switches between these states.

2. UI Components: Buttons that change behaviour based on state (enabled, disabled, pressed)

3. Vending Machines: States like waiting for money, dispensing product or out of stock.

4. TCP Connections: Changing behaviour based on connection state (listening, connected, closed)
