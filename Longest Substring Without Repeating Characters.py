class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = {}
        leng = 0
        st = 0
        
        for i in range(len(s)):
            if s[i] in ind and ind[s[i]] >= st:
    
                st = ind[s[i]] + 1

            ind[s[i]] = i

            leng = max(leng, i - st + 1)
        
        return leng

        
