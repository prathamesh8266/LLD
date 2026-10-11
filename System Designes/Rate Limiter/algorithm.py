from abc import ABC, abstractmethod
import time
import threading

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
                