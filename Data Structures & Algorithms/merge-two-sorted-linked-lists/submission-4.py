# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2=list1,list2
        newN=ListNode(0)
        head=newN
        while h1 and h2:
            if h1.val<h2.val:
                head.next=h1
                h1=h1.next
            else:
                head.next=h2
                h2=h2.next
            head=head.next
        if h1:
            head.next=h1
        elif h2:
            head.next=h2
        return newN.next
                

