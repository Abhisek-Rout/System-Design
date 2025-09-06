## Decorator pattern
This pattern is used when you need to add functionality to an object at runtime, but subclassing would lead to an explosion of subclasses or is impractical.

## Problem statement
Let's say we have a simple Pizza ordering system. Initially we just have plain pizza but now we want to add options such as cheese, olives, tomatoes and mushrooms without modifying the existing pizza class or creating multiple subclass.

## Solution
Use a decorator to add the feature to the base class. Make individual feature classes.

## Benefits
1. This design is flexible and scalable for addition of more features.
2. Each class has its own responsibility.
3. It is open for modification but closed for change on existing feature.
4. Changes are dynammically implemented as per the client requirement, as you do not have to worry about the combinations any more.
5. Your do not have to worry about the combinations.