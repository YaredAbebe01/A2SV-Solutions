class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mArea = 0
        left, right = 0, len(height) - 1

        while left < right:
            cArea = min(height[left], height[right]) * (right - left)
            mArea = max(mArea, cArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mArea
        
