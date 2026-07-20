# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr,l2curr=list1,list2
        dummy=ListNode()
        curr=dummy

        while l1curr and l2curr:
            if l1curr.val<=l2curr.val:
                curr.next=l1curr
                curr=curr.next
                l1curr=l1curr.next

            else:
                curr.next=l2curr
                curr=curr.next
                l2curr=l2curr.next

        if l1curr:
            curr.next=l1curr
        else:
            curr.next=l2curr
        return dummy.next