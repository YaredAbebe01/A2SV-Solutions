class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for n in range(len(nums)-1):
            if nums[n]== nums[n+1]:
                p=nums[n]*2
                ans.append(p)
                nums[n+1]=0
            else:
                ans.append(nums[n])
            if n==len(nums)-2:
                ans.append(nums[-1])
        ans1=[n for n in ans if n!=0]+[0]*(ans.count(0))
        return ans1
        
