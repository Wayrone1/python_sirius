
    """Сложность данной функции O(n+1)
        Args:
            n (int): list's length.
        Returns:
            int: max element in this list.
        """     
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        gen = [0] * (n+1)
        if len(gen) >= 2:
            gen[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                gen[i] = gen[i //2]
            else:
                gen[i] = gen[i//2] + gen[i//2 + 1]
        return max(gen)        
