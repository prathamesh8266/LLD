r"""
Rules to follow while implementing LSV 

Terminalogy 
(broad) parent class 
eg. 
class Animal:
 ...
class Dog(Animal):
 ...

Animal is a broader class of Dog

(narrow) child class
Dog is a narrow class of Animal


"""

# 1. Signature rule
# eg. 1
class Parent:

    def add(self, a: int, b: int):
        ...

class Child(Parent):

    def add(self, a: int, b: int):
        ...

# eg. 2
class Parent:

    def add(self, a: str):
        ...

class Child(Parent):

    def add(self, a: str):
        ...

# possible in python, but this is not the Signature rule
class Parent:

    def add(self, a: int, b: int):
        return a+b

class Child(Parent):

    def add(self, a: int, b: int, c: int):
        print(super().add(a,b)+c)


r"""
Signature rule says the method signature in the extending class should be the same if its overriting the method, the argument types
and the return type
There are 3 types under Signature rule
1. Method type
2. Return type
3. Exception type
"""

r"""
Invariant rule (rule 2):
"""