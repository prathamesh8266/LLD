from algorithm import *
from typing import *
from enum import Enum

class Algo(Enum):
    
    FIXED_WINDOW = "fixed_window"
    SLIDING_WINDOW = "sliding_window"
    TOKEN_BUCKET = "token_bucket"
    
    
class RateLimiter:
    
    def __init__(self, algorithm: Algorithm = None, request_per_min: int = 60):
        self._request_per_min = request_per_min
        self._algorithm = algorithm
        self._algorithm_list = {
            Algo.FIXED_WINDOW : FixedWindow()
        }
        
    def setAlgo(self, algorithm: Algo) -> RateLimiter:
        if algorithm in self._algorithm_list:
            self._algorithm = self._algorithm_list[algorithm]
            self._algorithm.setMaxAllowedRequests(self._request_per_min)
            return self
        else:
            raise Exception("Invalid Algorithm")
        
    def isValidIp(self, ip: str):
        return self._algorithm.isValid(ip)
    