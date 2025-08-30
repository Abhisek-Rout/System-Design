from notification_channel import NotificationChannel

class SmsService(NotificationChannel):
    def send(self, msg):
        print(f"Sending sms {msg}")