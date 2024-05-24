class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        match = 0
        pptr = 0
        tptr = 0

        while pptr < len(players) and tptr < len(trainers):
            if players[pptr] <= trainers[tptr]:
                match += 1
                pptr += 1
                tptr += 1
            else:
                tptr += 1
        return match
