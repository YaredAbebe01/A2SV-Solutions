class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if left < 2:
            left = 2
        prm = [True] * (right + 1)
        prm[0] = prm[1] = False
        p = 2
        while p * p <= right:
            if prm[p]:
                for multiple in range(p * p, right + 1, p):
                    prm[multiple] = False
            p += 1
        primes = [num for num in range(left, right + 1) if prm[num]]
        mdif = right - left + 1
        ans = [-1, -1]
        for i in range(len(primes) - 1):
            num1 = primes[i]
            num2 = primes[i + 1]
            dif = num2 - num1
            if dif < mdif:
                mdif = dif
                ans = [num1, num2]
        return ans
