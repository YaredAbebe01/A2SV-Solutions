class Solution(object):
    def addSpaces(self, s, spaces):
        ans = []
        space = 0
        numsp = len(spaces)
        
        for i in range(len(s)):
            if space < numsp and i == spaces[space]:
                ans.append(' ')
                space += 1
            ans.append(s[i])
        
        return ''.join(ans)

            
