from notification_collection import EmailNotifications, SMSNotifications, PushNotifications
from notification_manager import NotificationManager

class Exercise:
    def main(self):
        # Create collections
        emails = EmailNotifications()
        sms = SMSNotifications()
        push = PushNotifications()

        # Add notifications
        emails.add_notification("Email: Meeting at 10 AM")
        emails.add_notification("Email: Project deadline tomorrow")

        sms.add_notification("SMS: Your OTP is 123456")
        sms.add_notification("SMS: Recharge successful")

        push.add_notification("Push: New friend request")
        push.add_notification("Push: Package delivered")

        # Notification Manager handles all collections
        manager = NotificationManager(emails, sms, push)

        # Iterate seamlessly
        print("---- All Notifications ----")
        for notification in manager:
            print(notification)

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()


"""
Module Type → Application entry point.

Purpose → Simulates real usage: adds notifications, then iterates through them.

Significance →

Verifies that the Iterator Pattern hides internal storage details.

Demonstrates extensibility (adding more notifications/collections doesn’t require touching the existing iterator code).
"""