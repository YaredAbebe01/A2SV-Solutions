class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lh = ListNode(0)
        gh = ListNode(0)
        l = lh
        g = gh 
        cur = head
        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                g.next = cur
                g = g.next
            cur = cur.next
        g.next = None
        l.next = gh.next
        return lh.next
