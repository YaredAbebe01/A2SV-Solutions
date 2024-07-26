class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = sum(nums)
        left = 0
        
        for i, num in enumerate(nums):
            right = tot - left - num
            if left == right:
                return i
            left += num
        
        return -1
