# Adapter Pattern
The adapter pattern is a structural design pattern that allows objects with incompatible interfaces to work togeather.

## Problem Statement
Imagine you are working on an e-commerce application that needs to send email notifications to customers. Currently you are using your own in-house 'EmailNotificationService', but now you want to integrate a popular 3rd party service like 'SendGrid'. However, the interface for your in-house system and the SendGrid service are incompatible.

Let's see how the *Adapter Pattern* can solve this problem.

*Problem*: When two systems or components have incompatible interfaces, they cannot work togeather directly.

*Solution*: The Adapter Pattern bridges the gap by converting the interface of one class into another that the client expects.

## Real-world analogy:
A power adapter that allows a device with a US power plug to fit and work with a European power socket.

## Adapter Pattern Examples:
1. Adapters in Software Frameworks: In GUI frameworks, adapters are used to convert legacy code into newer formats.
2. Adapter in Java I/O: In Java *InputStreamReader* works as an adapter to convert InputStream(byte-based) to Reader (character-based)
3. Adapter in APIs: When integrating external libraries, you often need adapters to convert data formats or APIs to match your system's requirement.

The Adapter Pattern is a versatile solution to ensure incompatible interfaces work togeather seamlessly, making it invaluabe in software integration and legacy system migration.

## Adpater Pattern Benefits:
1. *Reusability*: You can reuse existing code even when its interface is not compatible with the current system.
2. *Flexibility*: It helps integrate classes from different libraries or systems that were not designed to work togeather.
3. *Decoupling*: The Adapter decouples the client from the specific implementation of the Adaptee.