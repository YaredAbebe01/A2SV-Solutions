class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = False
        i = 0
        while True:
            if 3 ** i == n:
                ans = True
                break
            elif 3 ** i > n:
                break
            i += 1
        return ans
