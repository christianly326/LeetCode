# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def digiter(self, l1: Optional[ListNode]) -> int:
        n = 0
        count = 0
        curr = l1
        while curr:
            n += curr.val * (10 ** count)
            count += 1
            curr = curr.next
        return n
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        n = self.digiter(l1)
        m = self.digiter(l2)
        r = n + m
        while r > 0:
            val = r % 10
            curr.val = val
            
            r //= 10
            if r > 0:
                curr.next = ListNode()
                curr = curr.next
        return dummy
# Time Complexity O(n) where n is the bigger linked list
# Space Complexity O(n) where n is the bigger linked list
