
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        sr = sorted(deck)
        i = deque(range(n))
        ans = [0] * n
        for card in sr:
            ans[i.popleft()] = card
            if i:
                i.append(i.popleft())
        
        return ans
