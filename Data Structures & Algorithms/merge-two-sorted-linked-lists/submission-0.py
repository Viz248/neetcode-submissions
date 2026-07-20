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

        while l1curr or l2curr:
            if not l1curr:
                curr.next=l2curr
                return dummy.next

            elif not l2curr:
                curr.next=l1curr
                return dummy.next

            elif l1curr.val<=l2curr.val:
                curr.next=l1curr
                curr=curr.next
                l1curr=l1curr.next

            else:
                curr.next=l2curr
                curr=curr.next
                l2curr=l2curr.next
        return None