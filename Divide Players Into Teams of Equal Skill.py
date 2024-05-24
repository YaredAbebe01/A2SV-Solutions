class Solution(object):
    def dividePlayers(self, skill):

        n = len(skill)
        skill.sort() 
        t = 0    
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != skill[i + 1] + skill[n - i - 2]:
                return -1    
        for i in range(n // 2):
            t += skill[i] * skill[n - i - 1]   
        return t
