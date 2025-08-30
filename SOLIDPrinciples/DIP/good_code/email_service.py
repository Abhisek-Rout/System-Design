from notification_channel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self, msg):
        print(f"Sending email {msg}")