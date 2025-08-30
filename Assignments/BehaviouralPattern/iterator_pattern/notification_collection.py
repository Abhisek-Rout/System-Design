from aggregate import Aggregate
from notification_iterator import NotificationIterator

# ---------- Concrete Notification Collections ----------
class NotificationCollection(Aggregate):
    """Base collection for notifications"""
    def __init__(self):
        self._items = []

    def add_notification(self, message: str):
        self._items.append(message)

    def create_iterator(self):
        return NotificationIterator(self._items)


class EmailNotifications(NotificationCollection):
    pass


class SMSNotifications(NotificationCollection):
    pass


class PushNotifications(NotificationCollection):
    pass

