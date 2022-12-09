#Сложность алгоритма равна o(n*m)


class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		nums = 0
		row, col = len(grid),len(grid[0])
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1:
					nums += 4
					if 0<=i-1<row and grid[i-1][j] == 1:
						nums -= 1
					if 0<=i+1<row and grid[i+1][j] == 1:
						nums -= 1
					if 0<=j-1<col and grid[i][j-1] == 1:
						nums -= 1
					if 0<=j+1<col and grid[i][j+1] == 1:
						nums -= 1
		return nums