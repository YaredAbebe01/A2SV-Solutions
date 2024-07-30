class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        csum = 0
        msum = 0
        seen = set()

        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                csum -= nums[left]
                left += 1

            seen.add(nums[right])
            csum += nums[right]
            msum = max(msum, csum)
        return msum
