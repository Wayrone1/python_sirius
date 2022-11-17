    #    Сложность данной функции O(n*m).
    #     Args:
    #         matrix (List[List[int]]): matrix where we search squares.
    #     Returns:
    #         int: amount of squares in matrix.
        




from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
 
        count=matrix.count(1)
        count=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    count+=1
                if i==0 or j==0: continue
                
                old_val=matrix[i][j]
                matrix[i][j]=min(matrix[i-1][j-1], matrix[i][j-1],matrix[i-1][j]) + 1 if matrix[i][j]==1 else 0
                count= count+ matrix[i][j]- old_val  
        return count