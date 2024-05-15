# Transpose Matrix

class Solution(object):
    def transpose(self, matrix):
        a=[]
        for i in range(len(matrix[0])):
            b=[]
            for j in range(len(matrix)):
                b.append(matrix[j][i])
            a.append(b)
        return a

sol=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
result=sol.transpose(matrix)
print(result)


 
