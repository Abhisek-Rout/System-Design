# Abstract Factory Pattern
Consider an application that needs to support multiple UI themes (e.g Windows, macOS). Each theme has its own set of UI components such as buttons, scrollbars and windows. The challenge is to cteate an architecture that allows switching between these themes without changing the client code that uses the UI components.

Without the Abstract Factory Pattern, the client code would tightly coupled with the concreate implementations of buttons, scrollbars etc and switching between themes would equire modifying the client code.

## Problems without Factory Pattern:
1. *Tight coupling*: The client is tightly coupled to specific implementations of UI components (WindowsButton, WindowsScrollBar)
2. *Hard to extend*: If we want to add support for macOS UI components, we would need to modify the client code to create instances of MacOSButton and MacOSScrollBar.


## Problems it resolves:
This approach provides an inerface for creating *families of related objects* without specifying their concrete classes.

## Structure:
1. *Abstract Factory*: Interface for creating abstract products.
2. *Concrete Factory*: Implements the abstract factory and creates concrete products.

Using the Abstract Factory Pattern, you create interfaces for each prodcut (e.g Button, ScrollBar, Window) and provide a family of concrete implementations for each theme (e.g WindowsButton, MacOSButton etc). The Abstract Facotry provides a way to create a suite of related objects without knowing the exact type of objects that will be created.