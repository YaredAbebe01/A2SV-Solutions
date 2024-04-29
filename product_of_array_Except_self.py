class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        lp = 1
        for i in range(n):
            ans[i] *= lp
            lp *= nums[i]
        rp = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= rp
            rp *= nums[i]

        return ans
