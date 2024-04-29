class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        i = 0
        for j in range(3):
            while count[j] > 0:
                nums[i] = j
                i += 1
                count[j] -= 1
