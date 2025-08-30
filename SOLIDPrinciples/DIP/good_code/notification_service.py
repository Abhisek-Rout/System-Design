from notification_channel import NotificationChannel

class NotificationService(NotificationChannel):
    def __init__(self, channel: NotificationChannel):
        self.notification_channel = channel

    def notify(self, msg: str):
        self.notification_channel.send(msg)