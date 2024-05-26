class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mrg = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        
        while i < len1 or j < len2:
            if word1[i:] >= word2[j:]:
                mrg.append(word1[i])
                i += 1
            else:
                mrg.append(word2[j])
                j += 1 
        return ''.join(mrg)
            
