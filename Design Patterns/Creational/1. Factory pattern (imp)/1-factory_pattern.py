"""
Seperate buisness logic from object creation logic
- simple factory (principle)
- factory method (pattern)
- abstract factory method (pattern)
"""

# Simple factory

from abc import ABC, abstractmethod

class Burger(ABC):

    @abstractmethod
    def prepeare(self):
        ...

class BasicBurger(Burger):

    def prepeare(self):
        ...

class StandardBurger(Burger):

    def prepeare(self):
        ...

class PremiumBurger(Burger):

    def prepeare(self):
        ...

class BurgerFactory:

    @staticmethod
    def createBurget(burger_type: str) -> Burger:
        burger_dict = {
            "basic": BasicBurger,
            "standard": StandardBurger,
            "premium": PremiumBurger,
        }
        burger_class = burger_dict.get(burger_type.lower())
        if burger_class is None:
            raise ValueError(f"Unknown burger type: {burger_type}")
        return burger_class()
    

# print(BurgerFactory().createBurget('basic').__class__.__name__)

r"""
                    ______________________________________
                   |            BurgerFactory             |
                   |--------------------------------------|
                   | + createBurget(burger_type: str):    |- - - - - - - - - - - - - - - - -> creates
                   |              Burger  <<static>>      |
                   |______________________________________|
                              |
                              | 
                              v
                    _______________________
                   |     <<abstract>>      |
                   |        Burger         |
                   |-----------------------|
                   | prepeare()            |
                   |_______________________|
                            /_\
                             |
          ---------------------------------------------
          |                   |                       |
 ___________________  ___________________  ___________________
|   BasicBurger     ||  StandardBurger   ||  PremiumBurger    |
|-------------------||-------------------||-------------------|
| prepeare()        || prepeare()        || prepeare()        |
|___________________||___________________||___________________|

Simple factory:
A Factory class that decides which congcrete class to instintiate


                    ______________________________________
                   |              Factory                 |
                   |--------------------------------------|
                   | + createProduct(type: str): Product  |
                   |                        <<static>>    |
                   |______________________________________|
                              |
                              | - - -> creates
                              v
                    _______________________
                   |     <<abstract>>      |
                   |       Product         |
                   |-----------------------|
                   | + operation()         |
                   |_______________________|
                             /_\
                              |
          ---------------------------------------------
          |                   |                       |
 ___________________  ___________________  ___________________
| ConcreteProductA  || ConcreteProductB  || ConcreteProductC  |
|-------------------||-------------------||-------------------|
| + operation()     || + operation()     || + operation()     |
|___________________||___________________||___________________| 
"""

################################################################################
################################################################################
# Factory pattern (design pattern)
"""
Defination: Defines an interface for creating objects but allow subclasses to decide which class to instintiate
"""
class Burger(ABC):

    @abstractmethod
    def prepeare(self):
        ...

class BasicBurger(Burger):

    def prepeare(self):
        ...

class StandardBurger(Burger):

    def prepeare(self):
        ...

class PremiumBurger(Burger):

    def prepeare(self):
        ...

class BasicWheatBurger(Burger):

    def prepeare(self):
        ...

class StandardWheatBurger(Burger):

    def prepeare(self):
        ...

class PremiumWheatBurger(Burger):

    def prepeare(self):
        ...

class BurgerFactory(ABC):

    @staticmethod
    @abstractmethod
    def createBurger(self):
        ...

class SinghFactory(BurgerFactory):

    @staticmethod
    def createBurger(burger_type: str):
        burger_dict = {
            "basic": BasicBurger,
            "standard": StandardBurger,
            "premium": PremiumBurger,
        }
        burger_class = burger_dict.get(burger_type.lower())
        if burger_class is None:
            raise ValueError(f"Unknown burger type: {burger_type}")
        return burger_class()

class KingFactory(BurgerFactory):

    @staticmethod
    def createBurger(burger_type: str):
        burger_dict = {
            "basic": BasicWheatBurger,
            "standard": StandardWheatBurger,
            "premium": PremiumWheatBurger,
        }
        burger_class = burger_dict.get(burger_type.lower())
        if burger_class is None:
            raise ValueError(f"Unknown burger type: {burger_type}")
        return burger_class()
    

print(SinghFactory().createBurger('basic').__class__.__name__)
print(SinghFactory().createBurger('standard').__class__.__name__)
print(KingFactory().createBurger('basic').__class__.__name__)
print(KingFactory().createBurger('premium').__class__.__name__)

r"""
   __________________________            creates             _______________________
  |     «abstract»           |  - - - - - - - - - - - - ->   |     «abstract»        |
  |     BurgerFactory        |                               |        Burger         |
  |--------------------------|                               |-----------------------|
  | createBurger()           |                               | prepeare()            |
  |__________________________|                               |_______________________|
              /_\                                                       /_\
               |                                                         |
       ----------------                              -----------------------------------------
       |              |                              |                                       |
  _____________  _____________            (Singh's plain variants)                (King's wheat variants)
 |SinghFactory ||KingFactory  |                      |                                       |
 |-------------||-------------|            ___________________               ___________________
 |createBurger ||createBurger |          | BasicBurger       |             | BasicWheatBurger  |
 |   (type)    ||   (type)    |          |-------------------|             |-------------------|
 |_____________||_____________|          | prepeare()        |             | prepeare()        |
                                         |___________________|             |___________________|
                                          ___________________               ___________________
                                         | StandardBurger    |             | StandardWheatBurger|
                                         |-------------------|             |-------------------|
                                         | prepeare()        |             | prepeare()        |
                                         |___________________|             |___________________|
                                          ___________________               ___________________
                                         | PremiumBurger     |             | PremiumWheatBurger |
                                         |-------------------|             |-------------------|
                                         | prepeare()        |             | prepeare()        |
                                         |___________________|             |___________________|

   SinghFactory -> Basic / Standard / Premium Burger
   KingFactory  -> Basic / Standard / Premium WheatBurger


Generalized diagram

   __________________________            creates              _______________________
  |     «abstract»           |  - - - - - - - - - - - - ->   |     «abstract»        |
  |       Creator            |                               |       Product         |
  |--------------------------|                               |-----------------------|
  | + factoryMethod():Product|                               | + operation()         |
  | + someOperation()        |                               |_______________________|
  |__________________________|                                        /_\
            /_\                                                        |
             |                                          ----------------------------------
      ----------------                                  |                                |
      |              |                          ___________________              ___________________
  ________________  ________________           | ConcreteProductA  |            | ConcreteProductB  |
 |ConcreteCreatorA||ConcreteCreatorB|          |-------------------|            |-------------------|
 |----------------||----------------|          | + operation()     |            | + operation()     |
 |+factoryMethod()||+factoryMethod()|          |___________________|            |___________________|
 |________________||________________|
        |                  |
        |                  ----------- creates ----------> ConcreteProductB
        --------------------- creates ------------------> ConcreteProductA

"""
################################################################################
################################################################################
### Abstract Factory
"""
Defination: provides an interface for creating famalies of relted objects withot specifing the concrete class
"""
class Burger(ABC):

    @abstractmethod
    def prepeare(self):
        ...

class BasicBurger(Burger):

    def prepeare(self):
        ...

class StandardBurger(Burger):

    def prepeare(self):
        ...

class PremiumBurger(Burger):

    def prepeare(self):
        ...

class BasicWheatBurger(Burger):

    def prepeare(self):
        ...

class StandardWheatBurger(Burger):

    def prepeare(self):
        ...

class PremiumWheatBurger(Burger):

    def prepeare(self):
        ...

class GarlicBread(ABC):

    @abstractmethod
    def prepare(self):
        ...

class CheeseGarlicBread(GarlicBread):

    def prepare(self):
        ...

class NormalGarlicBread(GarlicBread):

    def prepare(self):
        ...

class MealFactory(ABC):

    @staticmethod
    @abstractmethod
    def createBurger(burger_type: str) -> Burger:
        ...    

    @staticmethod
    @abstractmethod
    def createGarlicBread(garlic_bread_type: str) -> GarlicBread:
        ...


class SinghFactory(MealFactory):

    @staticmethod
    def createBurger(burger_type: str):
        burger_dict = {
            "basic": BasicBurger,
            "standard": StandardBurger,
            "premium": PremiumBurger,
        }
        burger_class = burger_dict.get(burger_type.lower())
        if burger_class is None:
            raise ValueError(f"Unknown burger type: {burger_type}")
        return burger_class()
    
    @staticmethod
    def createGarlicBread(garlic_bread_type: str):
        garlic_bread_dict = {
            "normal": NormalGarlicBread,
            "cheese": CheeseGarlicBread
        }
        garlic_bread_class = garlic_bread_dict.get(garlic_bread_type.lower())
        if garlic_bread_class is None:
            raise ValueError(f"Unknown garlic bread type: {garlic_bread_type}")
        return garlic_bread_class()

class KingFactory(MealFactory):

    @staticmethod
    def createBurger(burger_type: str):
        burger_dict = {
            "basic": BasicWheatBurger,
            "standard": StandardWheatBurger,
            "premium": PremiumWheatBurger,
        }
        burger_class = burger_dict.get(burger_type.lower())
        if burger_class is None:
            raise ValueError(f"Unknown burger type: {burger_type}")
        return burger_class()
    
    @staticmethod
    def createGarlicBread(garlic_bread_type: str):
        garlic_bread_dict = {
            "normal": NormalGarlicBread,
            "cheese": CheeseGarlicBread
        }
        garlic_bread_class = garlic_bread_dict.get(garlic_bread_type.lower())
        if garlic_bread_class is None:
            raise ValueError(f"Unknown garlic bread type: {garlic_bread_type}")
        return garlic_bread_class()
    

# used in notification system where there are multiple notification types, eg. sms, email, push
# the way you will have to decide strategy pattern to use of factory pattern is by checking what you actually want.
# seperate object creation or strategy implementation as notification system can be created using strategy pattern toor