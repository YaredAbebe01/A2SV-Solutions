class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        n = len(blocks)
        op = float('inf')
        cur = 0
        for i in range(k):
            if blocks[i] == 'W':
                cur += 1
        op = cur
        for i in range(k, n):
            if blocks[i] == 'W':
                cur += 1
            if blocks[i - k] == 'W':
                cur -= 1
            op = min(op, cur)
        
        return op
