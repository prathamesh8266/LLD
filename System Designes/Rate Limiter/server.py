
class Server:
    
    def __init__(self, name):
        self._name = name
    
    def call(self, ip: str):
        print(f"IP: {ip} processed by server: {self._name}")
        