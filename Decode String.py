class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur = 0
        st = ""
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char == '[':
                stack.append((st, cur))
                st = ""
                cur = 0
            elif char == ']':
                last_string, num = stack.pop()
                st = last_string + st * num
            else:
                st += char
        
        return st
