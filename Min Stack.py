class MinStack(object):
    def __init__(self):
        """
        Initialize the stack.
        """
        self.stack = []
        self.ms = []
        
    def push(self, val):
        """
        Push element val onto the stack.
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.ms:
            self.ms.append(val)
        else:
            self.ms.append(min(val, self.ms[-1]))
    
    def pop(self):
        """
        Remove the element on the top of the stack.
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.ms.pop()
    
    def top(self):
        """
        Get the top element of the stack.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
    
    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        :rtype: int
        """
        if self.ms:
            return self.ms[-1]

# Example usage:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin()) # return -3
# obj.pop()
# print(obj.top())    # return 0
# print(obj.getMin()) # return -2
