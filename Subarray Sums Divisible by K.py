class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        psum = 0
        count = 0
        remc = {0: 1} 
        for num in nums:
            psum += num
            rem = psum % k
            if rem < 0:
                rem += k
            if rem in remc:
                count += remc[rem]
                remc[rem] += 1
            else:
                remc[rem] = 1
        return count
