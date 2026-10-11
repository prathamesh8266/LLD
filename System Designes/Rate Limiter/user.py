

class User:
    
    def __init__(self, ip: str):
        self._ip = ip
        
    def getip(self):
        return self._ip