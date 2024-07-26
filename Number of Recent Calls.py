class RecentCounter(object):

    def __init__(self):
        self.req = deque()
    def ping(self, t):
        self.req.append(t)
        while self.req and self.req[0] < t - 3000:
            self.req.popleft()
        return len(self.req)
