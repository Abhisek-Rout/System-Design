# Observer pattern
Suppose we have a weather station that records temperature and multiple devices (e.g display units) want to show the latest temperature. Without using the observer pattern, the weather station would have to explicitly inform each device about the temperature change, which results in tight coupling between the station and devices.


## Benefits of observer pattern
1. *Loose Coupling*: The subject (e.g WeatherStation) doesn't need to know about the specific observers. It just notifies them.
2. *Scalability*: New observers (e.g new display devices) can easily be added without changing the subject.
3. *Flexibility*: Observers can be dynamically added or removed at runtime.
Note: It is a typical example of Publisher-Subscriber model.

## Observer pattern use-case
1. *Event Listners*: GUI frameworks often use the Observer Pattern to implement event listners for handling button clicks, input changes etc.
2. *Stock Price Monitoring*: When a stock price changes, multiple subscribers (like investors or systems) can be notified of the change.
3. *News Publishing Systems*: News articles are published (subject), and subscribers (users) are notified whenever a new article is available.
4. *Social Media Notifications*: Users can subscribe to updates form specific accounts, and when an account posts (subject), all followers (observers) are notified.
5. *Logging Systems*: Different logging handlers can observe events and log them as needed, such as to the console, file or remote server.