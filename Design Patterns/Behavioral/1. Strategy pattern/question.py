"""
Strategy Pattern Practice Question

Problem:
You are building a delivery cost calculator for an e-commerce checkout system.

The checkout system supports multiple delivery options:
- standard delivery
- express delivery
- same-day delivery

Each option calculates delivery cost differently.

Goal:
Design this using the Strategy pattern.

Constraint:
The checkout code should not contain if/else or match/case logic for calculating
delivery cost based on delivery type.

The delivery calculation behavior should be replaceable at runtime.

Example behavior:

Order amount: 1000
Distance: 12 km

Standard delivery might calculate a low cost.
Express delivery might calculate a higher cost.
Same-day delivery might calculate the highest cost.

Expected output can be something like:

Standard delivery cost: 60
Express delivery cost: 120
Same-day delivery cost: 180

Important:
Focus on separating the varying algorithm from the checkout/order context.
"""

f"""Entities
Checkout
Delivery
"""

from abc import ABC, abstractmethod

class Delivery(ABC):
    
    @abstractmethod
    def calculate_cost(self, weight: int, distance: int) -> float:
        ...
        
class StandardDelivery(Delivery):
    
    def calculate_cost(self, weight, distance):
        return f"Standard delivery cost: {weight*distance}"
        
class ExpressDelivery(Delivery):
    
    def calculate_cost(self, weight, distance):
        return f"Express delivery cost: {weight*distance*2}"
        
class SameDayDelivery(Delivery):
    
    def calculate_cost(self, weight, distance):
        return f"Same-Day delivery cost: {weight*distance*3}"
        
class Checkout:
    
    def __init__(self, delivery: Delivery):
        self.delivery = delivery

    def set_delivery(self, delivery: Delivery):
        self.delivery = delivery

    def calculate_delivery_cost(self, weight, distance):
        return self.delivery.calculate_cost(weight, distance)

user_checkout = Checkout(StandardDelivery())
standard_checkout_cost = user_checkout.calculate_delivery_cost(12, 200)
print(standard_checkout_cost)