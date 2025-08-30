# Strategy Pattern
Let's consider a simple payment system where users can pay using different methods like credit cards or PayPal. Without the strategy pattern, you might use if-else conditions to handle the different payment methods, leading to less maintainable and flexible code.


# Problems if we do not implement above using Strategy pattern
1. The PaymentService class has multiple responsibilities (deciding the payment type and processing it).
2. Adding a new payment method requires modifying the PaymentService class.
3. The use of if-else conditions can make the code harder to maintain as more payment types are added.

With the strategy pattern, the logic for each payment type is encapsulated in separate strategy classes and the PaymentService (context class) delegates the task of processing to one of these strategies at runtime.

