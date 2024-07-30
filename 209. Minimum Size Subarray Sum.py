class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        curs = 0
        mlen = float('inf')

        for right in range(n):
            curs += nums[right]

            while curs >= target:
                mlen = min(mlen, right - left + 1)
                curs -= nums[left]
                left += 1

        return mlen if mlen != float('inf') else 0
