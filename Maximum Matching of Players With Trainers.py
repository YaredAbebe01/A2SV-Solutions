class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        match = 0
        use = [False] * len(trainers)

        for player in players:
            for j, trainer in enumerate(trainers):
                if not use[j] and player <= trainer:
                    match += 1
                    use[j] = True
                    break

        return match
