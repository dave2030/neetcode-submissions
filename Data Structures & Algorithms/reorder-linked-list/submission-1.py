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
        slow.next=None
        p=None
        while nxt:
            tmp=nxt.next
            nxt.next=p
            p=nxt
            nxt=tmp
        first,second=head,p
        while second:
            t1,t2=first.next,second.next
            first.next=second
            second.next=t1
            first,second=t1,t2


        