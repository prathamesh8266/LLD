"""
Class should be one for extension and close for modification
eg. To integrate a new feature you should not modify the methods/ add the methods of previously implemented class
"""

"""
Problem in previous SRP flow, what is we want to store the products to files as well as other databases,
adding saveTOMong(), saveToFile() inside cartDBStorage would be wrong as it will break open close principle

we can solve this issue using abstraction, injheritance and polimorfism
___________________                _______________________________
|     Product     |                |         ShoppingCart        |
|-----------------|    1...*       |-----------------------------|
|name: str        |<---------------|products: list[Product]      |
|price: float     |    (has-a)     |calculateTotalPrice()        |
|_________________|                |getProducts()                |
                                   |_____________________________|
                                       ^                       ^
                                       |                       |
                               (has-a) | 1             (has-a) | 1
                                       |                       |
                        _______________|_______         _______|_______________
                        |  cartInvoicePrinter |         |    cartDBStorage    |
                        |---------------------|         |---------------------|
                        |shoppingCart:        |         |shoppingCart:        |
                        |  ShoppingCart       |         |  ShoppingCart       |
                        |printInvoice()       |         |saveToDB()           |
                        |_____________________|         |_____________________|
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Product:
    name: str
    price: float

class ShoppingCart:
    
    def __init__(self,products: list[Product]):
        self.products = products

    def calculateTotalPrice(self):
        total_price = 0
        for product in self.products:
            total_price += product.price

        return total_price

    def getProducts(self):
        return self.products
    
class Printer(ABC):

    @abstractmethod
    def print(self,shoppingCart:ShoppingCart):
        ...

class Storage(ABC):

    @abstractmethod
    def store(self,shoppingCart:ShoppingCart):
        ...

class cartInvoicePrinter(Printer):

    def __init__(self, shoppingCart: ShoppingCart):
        self.shoppingCart = shoppingCart

    def print(self):
        print("Shopping cart invoice")
        for product in self.shoppingCart.products:
            print(f'name: {product.name} - ${product.price}')

        print(f"Total: ${self.shoppingCart.calculateTotalPrice()}")

class cartDBStorage(Storage):

    def __init__(self, shoppingCart: ShoppingCart):
        self.shoppingCart = shoppingCart

    def store(self):
        print("Saving product's to db")


monitor = Product("monitor",75000)
gpu = Product("gpu",450000)
cpu = Product("cpu",75000)

shopping_cart = ShoppingCart([monitor,gpu,cpu])

print_invoice = cartInvoicePrinter(shopping_cart)
print_invoice.print()


store_to_db = cartDBStorage(shopping_cart)
store_to_db.store()