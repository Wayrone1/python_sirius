 """Сложность данной функции O((n+1)*(m+1))
        Args:
            obstacleGrid (List[List[int]]): grid which we should research.
        Returns:
            int: he number of possible unique paths that the robot can take to reach the bottom-right corner.
        """       


from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        d = [[0]*(col+1) for _ in range(row+1)]
            
        for i in range(1,row+1):
            for j in range(1,col+1):
                if i==1 and j==1:
                    d[i][j] = 1
                elif obstacleGrid[i-1][j-1] != 1:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        return d[-1][-1]
