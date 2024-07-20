class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sotrh = ListNode(0)
        cur = head
        while cur:
            prev = sotrh
            nextn = sotrh.next
            while nextn:
                if nextn.val >= cur.val:
                    break
                prev = nextn
                nextn = nextn.next
            temp = cur.next
            cur.next = nextn
            prev.next = cur
            cur = temp 
        return sotrh.next
