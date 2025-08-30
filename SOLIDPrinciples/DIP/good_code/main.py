from email_service import EmailService
from sms_service import SmsService
from notification_service import NotificationService

class Main:
    def main(self):
        email_notification: NotificationService = NotificationService(EmailService())
        email_notification.notify("Your order has been shipped")

        sms_notification: NotificationService = NotificationService(SmsService())
        sms_notification.notify("OTP 1234")

if __name__ == "__main__":
    main_obj = Main()
    main_obj.main()
