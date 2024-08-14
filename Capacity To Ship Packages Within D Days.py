class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            tot = 0
            day = 1
            
            for weight in weights:
                tot += weight
                if tot > mid:
                    day += 1
                    tot = weight
                    if day > days:
                        break
            
            if day > days:
                l = mid + 1
            else:
                r = mid
        
        return l
