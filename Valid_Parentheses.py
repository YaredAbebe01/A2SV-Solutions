class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if not stack or not self.isMatch(stack[-1], c):
                    return False
                stack.pop()

        return not stack

    def isMatch(self, left, right):
        return (left == '(' and right == ')') or (left == '{' and right == '}') or (left == '[' and right == ']')
