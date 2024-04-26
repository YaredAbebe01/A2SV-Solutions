class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        p = strs[0]
        for ch in strs[1:]:
            while ch[:len(p)] != p:
                p = p[:-1]
                if not p:
                    return ""
        return p

            
