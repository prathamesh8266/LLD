from abc import ABC, abstractmethod
import time
import threading
from collections import deque

class Algorithm(ABC):
    
    @abstractmethod
    def isValid(self, ip: str):
        pass
    
    @abstractmethod
    def setMaxAllowedRequests(self, max_allowed_requests: int) -> FixedWindow:
        pass
    

class FixedWindow(Algorithm):
    
    def __init__(self):
        self._counter = {} # stores k:ip , v:(last_request_window_id, count)
        self._window_duration = 60
        self._max_allowed_requests = None
        self._lock = threading.Lock()
        
    def setMaxAllowedRequests(self, max_allowed_requests: int) -> Algorithm:
        if max_allowed_requests < 1:
            raise Exception("Max allowed requests should be > 1")
            
        self._max_allowed_requests = max_allowed_requests
        return self
    
    
    def isValid(self, ip: str):
        
        if self._max_allowed_requests is None:
            raise Exception("Max allowed requests not configured")
        
        with self._lock:
            window_id = int(time.time() // self._window_duration)
            if ip in self._counter:
                last_request_window_id = self._counter[ip][0]
                request_count_in_window = self._counter[ip][1]

                if last_request_window_id == window_id:
                    if self._max_allowed_requests > request_count_in_window:
                        self._counter[ip] = (window_id, request_count_in_window+1)
                    else:
                        return False
                else:
                    self._counter[ip] = (window_id, 1)
            else:
                self._counter[ip] = (window_id, 1)
            
        return True
    

class RollingWindowLog(Algorithm):
    
    def __init__(self):
        self._request_counter = {}
        self._window_duration = 60
        self._max_allowed_requests = None
        self._lock = threading.Lock()
                
                
    def setMaxAllowedRequests(self, max_allowed_requests: int) -> Algorithm:
        if max_allowed_requests < 1:
            raise Exception("Max allowed requests should be > 1")
            
        self._max_allowed_requests = max_allowed_requests
        return self
    
    
    def isValid(self, ip: str):
    
        if self._max_allowed_requests is None:
            raise Exception("Max allowed requests not configured")
        
        with self._lock:
            if ip in self._request_counter:
                now = time.time()
                while len(self._request_counter[ip]) > 0 and now - self._request_counter[ip][0] >= self._window_duration:
                    self._request_counter[ip].popleft()
                if len(self._request_counter[ip]) < self._max_allowed_requests:
                    self._request_counter[ip].append(now)
                else:
                    return False
            else:
                self._request_counter[ip] = deque([time.time()])
                
        return True
        
        
        