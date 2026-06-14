r"""
Many client specific interfaces are better than one general purpose interface.
client should not be forced to implement the method they dont need
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

class Square(Shape):

    def area(self):
        ...

class Circle(Shape):

    def area(self):
        ...

class Cube(Shape):

    def area(self):
        ...

    def volume(self): 
        ...
    # this is the issue, now we will need to add volume() as a abstract method in Shape and force Square and Circle 
    # to implement it


# Solution

class TwoDShape(ABC):

    @abstractmethod
    def area(self):
        ...

class ThreeDShape(ABC):

    @abstractmethod
    def volume(self):
        ...

    @abstractmethod
    def area(self):
        ...

class Square(TwoDShape):

    def area(self):
        ...

class Circle(TwoDShape):

    def area(self):
        ...

class Cube(ThreeDShape):

    def area(self):
        ...

    def volume(self): 
        ...

r"""
             ___________________________               ___________________________
            |     <<abstract>>          |            |     <<abstract>>          |
            |     TwoDShape             |            |     ThreeDShape           |
            |---------------------------|            |---------------------------|
            | area()                    |            | area()                    |
            |___________________________|            | volume()                  |
                        /_\                          |___________________________|
                         |                                       /_\
                ----------------                                  |
                |              |                           ________________
        _________________  _________________              |     Cube       |
        |    Square       ||    Circle       |            |----------------|
        |-----------------||-----------------|            | area()         |
        | area()          || area()          |            | volume()       |
        |_________________||_________________|            |________________|
"""