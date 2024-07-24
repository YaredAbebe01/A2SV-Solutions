class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            gcd = nums[i]
            for j in range(i, n):
                a, b = gcd, nums[j]
                while b != 0:
                    a, b = b, a % b
                gcd = a   
                if gcd == k:
                    count += 1
                elif gcd < k:
                    break
        
        return count
