"""Сложность данной функции O(n)."""

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
       
        pr = len(prices)
        d = [1]*pr
        f = 1
        for i in range(1, pr):
            if prices[i-1]-prices[i] == 1:
                d[i] = d[i-1]+1
            f += d[i]
        return f
