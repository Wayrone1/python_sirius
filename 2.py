from typing import List
class Solution:
    """Сложность данной функции O(n*m).
        Args:
            matrix (List[List[int]]): matrix where we search squares.
        Returns:
            int: amount of squares in matrix.
        """
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def goal(arr, i,j,k,count):  # мне нужно вернуть count (после обновления), поэтому моя рекурсивная функция должна возвращать count
            if i>=row or j>= col:
                return 0
            if arr[i][j]==1:  #препятствие отсюда, возвращение
                return 0
            if i==row-1 and j==col-1:   #цель достигнута, увеличьте количество на 1
                count+=1
                return count
				# поскольку мы будем двигаться либо вниз, либо вправо
                # , мы не столкнемся с какой-либо проблемой зацикливания в этой задаче
            if (i,j) not in k:   #чтобы избежать повторного вычисления ранее посещенных путей
                count = goal(arr,i+1,j,k,count)+goal(arr, i,j+1,k,count)
                k[(i,j)] = count
            return k[(i,j)]
        return goal(grid, 0,0,{}, 0)
		