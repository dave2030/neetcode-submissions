# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq={}

        cur=head
        while cur:
            freq[cur.val]= 1 + freq.get(cur.val,0)
            cur=cur.next
        dummy=ListNode(0,head)
        cur=head
        prev=dummy
        while cur:
            if freq[cur.val]>1:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return dummy.next
