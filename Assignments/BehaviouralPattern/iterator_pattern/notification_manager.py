# ---------- Notification Manager (for seamless iteration) ----------
from aggregate import Aggregate

class NotificationManager:
    def __init__(self, *collections: Aggregate):
        self._collections = collections

    def __iter__(self):
        for collection in self._collections:
            for notification in collection.create_iterator():
                yield notification

"""
Module Type → High-level façade.

Purpose → Lets you iterate across multiple collections seamlessly (emails, SMS, push).

Uses yield (Python generator) so it looks like a single unified stream of notifications.

Significance →

Client code doesn’t need to worry about which collection to loop over.

If you add a new collection type (like Slack), just pass it to the manager.
"""