class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        seen = {}
        mind = float('inf')

        for i, card in enumerate(cards):
            if card in seen:
                mind = min(mind, i - seen[card] + 1)
            seen[card] = i
        return mind if mind != float('inf') else -1
