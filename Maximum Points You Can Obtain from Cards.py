class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        tot = sum(cardPoints)
        size = n - k
        mins = float('inf')
        cur = 0
        for i in range(size):
            cur += cardPoints[i]
        mins = cur
        for i in range(size, n):
            cur += cardPoints[i] - cardPoints[i - size]
            mins = min(mins, cur)
        return tot - mins
