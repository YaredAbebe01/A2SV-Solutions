class DataStream:
    def __init__(self, value, k):
        self.k = k
        self.val = value
        self.m = k
    def consec(self, num):
        if self.m > 0:
            self.m -= 1
            
        if num != self.val:
            self.m = self.k
        
        if self.m:
            return False
        return True
