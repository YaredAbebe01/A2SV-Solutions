class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur['next']
        return cur['val']

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newn = {'val': val, 'next': self.head}
        self.head = newn
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newn = {'val': val, 'next': None}
        if not self.head:
            self.head = newn
        else:
            cur = self.head
            while cur['next']:
                cur = cur['next']
            cur['next'] = newn
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        else:
            newn = {'val': val, 'next': None}
            cur = self.head
            for _ in range(index - 1):
                cur = cur['next']
            newn['next'] = cur['next']
            cur['next'] = newn
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head['next']
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur['next']
            cur['next'] = cur['next']['next']
        self.size -= 1
