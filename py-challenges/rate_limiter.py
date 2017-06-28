import datetime
import time

class RateLimiter():
    
    req_queue = []
    rate_limit_rps = 5
    
    def get_access(self):
        # get current timestamp
        now = datetime.datetime.now().timestamp()
        # did we have already 'rate_limit_rps' requests in the last second
        counter = 0
        for timestamp in self.req_queue:
            if now -  timestamp < 1:
                counter+=1

        if (counter == self.rate_limit_rps):
            # exceeded limit, stopped
            return False
        else:
            self.req_queue.insert(0, now)
            if len(self.req_queue) > self.rate_limit_rps:
                self.req_queue.pop()
            return True

rate_limiter = RateLimiter()
for index in range (0,20):
    limited = rate_limiter.get_access()
    print("Request {} result: {}".format(index+1, limited))
    time.sleep(0.03)
print("Waiting now!")
time.sleep(2)
for index in range (0,20):
    limited = rate_limiter.get_access()
    print("Request {} result: {}".format(index, limited))