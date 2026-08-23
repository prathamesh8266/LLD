"""
Factory Design Pattern Practice

Goal:
Learn when to use factory patterns by solving small object-creation problems.

Core idea:
Use a factory when the client should not know which concrete class it is creating.
The client asks for "email", "sms", "upi", "stripe", etc. and receives an object
that follows a common interface.

How to practice:
1. Read the problem.
2. Fill the TODOs.
3. Run this file.
4. Compare the object names/output with what you expected.
"""

from abc import ABC, abstractmethod


# =============================================================================
# Problem 1: Simple Factory
# =============================================================================
"""
Scenario:
You are building a notification service. The app supports email, sms, and push
notifications.

When to use simple factory:
- You have one product family: Notification.
- You choose the concrete class using one input value.
- You want to hide object creation from the client.

Task:
Complete NotificationFactory.create_notification().
"""


class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        ...


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SmsNotification(Notification):
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


class PushNotification(Notification):
    def send(self, message: str) -> str:
        return f"Push sent: {message}"


# class NotificationFactory:
#     @staticmethod
#     def create_notification(notification_type: str) -> Notification:
#         # TODO:
#         # 1. Create a dictionary that maps:
#         #    "email" -> EmailNotification
#         #    "sms"   -> SmsNotification
#         #    "push"  -> PushNotification
#         # 2. Pick the class based on notification_type.
#         # 3. Raise ValueError for unknown types.
#         # 4. Return an object of the selected class.
#         raise NotImplementedError

class NotificationFactory:
    
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        
        notification_map = {
            "email": EmailNotification,
            "sms": SmsNotification,
            "push": PushNotification,
        }
        
        notification_type_class = notification_map.get(notification_type.lower())
        if notification_type_class is None:
            raise ValueError("Invalid Notification Type")
        
        return notification_type_class()
        

def problem_1_demo():
    notification = NotificationFactory.create_notification("email")
    print(notification.send("Your order is confirmed"))

# =============================================================================
# Problem 2: Factory Method
# =============================================================================
"""
Scenario:
Two companies process payments differently.

RazorpayFactory creates Indian payment processors.
StripeFactory creates international payment processors.

When to use factory method:
- You still create one product type: PaymentProcessor.
- But the creator/factory itself changes by company, platform, region, etc.
- Each factory decides which concrete class to instantiate.

Task:
Complete RazorpayFactory.create_processor() and StripeFactory.create_processor().
"""


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: int) -> str:
        ...


class UpiPayment(PaymentProcessor):
    def pay(self, amount: int) -> str:
        return f"Paid Rs.{amount} using UPI"


class CardPayment(PaymentProcessor):
    def pay(self, amount: int) -> str:
        return f"Paid Rs.{amount} using card"


class PaypalPayment(PaymentProcessor):
    def pay(self, amount: int) -> str:
        return f"Paid ${amount} using PayPal"


class InternationalCardPayment(PaymentProcessor):
    def pay(self, amount: int) -> str:
        return f"Paid ${amount} using international card"


class PaymentFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_processor(payment_type: str) -> PaymentProcessor:
        ...


# class RazorpayFactory(PaymentFactory):
#     @staticmethod
#     def create_processor(payment_type: str) -> PaymentProcessor:
#         # TODO:
#         # Support "upi" and "card".
#         raise NotImplementedError


# class StripeFactory(PaymentFactory):
#     @staticmethod
#     def create_processor(payment_type: str) -> PaymentProcessor:
#         # TODO:
#         # Support "paypal" and "card".
#         # "card" should create InternationalCardPayment.
#         raise NotImplementedError

class RazorpayFactory(PaymentFactory):
    @staticmethod
    def create_processor(payment_type: str) -> PaymentProcessor:
        payment_type_map = {
            'upi': UpiPayment,
            'card': CardPayment,
        }
        payment_type_class = payment_type_map.get(payment_type.lower())
        if payment_type_class is None:
            raise ValueError("Invalid Payment Type")
        return payment_type_class()


class StripeFactory(PaymentFactory):
    @staticmethod
    def create_processor(payment_type: str) -> PaymentProcessor:       
        payment_type_map = {
            'paypal': PaypalPayment,
            'card': InternationalCardPayment,
        }
        payment_type_class = payment_type_map.get(payment_type.lower())
        if payment_type_class is None:
            raise ValueError("Invalid Payment Type")
        return payment_type_class()


def problem_2_demo():
    indian_payment = RazorpayFactory.create_processor("upi")
    global_payment = StripeFactory.create_processor("card")

    print(indian_payment.pay(500))
    print(global_payment.pay(20))


# =============================================================================
# Problem 3: Abstract Factory
# =============================================================================
"""
Scenario:
You are building UI components for two themes: light and dark.
Each theme must create a matching button and checkbox.

When to use abstract factory:
- You create families of related objects.
- Objects from the same factory should be compatible with each other.
- Example families: LightButton + LightCheckbox, DarkButton + DarkCheckbox.

Task:
Complete LightThemeFactory and DarkThemeFactory.
"""


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        ...


class LightButton(Button):
    def render(self) -> str:
        return "Rendering light button"


class DarkButton(Button):
    def render(self) -> str:
        return "Rendering dark button"


class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering light checkbox"


class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering dark checkbox"


class ThemeFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_button() -> Button:
        ...

    @staticmethod
    @abstractmethod
    def create_checkbox() -> Checkbox:
        ...


class LightThemeFactory(ThemeFactory):
    @staticmethod
    def create_button() -> Button:
        return LightButton()

    @staticmethod
    def create_checkbox() -> Checkbox:
        return LightCheckbox()


class DarkThemeFactory(ThemeFactory):
    @staticmethod
    def create_button() -> Button:
        return DarkButton()

    @staticmethod
    def create_checkbox() -> Checkbox:
        return DarkCheckbox()


def problem_3_demo():
    factory = DarkThemeFactory

    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.render())
    print(checkbox.render())


# =============================================================================
# Quick Decision Practice
# =============================================================================
"""
For each situation, decide which one fits best:
1. Simple Factory
2. Factory Method
3. Abstract Factory

Questions:
1. Based on "pdf", "excel", or "csv", create one ReportExporter object.
2. Swiggy and Zomato both create DeliveryPartner objects, but each platform has
   different partner implementations.
3. Windows UI should create WindowsButton + WindowsMenu. Mac UI should create
   MacButton + MacMenu.
4. Based on "car", "bike", or "truck", create one Vehicle object.
5. Different cloud providers create matching Storage + Queue + Database objects.

Answers:
1. Simple Factory
2. Factory Method
3. Abstract Factory
4. Simple Factory
5. Abstract Factory
"""


if __name__ == "__main__":
    # Uncomment one problem at a time after you finish its TODOs.
    problem_1_demo()
    problem_2_demo()
    problem_3_demo()
    # pass
