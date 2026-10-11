from server import *
from ratelimiter import *
from user import *

class Gateway:
    
    def __init__(self, rateLimiter: RateLimiter = None, server: Server = None):
        self._rateLimiter = rateLimiter
        self._server = server
        
    def addRateLimiter(self, rateLimiter: RateLimiter) -> Gateway:
        self._rateLimiter = rateLimiter
        return self
        
    def addServer(self, server: Server) -> Gateway:
        self._server = server
        return self
        
    def request(self, user: User):
        
        ip = user.getip()
        if self._rateLimiter.isValidIp(ip):
            self._server.call(ip)
        else:
            print(f"Request with IP {ip} dropped")
        
