# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head.next
        while fast and fast.next and slow!=fast:
            slow=slow.next
            fast=fast.next.next
        return True if slow==fast else False