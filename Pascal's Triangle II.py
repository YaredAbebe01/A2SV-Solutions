class Solution(object):
    def getRow(self, rowIndex) :
        if rowIndex == 0:
            return [1]  
        init = [1]
        while rowIndex > 0:
            temp = []
            for i in range(len(init) + 1):
                if i == 0 or i == len(init):
                    temp.append(1)
                else:
                    temp.append(init[i - 1] + init[i])
            init = temp
            rowIndex -= 1
        
        return init
