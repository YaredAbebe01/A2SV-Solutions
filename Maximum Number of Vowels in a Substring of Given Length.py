class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vow = {'a', 'e', 'i', 'o', 'u'}
        maxc = 0
        curc = 0        
        for i in range(k):
            if s[i] in vow:
                curc += 1
        maxc = curc     
        for i in range(k, len(s)):
            if s[i] in vow:
                curc += 1
            if s[i - k] in vow:
                curc -= 1
            maxc = max(maxc, curc)
        return maxc
