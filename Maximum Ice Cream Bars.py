class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        maxc = max(costs)
        count = [0] * (maxc + 1)
        for cost in costs:
            count[cost] += 1
        bar = 0
        for i in range(1, maxc + 1):
            if coins >= i:
                num = min(count[i], coins // i)
                bar += num
                coins -= num * i
            else:
                break
        return bar
        
