class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [-1] * n  # Initialize the answer array with -1
        stack = []  # Stack to store the indices of the elements
        
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                answer[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        
        return answer
