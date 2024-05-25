class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sumset = {0: 1}
        
        csum = 0
        
        for num in nums:
            csum += num
            if csum - k in sumset:
                count += sumset[csum - k]     
            sumset[csum] = sumset.get(csum, 0) + 1

        return count
