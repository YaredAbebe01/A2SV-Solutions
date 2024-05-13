class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        ans=0
        piles.sort()
        for i in range(len(piles)/3):
            piles.pop()
            ans+=piles[-1]
            piles.pop()
        return ans


        
