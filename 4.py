from typing import List

class Solution:
    """Сложность данной функции O(n*m).
        Args:
            matrix (List[List[int]]): matrix where we search squares.
        Returns:
            int: amount of squares in matrix.
        """
    def maxProfit(self, prices: List[int]) -> int:
        # Инициализируйте максимальную прибыль
        maximumProfit = 0
        # Пройдите весь элемент через цикл
        for i in range(1, len(prices)):
            # проверьте, больше ли цена на i
            if prices[i] > prices[i-1]:
                # Добавьте разницу к прибыли и увеличьте ее
                maximumProfit += prices[i] - prices[i-1]
        return maximumProfit        # Верните максимальную прибыль