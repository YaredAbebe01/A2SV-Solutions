class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        
        ans = []
        for num in arr2:
            if num in freq:
                ans.extend([num] * freq[num])
                del freq[num]
        for num in sorted(freq.keys()):
            ans.extend([num] * freq[num])
        
        return ans
