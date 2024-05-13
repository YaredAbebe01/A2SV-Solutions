class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        con=0
        for w in range (len(words)):
            for m in range(len(words)):
                if w!=m:
                    s1=set(words[w])
                    s2=set(words[m])
                    if s1==s2:
                        con+=1

        return con/2

