class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        csum = sum(nums[:k])
        maxs = csum   
        for i in range(k, len(nums)):
            csum += nums[i] - nums[i - k]   
            maxs = max(maxs, csum)    
        return maxs / float(k)
