# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head

        size=1
        while curr.next:
            curr=curr.next
            size+=1
        curr=head
        
        index=size-n
        print(size,index)
        if index==0:
            return head.next
        for i in range(1,index):
            print(i,curr.val)
            curr=curr.next
            print(i,curr.val)
        curr.next=curr.next.next 
        return head