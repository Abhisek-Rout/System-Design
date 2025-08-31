# Singleton Pattern
In certain scenarios, such as managing a database connection, logging or configuration settings, you want to ensure that only one instance of a class is created throughout the application's lifecycle. If multiple instances were created, it could lead to issues like:
1. *Inconsistent state*: If multiple represent the sae concept, they may hold different data.
2. *Resource conflicts*: If multiple instances of a resource-heavy class are created, it can lead to performance degradation.

## When to use singleton pattern?
The singleton pattern is used when exactly one instance of a class is required to coordinate actions across the system.

## Use-cases:
1. *Global resource management* (eg managing database connections, logging)

2. *Configuration settings* in applications that need to be shared.

## Singleton pattern components:
1. Private Constructor: The constructor is private so that on other class can instantiate *AppSettings* directly.
2. Singleton Access: The *get_instance()* method is used to access the single instance of the settings.
3. Global Access: Any part of the application can access the settings using *AppSettings.get_instance()*.