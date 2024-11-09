class Solution(object):
    def rotate(self, matrix):
        for i in range((len(matrix)+1)//2):
            for j in range((len(matrix))//2):
                matrix[i][j],matrix[j][len(matrix)-1-i], matrix[len(matrix)-1-i][len(matrix)-1-j], matrix[len(matrix)-1-j][i]=matrix[len(matrix)-1-j][i], matrix[i][j], matrix[j][len(matrix)-1-i], matrix[len(matrix)-1-i][len(matrix)-1-j]

