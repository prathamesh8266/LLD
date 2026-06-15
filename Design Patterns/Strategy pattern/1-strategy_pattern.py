"""
Problem with Inheritance
1. code reuse
2. To add a new feature a lot of changes were required
3. Breaking OCP


Defination: 
Defines a family of Agodithm, puts them into seperate classes so that can change in runtime

whatever was getting broken using Inheritance can be solved by composition here
Polimorfism is heavily used here

- favour composition over inheritance
- Standard diagram
                          _______________________________
                         |          Context              |
                         |-------------------------------|
                         | - strategy: Strategy          |
                         |-------------------------------|
                         | + setStrategy(s: Strategy)    |
                         | + executeStrategy()           |
                         |_______________________________|
                                       |
                                       | - - -> Strategy
                                       v
                          _______________________________
                         |       <<interface>>           |
                         |          Strategy             |
                         |-------------------------------|
                         | + execute()                   |
                         |_______________________________|
                                      /_\
                                       |
                    -----------------------------------------
                    |                  |                    |
       _____________________  _____________________  _____________________
      | ConcreteStrategyA   || ConcreteStrategyB   || ConcreteStrategyC   |
      |---------------------||---------------------||---------------------|
      | + execute()         || + execute()         || + execute()         |
      |_____________________||_____________________||_____________________|
"""

from abc import ABC, abstractmethod

# Strategies i.e taking, walkin and flying
class Talkable(ABC):

    @abstractmethod
    def talk(self):
        ...

class Walkable(ABC):

    @abstractmethod
    def walk(self):
        ...

class Flyable(ABC):

    @abstractmethod
    def fly(self):
        ...

# client
class Robot(ABC):

    def __init__(self,talkable: Talkable, walkable: Walkable, flyable: Flyable):
        self.talkable = talkable
        self.walkable = walkable
        self.flyable = flyable

    @abstractmethod
    def looks(self):
        ...

class NormalTalk(Talkable):

    def talk(self):
        ...

class NoTalk(Talkable):

    def talk(self):
        ...


class NormalWalk(Walkable):

    def walk(self):
        ...

class NoWalk(Walkable):

    def walk(self):
        ...

r"""
         ____________________      ____________________      ____________________
        |  <<abstract>>      |    |  <<abstract>>      |    |  <<abstract>>      |
        |     Talkable       |    |     Walkable       |    |     Flyable        |
        |--------------------|    |--------------------|    |--------------------|
        | talk()             |    | walk()             |    | fly()              |
        |____________________|    |____________________|    |____________________|
                /_\   /_\                 /_\   /_\                    /_\
                 |     |                   |     |                      |
            -----   ------            -----      ------                 |
            |             |           |                |                |
         ______________ ______________ ______________ ______________    |
        |  NormalTalk  |  NoTalk     ||  NormalWalk ||  NoWalk      |   |
        |--------------|-------------||-------------||--------------|   |
        | talk()       | talk()      || walk()      || walk()       |   |
        |______________|_____________||_____________||______________|   |
                                                                        |
                (no concrete Flyable implementations in code)           |
                                                                        |
        ____________________                                            |
        |       Robot        |  uses                                     |
        |--------------------|------------------------------------------>|
        | talk: Talkable     |-------> Talkable                          |
        | walk: Walkable     |-------> Walkable                          |
        | fly:  Flyable      |---------------------------------(above)---
        |--------------------|
        | looks()            |
        |____________________|
"""

class CompanionRobot(Robot):

    def __init__(self,talkable: Talkable, walkable: Walkable, flyable: Flyable):
        super().__init__(talkable,walkable,flyable)

    def looks(self):
        ...


companionRobot: Robot = CompanionRobot(NormalTalk(),NormalWalk(),...)

"""
Usages:
can be used in payment strategy
"""

class Pay(ABC):

    @abstractmethod
    def pay(self):
        ...

class UPI(Pay):

    def pay(self):
        ...

class Card(Pay):

    def pay(self):
        ...

class PaymentSystem:

    def __init__(self, pay: Pay ):
        self.pay = pay

    def payNow(self):
        self.pay.pay()


"""
- Encapsulate what varies and keep it seperate from what remains same
- Solution to inheritance is not more inheritance
- Composition should be favoired over inheritance
- Code to interface and not to concreation
- DIY (Do Not Repeat Yourself)
"""