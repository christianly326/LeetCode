# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        link = ListNode(0, head)
        current = link
        while current and current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next
        return link.next
# Space Complextiy O(n)
# Time Complexity O(n + m)