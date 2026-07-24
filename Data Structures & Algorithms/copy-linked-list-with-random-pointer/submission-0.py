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
        oldToCopy={None:None}

        curr=head
        while curr:
            copy=Node(curr.val)
            oldToCopy[curr]=copy

            print("Val:",curr.val)
            print("Next Val:", curr.next.val) if curr.next else print("Next Val: None")
            print("Random Val:", curr.random.val) if curr.random else print("Random Val: None")
            curr=curr.next
            print("\n")


        curr=head
        while curr:
            copy=oldToCopy[curr]
            copy.next=oldToCopy[curr.next]
            copy.random=oldToCopy[curr.random]
            curr=curr.next
        
        return oldToCopy[head]