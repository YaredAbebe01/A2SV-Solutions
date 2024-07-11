class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1count = [0] * 26
        for char in s1:
            s1count[ord(char) - ord('a')] += 1
        windc = [0] * 26
        for char in s2[:len1]:
            windc[ord(char) - ord('a')] += 1
        if windc == s1count:
            return True
        for i in range(len1, len2):
            windc[ord(s2[i]) - ord('a')] += 1
            windc[ord(s2[i - len1]) - ord('a')] -= 1
            if windc == s1count:
                return True
        return False
