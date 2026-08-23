# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        nxt=slow.next
        prev=None
        slow.next=None
        while nxt:
            tmp=nxt.next
            nxt.next=prev
            prev=nxt
            nxt=tmp
        s1=head
        s2=prev
        while s2:
            n1,n2=s1.next,s2.next
            s1.next=s2
            s2.next=n1
            s1=n1
            s2=n2
