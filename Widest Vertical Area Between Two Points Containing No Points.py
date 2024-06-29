class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x = [point[0] for point in points]
        x.sort()
        wid = 0
        for i in range(1, len(x)):
            wid = max(wid, x[i] - x[i - 1])
        return wid
