# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        nxt=slow.next
        slow.next=None
        slow=nxt
        prev, curr= None, slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        curr, nxt2=head, None
        while prev:
            nxtcurr=curr.next
            curr.next=prev
            curr=nxtcurr

            nxtprev=prev.next
            prev.next=curr
            prev=nxtprev