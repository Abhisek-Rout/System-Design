# Meal Builder Application Exercise
You are tasked with designing a Meal Builder application that allows users to customize their meal by selecting various components such as a main dish, a side dish, and a drink. Each meal should include optional components such as desserts or appetizers. The system should allow flexibility in meal creation, ensuring users can choose only the components they want, while providing default options for any component they skip.



Requirements:

Implement the Builder Design Pattern to allow flexible meal creation.

Each meal must have a main dish, side dish, and drink, with optional components like dessert and appetizer.

Provide default values for any component not explicitly set by the user.

Once a meal is built, the application should display a summary of the meal components.

Ensure the builder is easy to extend, in case more components are added in future (e.g., sauces, salads, etc.).



Task:

Use the Builder Design Pattern to construct a meal based on user preferences. Implement a MealBuilder class to manage the construction of the meal components and a Meal class to represent the final meal.



Instructions:

Implement the MealBuilder class that allows adding various components to the meal.

Ensure the builder can chain method calls for setting components.

Default options should be included for components the user does not set explicitly.

After building the meal, print out a summary of the selected components.



Output:

After executing the code, you should create a meal by setting at least two components and leaving the rest to default values. Then, print a summary of the final meal, including both the user-selected and default components.



Instructions:

You only need to complete the TODOs mentioned in the code.

Please do not modify any existing code outside of the specified TODO sections.