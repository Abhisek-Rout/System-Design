# Factory Pattern
Consider an example of a transporation service app where users can request different types of transportation vehicles (e.g Car, Bike, Bus). You might initially create seperate classes of each type and ceate instances like this:
    car: Car = Car()
    bike: Bike = Bike()
But as the system evolves, managing object creation directly like this can become complex, especially when adding new types of vehicles.

## Problems without factory pattern
1. The client code (i.e TransportService) is tightly coupled to concrete classes (Car, Bike, Bus)
2. Adding new transport types requires modifying client code.

## Why factory pattern?
The factory pattern helps centralize the creation logic and delegates the responsibility of creating objects to factory classes, which decide the specific class to instantiate. This allows the code to adhere to the Open/Closed principle by letting new types of vehicles to be added without modifying the existing code.

## Benefits of factory pattern
1. *Factory class*: The TransportFactory class contains the logic to create different types of transport based on the input string. This abstracts the creation logic and makes it easier to add or change transport types.
2. *Decoupling*: The TransportService class(client) no longer needs to know the details of how Car, Bike or Bus are created. It simply calls the factory method.
3. *Flexibility*: Adding a new transport type (e.g Truck) only requires modifying the factory, not the client code.

## Real World Use Cases
1. *GUI Frameworks*: When the type of button or widget to be created is determined at runtime based on the platfrom (e.g Windows, macOS, Linux).
2. *Database Connectivity*: When choosing different types of databases (e.g SQL, NoSQL) based on configuration.
3. *Different Conversion Tools*: Where the type of file (e.g PDF, Word, HTML) to be created depends on user inputs or settings.

The factory desing pattern is a fundamental tool to reduce coupling and centralize object creation logic, especially in systems that need to support multiple types of objects.