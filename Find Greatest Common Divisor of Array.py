class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s = nums[0]
        l = nums[-1]
        for i in range(s, 0, -1):
            if l % i == 0 and s % i == 0:
                return i
        return 1
