class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        t = 0
        n = len(tickets)

        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    t += 1
                    if i == k and tickets[k] == 0:
                        return t
        
