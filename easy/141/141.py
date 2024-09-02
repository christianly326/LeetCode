# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        table = {}
        pos = 0
        current = head
        while current:
            if current.next in table:
                return True
            table[current] = pos
            pos += 1
            current = current.next
        return False