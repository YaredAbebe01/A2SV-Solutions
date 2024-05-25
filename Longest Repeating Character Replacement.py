class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        leng = 0
        count = [0] * 26
        start = 0
        maxc = 0
        
        for end, char in enumerate(s):
            index = ord(char) - ord('A')
            count[index] += 1
            maxc = max(maxc, count[index])
            
            if end - start + 1 - maxc > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            
            leng = max(leng, end - start + 1)
        
        return leng
