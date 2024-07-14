# Dependency Inversion Principle (DSP)

# Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces).

# ##################
# Bad Implementation
# ##################

# This is a bad implementation because our high level NotificationService class depends on lower level modules including EmailService and SMSService

class EmailService:
    def send_email(self, message, reciever):
        print(f"Sending email: {message} to {reciever}")

class SMSService:
    def send_sms(self, message, reciever):
        print(f"Sending SMS: {message} to {reciever}")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
    
    def send_notification(self, message, reciever, method):
        if method == "email":
            self.email_service.send_email(message, reciever)
        elif method == "sms":   
            self.sms_service.send_sms(message, reciever)


if __name__ == "__main__":
    # Set Up
    print("Bad Implementation (Dependency Inversion Principle)")
    notification_service = NotificationService()

    # Method Execution
    notification_service.send_notification("Hello!", "Jacob", "email")
    notification_service.send_notification("Hello!", "Jacob", "sms")
    print("\n")


# ###################
# Good Implementation
# ###################

# This is a good implementation because both high level and low level classes depend on abstractions as opposed to concrete implementations
from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, reciever):
        pass

class EmailService(IMessageService):
    def send(self, message, reciever):
        print(f"Sending email: {message} to {reciever}")

class SMSService(IMessageService):
    def send(self, message, reciever):
        print(f"Sending SMS: {message} to {reciever}")

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message, reciever):
        self.message_service.send(message, reciever)


if __name__ == "__main__":
    # Set Up
    print("Good Implementation (Dependency Inversion Principle)")
    email_service = EmailService()
    sms_service = SMSService()
    notification_service_email = NotificationService(email_service)
    notification_service_sms = NotificationService(sms_service)

    # Method Execution
    notification_service_email.send_notification("Hello!", "Jacob")
    notification_service_sms.send_notification("Hello!", "Jacob")