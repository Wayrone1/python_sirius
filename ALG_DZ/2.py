# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Сложность алгоритма равна o(n)

class Solution(object):
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        current  = head
        result = length = 0
        while current .next:
            length += 1
            current  = current .next
        current  = head
        while current :
            if current .val == 1:
                result += 2 ** length
            length -= 1
            current  = current .next
        return result