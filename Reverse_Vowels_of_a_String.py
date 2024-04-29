class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        for char in s:
            if char.lower() in "aeiou":
                vowels.append(char)
        
        result = []
        for char in s:
            if char.lower() in "aeiou":
                result.append(vowels.pop())
            else:
                result.append(char)
        
        return ''.join(result)
