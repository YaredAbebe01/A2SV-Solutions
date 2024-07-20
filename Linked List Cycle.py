# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        sl = head
        ft = head.next
        
        while sl != ft:
            if not ft or not ft.next:
                return False
            sl = sl.next
            ft = ft.next.next
        
        return True
