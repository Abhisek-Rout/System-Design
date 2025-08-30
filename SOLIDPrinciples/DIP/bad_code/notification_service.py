from email_service import EmailService
from sms_service import SmsService

class NotificationService:
    def notification_servie(self):
        self.email_service: EmailService = EmailService()
        self.sms_service: SmsService = SmsService()

    def notify_by_email(self, msg:str):
        self.email_service.send_mail(msg)

    def notify_by_sms(self, msg: str):
        self.sms_service.send_sms(msg)
