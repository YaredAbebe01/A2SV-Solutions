class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        st = sorted((j[0], i) for i, j in enumerate(intervals))
        ans = []
        for j in intervals:
            end = j[1]
            l, r = 0, len(st) - 1
            while l < r:
                mid = (l + r) // 2
                if st[mid][0] < end:
                    l = mid + 1
                else:
                    r = mid
            
            if st[l][0] >= end:
                ans.append(st[l][1])
            else:
                ans.append(-1)
        
        return ans
