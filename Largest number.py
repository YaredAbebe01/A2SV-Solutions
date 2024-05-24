class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums_str = [str(num) for num in nums]
        n = len(nums_str)
        for i in range(n):
            for j in range(0,n-i-1):
                if compare(nums_str[j], nums_str[j+1]) > 0:
                    nums_str[j], nums_str[j+1] = nums_str[j+1], nums_str[j]
        lnum = ''.join(nums_str)
        if lnum[0] == '0':
            return '0'
        else:
            return lnum
