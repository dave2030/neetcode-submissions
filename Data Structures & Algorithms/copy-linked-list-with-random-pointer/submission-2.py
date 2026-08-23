"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        newH={}
        if not head: return head
        while curr:
            newH[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            copy=newH[curr]
            copy.random=newH.get(curr.random)
            copy.next=newH.get(curr.next)
            curr=curr.next
        return newH[head]