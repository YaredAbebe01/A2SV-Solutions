class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()   
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    if (i, num) in seen:
                        return False
                    seen.add((i, num))                
                    if (num, j) in seen:
                        return False
                    seen.add((num, j))
                    
                    b = (i // 3, j // 3)
                    if (b, num) in seen:
                        return False
                    seen.add((b, num))
        
        return True
