class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        alpha = "abcdefghijklmnopqrstuvwxyz"
        r = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                r += alpha[int(s[i:i + 2]) - 1]
                i += 3
            else:
                r += alpha[int(s[i]) - 1]
                i += 1
        return r
