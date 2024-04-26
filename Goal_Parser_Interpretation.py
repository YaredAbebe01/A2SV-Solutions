class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        count = 0
        newn = []
        i = 0
        while i < len(command):
            if command[i].isalpha():
                newn.append(command[i])
                count += 1
            elif command[i] == '(' and not command[i + 1].isalpha():
                newn.append("o")
                i += 1 
                count += 1
            i += 1

        return ''.join(newn)
        
