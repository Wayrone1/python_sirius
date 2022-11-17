    #    Сложность данной функции O(n*m).
    #     Args:
    #         matrix (List[List[int]]): matrix where we search squares.
    #     Returns:
    #         int: amount of squares in matrix.


from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        dp = [[0]*(col+1) for _ in range(row+1)]
            
        for i in range(1,row+1):
            for j in range(1,col+1):
                if i==1 and j==1:
                    dp[i][j] = 1
                elif obstacleGrid[i-1][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]