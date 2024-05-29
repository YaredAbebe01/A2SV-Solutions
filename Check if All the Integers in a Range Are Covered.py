class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        cov = set()
        
        for start, end in ranges:
            cov.update(range(start, end + 1))        
        for num in range(left, right + 1):
            if num not in cov:
                return False
        
        return True
        
