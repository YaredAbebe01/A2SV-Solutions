class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter        
        ns, np = len(s), len(p)      
        pc = Counter(p)
        sc = Counter()    
        ans = []     
        for i in range(ns):
            sc[s[i]] += 1
            if i >= np:
                if sc[s[i - np]] == 1:
                    del sc[s[i - np]]
                else:
                    sc[s[i - np]] -= 1
            if pc == sc:
                ans.append(i - np + 1)
        
        return ans
        
