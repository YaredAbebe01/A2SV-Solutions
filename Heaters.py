class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        rad = 0
        
        for house in houses:
            left, right = 0, len(heaters) - 1
            
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            
            dist1 = abs(house - heaters[left])
            dist2 = abs(house - heaters[left - 1]) if left > 0 else float('inf')
            dis = min(dist1, dist2)
            rad = max(rad, dis)
        return rad
