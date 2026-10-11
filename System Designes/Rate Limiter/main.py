from algorithm import *
from user import *
from gateway import *
from server import *
    

if __name__ == "__main__":
    
    userA = User('111.111.111')
    userB = User('222.222.222') 
    
    rate_limiter = RateLimiter(request_per_min= 30).setAlgo(Algo.FIXED_WINDOW)
    gateway = Gateway().addRateLimiter(rate_limiter).addServer(Server('A'))
    
    for i in range(40):
        gateway.request(userA)
        gateway.request(userB)