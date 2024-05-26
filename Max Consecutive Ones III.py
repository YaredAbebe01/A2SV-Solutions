class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
                """
        left = 0
        mlen = 0
        count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            
            mlen = max(mlen, right - left + 1)
        
        return mlen
