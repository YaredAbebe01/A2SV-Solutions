class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nor = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(nor) - 1
        while left < right:
            if nor[left] != nor[right]:
                return False
            left += 1
            right -= 1
        return True

        
