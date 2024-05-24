class Solution(object):
    def partitionLabels(self, s):
        las = {char: i for i, char in enumerate(s)}
        par = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, las[char])

            if i == end:
                par.append(end - start + 1)
                start = i + 1

        return par
            
