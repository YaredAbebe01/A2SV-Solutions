class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        c = {}
        winners = set()
        for winner, loser in matches:
            if loser in c:
                c[loser] += 1
            else:
                c[loser] = 1
            
            if winner not in c:
                c[winner] = 0    
            winners.add(winner)
        n = [player for player in winners if c[player] == 0]
        j = [player for player, count in c.items() if count == 1]
        n.sort()
        j.sort()
        
        return [n, j]
