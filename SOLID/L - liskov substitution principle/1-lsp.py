"""
Subclasses should be substutable of their base classes

eg. A is a base class and B is a subclass that inherits/extends base class (A)
any client that expects a base class A should also work with sub class B, A child class should behave like parent class
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class User:
    name: str
    accounts: list[Account]


class Account(ABC):

    @abstractmethod
    def deposit(self):
        ...

    @abstractmethod
    def withdraw(self):
        ...

class SavingsAccount(Account):

    def deposit(self):
        pass

    def withdraw(self):
        pass

class CurrentAccount(Account):

    def deposit(self):
        pass

    def withdraw(self):
        pass

class FixedAccount(Account): # Fixed deposite FD

    def deposit(self):
        pass

    def withdraw(self):
        raise Exception("Cannot call withdraw on FixedAccount") 
    
r"""
___________________________
|         User              |
|---------------------------|
| name: str                 |
| accounts: list[Account]   |
|___________________________|
              |
              | 1
              |
              o  aggregates
              |
              | *
              v
 ___________________________
|     <<abstract>>          |
|       Account             |
|---------------------------|
| deposit()                 |
| withdraw()                |
|___________________________|
             /_\
              |
      ------------------------------------------------
      |                      |                        |
 _________________   _________________      _____________________
| SavingsAccount  | | CurrentAccount  |    |   FixedAccount      |
|-----------------| |-----------------|    |---------------------|
| deposit()       | | deposit()       |    | deposit()           |
| withdraw()      | | withdraw()      |    | withdraw()          |
|_________________| |_________________|    |_____________________|

User aggregates Account (1 user → * accounts; the o marks aggregation since accounts can exist independently of the user object).
Account is abstract with abstract deposit() / withdraw(), realized by the three concrete subclasses via the /_\ inheritance triangle.

In this above code SavingsAccount and CurrentAccount can be used interchangable for Account but FixedAccount cannot be used, because
the client will be interacting with the abstract class Account (as that will act as an abstraction layer between the client and 
the buisness logic), now the client do not know that it cannot call withdraw() on FixedAccount as it will throw an exception,
here the LSP is broken
we cannot modify the client deirectly 
eg. if class name == FixedAccount:
        ...
    else:
        ...

here the code became tightly coupled, and to solve LSP we broke SRP, now if any new class will come in the client should again know about
it, and now we will have to change the client also

the solution to this is as follows
"""

class NonWithdrawableAccount(ABC):

    @abstractmethod
    def deposit(self):
        ...

class WithdrawableAccount(NonWithdrawableAccount, ABC):

    @abstractmethod
    def withdraw(self):
        ...

class FixedAccount(NonWithdrawableAccount):

    def deposit(self):
        print("Amount deposited to FixedAccount")


class SavingsAccount(WithdrawableAccount):

    def deposit(self):
        print("Amount deposited to SavingsAccount")

    def withdraw(self):
        print("Amount withdrawed from SavingsAccount") 


class CurrentAccount(WithdrawableAccount):

    def deposit(self):
        print("Amount deposited to CurrentAccount")

    def withdraw(self):
        print("Amount withdrawed from CurrentAccount") 


class Client:
    nonWithdrawableAccounts: list[NonWithdrawableAccount] = ... # client knows it cannot call .withdraw() on this
    withdrawableAccounts: list[WithdrawableAccount] = ... # client knows it can call both .withdraw() and .deposit() on this


r"""
                       ____________________________
                      |     <<abstract>>           |
                      |  NonWithdrawableAccount    |
                      |----------------------------|
                      | deposit()                  |
                      |____________________________|
                                  /_\
                                   |
                  -----------------------------------
                  |                                 |
 ____________________________            ____________________________
|       FixedAccount         |          |     <<abstract>>           |
|----------------------------|          |   WithdrawableAccount      |
| deposit()                  |          |----------------------------|
|____________________________|          | withdraw()                 |
                                        |____________________________|
                                                     /_\
                                                      |
                                      -------------------------------
                                      |                             |
                       ____________________________    ____________________________
                      |     SavingsAccount         |   |     CurrentAccount         |
                      |----------------------------|   |----------------------------|
                      | deposit()                  |   | deposit()                  |
                      | withdraw()                 |   | withdraw()                 |
                      |____________________________|   |____________________________|


 ______________________________________________________
|                       Client                          |
|-------------------------------------------------------|
| nonWithdrawableAccounts: list[NonWithdrawableAccount] |
| withdrawableAccounts: list[WithdrawableAccount]       |
|_______________________________________________________|
       |                                    |
       | uses                               | uses
       v                                    v
 (NonWithdrawableAccount)            (WithdrawableAccount)
"""