class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize the deque with a maximum size of k.
        :type k: int
        """
        self.k = k
        self.size = 0
        self.deque = [0] * k
        self.front = 0
        self.rear = -1

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.deque[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self):
        """
        Returns the front item from the Deque. Returns -1 if the deque is empty.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """
        Returns the last item from Deque. Returns -1 if the deque is empty.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self):
        """
        Returns true if the deque is empty, or false otherwise.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Returns true if the deque is full, or false otherwise.
        :rtype: bool
        """
        return self.size == self.k
