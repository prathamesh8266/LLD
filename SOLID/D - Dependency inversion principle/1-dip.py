"""
High level module should not depend on low level module, rather both should depend on abstraction
i.e high level module should not interact deirectly with low level module, there should be an interface/contract in between
"""

class Application:

    def __init__(self, sql_client: SQLClient, mongo_client: MongoClient):
        self.sql_client = sql_client
        self.mongo_client = mongo_client

    def saveToDB(self):
        self.sql_client.save()
        self.mongo_client.save()

class SQLClient:

    def save(self):
        ...

class MongoClient:

    def save(self):
        ...

""" 
Here the applicaiton (high level module) is talking directly to sql and mongo which are low level modules, tommorow if we 
add Casandra then we will need to change the logic in application because its tightly coupled
"""

from abc import ABC, abstractmethod

class Application:

    def __init__(self, persistance: Persistance):
        self.persistance = persistance

    def saveToDB(self):
        self.persistance.save()

class Persistance(ABC):

    @abstractmethod
    def save(self):
        ...

class SQLClient(Persistance):

    def save(self):
        ...

class MongoClient(Persistance):

    def save(self):
        ...