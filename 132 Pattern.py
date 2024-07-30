class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        stack = []
        i = float('-inf')
        for num in reversed(nums):
            if num < i:
                return True
            while stack and stack[-1] < num:
                i = stack.pop()
            stack.append(num)
        return False
