class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.sort(key=lambda x: int(x[-1]))
        w = [word[:-1] for word in words]
        sen = ' '.join(w)
        return sen
