# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Сложность алгоритма равна o(n*m)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
   
        if not root:
            return 0
        q = [root]
        result = [root.val]

        while q:
            size = len(q)
            lst = []
            while size:
                front = q.pop(0)
                size-=1

                if front.left:
                    q.append(front.left)
                    lst+=[front.left.val]
                if front.right:
                    q.append(front.right)
                    lst+=[front.right.val]
            if lst:
                avg = sum(lst)/len(lst)
                result.append(avg)

        return result