class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedn=sorted(nums)
        ans=[]
        for x in nums:
           ans.append(sortedn.index(x))
        return ans
        
