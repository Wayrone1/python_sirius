"""Сложность данной функции O(n)
        Args:
            nums (List[int]): representation of houses which we should rob.
        Returns:
            int: the maximum money which we can steal 
            """
from typing import List
class Solution :
     def rob(self, nums: List[int]) -> int: 
        if len(nums) < 2 :
            return max(nums)
        
        def max_rob(j) :
            max_rob = 0
            robber1 = robber2 = 0
            for i in range(j, len(nums) -1+j) :
                max_rob = max(robber2, nums[i] + robber1)
                robber1, robber2 = robber2, max_rob
            return max_rob
        max_robber1 = max_rob(0)        
        max_robber2 = max_rob(1)     

        return max(max_robber1, max_robber2)    
