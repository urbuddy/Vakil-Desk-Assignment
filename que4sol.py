"""A RateLimiter class in python that limits the number of
requests a user can make within a given time window"""
import time
import threading

class RateLimiter:
    """
    Class RateLimiter class that limits the number of
    requests a user can make within a given time window
    """
    def __init__(self, max_requests, time_window):
        """
        Constructor
        :param max_requests: Maximum number of requests allowed in the time window
        :param time_window: Time window in seconds (e.g., 60 seconds for 1 minute)
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}
        self.lock = threading.Lock()

    def allow_request(self, user_id):
        """
        Function to that limits the number of requests a user can make within a given time window
        :param user_id: user id
        :return: Boolean value that reflects request true: request allowed or false: request rejected
        """
        current_time = time.time()

        with self.lock:
            if user_id not in self.requests:
                self.requests[user_id] = []

            valid_requests = [req_time for req_time in self.requests[user_id] if current_time - req_time < self.time_window]
            self.requests[user_id] = valid_requests

            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            else:
                return False

# Example
if __name__ == "__main__":
    rate_limiter = RateLimiter(max_requests=5, time_window=60)
    user_id = "user_123"
    for i in range(7):
        allowed = rate_limiter.allow_request(user_id)
        print(f"Request {i + 1}: {'Allowed' if allowed else 'Rejected'}")
        time.sleep(5)
