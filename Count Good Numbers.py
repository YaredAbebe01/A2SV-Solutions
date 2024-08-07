class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7
        ev = (n + 1) // 2 
        od = n // 2   
        ans = (pow(5, ev, mod) * pow(4, od, mod)) % mod
        return ans
