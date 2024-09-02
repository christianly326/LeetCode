# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = first
        while second.next:
            first = first.next
            second = second.next
            if second.next:
                second = second.next
        return first
# Intial thought process was two have two pointers one will iterate twice as fast as the other one
# At first I coded it assuming there was always going to be at least 2 jumps the second pointer can make
# Then I accounted for if it couldn't make two jumps
# Then I returned the first pointer as it would be the 'middle' of the linked list
# Space complexity O(1)
# Time complexity O(n)