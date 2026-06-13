from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

class ShoppingCart:
    
    def __init__(self, products: list[Product]):
        self.products = products

    def calculatePrice(self):
        total_price = 0
        for product in self.products:
            total_price += product.price

        print(total_price)

    def printInvoice(self):
        print("Printing invoice")

    def saveToDB(self):
        print("Saving product's to db")


monitor = Product("monitor",75000)
gpu = Product("gpu",450000)
cpu = Product("cpu",75000)

shopping_cart = ShoppingCart([monitor,gpu,cpu])
shopping_cart.calculatePrice()
shopping_cart.printInvoice()
shopping_cart.saveToDB()
