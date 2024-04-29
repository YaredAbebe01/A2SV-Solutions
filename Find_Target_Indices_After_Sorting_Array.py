class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        nums.sort()
        for i in nums:
            if(target in nums):
                x=(nums.index(target))
                ans.append(x)
                nums[x]=target-1
        return (ans)
            
        
