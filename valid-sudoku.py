class Solution(object):
    def isValidSudoku(self, board):
                
        for i in range(len(board)):
            hash = {}
            for j in range(len(board[i])):
                if board[i][j]!="." and board[i][j] in hash:
                    return False
                else:
                    hash[board[i][j]] = 1
                
                
        for i in range(len(board[0])):
            hash = {}
            for j in range(len(board)):
                if board[j][i]!="." and board[j][i] in hash:
                    return False
                else:
                    hash[board[j][i]] = 1        
        
        for a in range(3):
            for b in range(3):
                hash = {}
                for i in range(a*3, (a+1)*3):
                    for j in range(b*3, (b+1)*3):
                        if board[i][j]!="." and board[i][j] in hash:
                            return False
                        else:
                            hash[board[i][j]] = 1
        return True
