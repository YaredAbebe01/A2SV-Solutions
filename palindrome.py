class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        c = x
        pal = True
        rev = 0       
        if x < 0:
            pal = False       
        while x > 0:
            temp = x % 10
            rev = rev * 10 + temp
            x //= 10        
        if c != rev:
            pal = False           
        return pal
