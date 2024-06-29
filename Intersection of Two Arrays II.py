class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        fre = {}
        for num in nums1:
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
        ans = []
        for num in nums2:
            if num in fre and fre[num] > 0:
                ans.append(num)
                fre[num] -= 1 
        return ans
