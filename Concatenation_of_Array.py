class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [] 
        for i in range(2):  
            for j in range(len(nums)): 
                ans.append(nums[j])  
        return ans      
