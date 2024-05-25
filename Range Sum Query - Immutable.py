class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.presum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.presum[i + 1] = self.presum[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.presum[right + 1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
