
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sl = head
        fa = head
        
        while fa and fa.next:
            sl = sl.next
            fa = fa.next.next
        
        return sl

