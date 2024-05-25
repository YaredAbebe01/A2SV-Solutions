class Solution(object):
    def removeDuplicateLetters(self, s):
        stack = []
        count = {char: s.count(char) for char in set(s)}
        vis = set()
        for char in s:
            count[char] -= 1
            if char in vis:
                continue
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                vis.remove(stack.pop())
            stack.append(char)
            vis.add(char)
        
        return ''.join(stack)
