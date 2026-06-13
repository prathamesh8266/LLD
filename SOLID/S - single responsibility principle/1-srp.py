"""
NOTE: SRP dosent mean each class should have 1 method, it means each class should have 1 responsibility (all the methods should work for a single responsibility)
"""

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

class ShoppingCart:
    
    def __init__(self, products: list[Product]):
        self.products = products

    def calculateTotalPrice(self):
        total_price = 0
        for product in self.products:
            total_price += product.price

        return total_price

    def printInvoice(self):
        print("Shopping cart invoice")
        for product in self.products:
            print(f'name: {product.name} - ${product.price}')

        print(f"Total: ${self.calculateTotalPrice()}")

    def saveToDB(self):
        print("Saving product's to db")


# monitor = Product("monitor",75000)
# gpu = Product("gpu",450000)
# cpu = Product("cpu",75000)

# shopping_cart = ShoppingCart([monitor,gpu,cpu])
# shopping_cart.calculateTotalPrice()
# shopping_cart.printInvoice()
# shopping_cart.saveToDB()

"""
___________________                _______________________________
|     Product     |                |         ShoppingCart        |
|-----------------|    1...*       |-----------------------------|
|name: str        |<---------------|products: list[Product]      |
|price: float     |    (has-a)     |calculateTotalPrice()        |
|_________________|                |printInvoice()               |
                                   |saveToDB()                   |
                                   |_____________________________|
"""
"""
The above soultion is not correct as it does not follow single responsibility principle, is anything changes within those 3 functions the ShoppingCart class will need a 
modification

To solve this we will be using COMPOSITION (tight coupling)
Better approach is bellow
"""

@dataclass
class Product:
    name: str
    price: float

class ShoppingCart:
    
    def __init__(self, products: list[Product]):
        self.products = products
    
    def calculateTotalPrice(self):
        total_price = 0
        for product in self.products:
            total_price += product.price

        return total_price

    def getProducts(self):
        return self.products
    

class cartInvoicePrinter:

    def __init__(self, shoppingCart: ShoppingCart):
        self.shoppingCart = shoppingCart

    def printInvoice(self):
        print("Shopping cart invoice")
        for product in self.shoppingCart.products:
            print(f'name: {product.name} - ${product.price}')

        print(f"Total: ${self.shoppingCart.calculateTotalPrice()}")

class cartDBStorage:

    def __init__(self, shoppingCart: ShoppingCart):
        self.shoppingCart = shoppingCart

    def saveToDB(self):
        print("Saving product's to db")

monitor = Product("monitor",75000)
gpu = Product("gpu",450000)
cpu = Product("cpu",75000)

shopping_cart = ShoppingCart([monitor,gpu,cpu])

print_invoice = cartInvoicePrinter(shopping_cart)
print_invoice.printInvoice()


store_to_db = cartDBStorage(shopping_cart)
store_to_db.saveToDB()

"""
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
"""
Now every class holds 1 responsibility and has only 1 reason to change
"""