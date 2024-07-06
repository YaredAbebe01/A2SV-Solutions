class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        op = 0
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in nums:
            if freq[num] > 0:
                comp = k - num
                if comp in freq and freq[comp] > 0:
                    if num == comp:
                        op += freq[num] // 2
                        freq[num] = 0
                    else:
                        pairs = min(freq[num], freq[comp])
                        op += pairs
                        freq[num] -= pairs
                        freq[comp] -= pairs
        return op
        
