from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, body: str):
        pass

class EmailNotificationService(NotificationService):
    def send(self, to: str, subject: str, body: str):
        print(f"Sending email to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")

class SendGridService:
    def send_email(self, recipient: str, title: str, content:str):
        print(f"Sending email via SendGrid to {recipient}")
        print(f"Title: {title}")
        print(f"Content: {content}")


class SendGridAdapter(NotificationService):
    def __init__(self, send_grid_service: SendGridService):
        self.send_grid_service = send_grid_service

    def send(self, to, subject, body):
        self.send_grid_service.send_email(to, subject, body)
 

class WithAdapterPattern:
    def main(self):
        email_service: NotificationService = EmailNotificationService()
        email_service.send("customer@coding.com", "Order confirmation", "Your order has been received.")
        
        send_grid_email_service: NotificationService = SendGridAdapter(SendGridService()) # SendGrid object passed on SendGridAdapter
        send_grid_email_service.send("customer@coding.com", "Order confirmation", "Your order has been received.")

if __name__ == "__main__":
    obj: WithAdapterPattern = WithAdapterPattern()
    obj.main()

