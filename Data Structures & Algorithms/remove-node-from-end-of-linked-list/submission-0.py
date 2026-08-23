# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        dummy=ListNode(0,head)
        tmp=dummy
        p=None
        while n>0:
            curr=curr.next
            n-=1

        while curr:
            tmp=tmp.next
            curr=curr.next
        tmp.next=tmp.next.next
        return dummy.next

            
        
        