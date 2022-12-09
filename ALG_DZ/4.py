#Сложность алгоритма равна o(n*m)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0: return 0
        col=len(grid[0])
         
        def isl(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i > 0:   isl(i-1, j)
                if i < row-1: isl(i+1, j)
                if j > 0:   isl(i, j-1)
                if j < col-1: isl(i, j+1)
                    
        count = 0 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    isl(i, j)
        return count 