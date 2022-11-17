"""Сложность данной функции O(n).
        Args:
            matrix (List[List[int]]): matrix where we search squares.
        Returns:
            int: amount of squares in matrix.
        """

from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        lst = []
        result = 0
        cur = 1
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                cur += 1
            else:
                lst.append(cur)
                cur = 1     
        lst.append(cur)
        for j in lst:
            result += ((1 + j)*j) // 2
            
        return result