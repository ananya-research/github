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
        
        # if not head: return None

        # cur=head
        # old_to_new={}

        # while cur:
        #     node=Node(x=cur.val)
        #     old_to_new[cur]=node
        #     cur=cur.next

        # cur=head

        # while cur:
        #     new_node=old_to_new[cur]
        #     new_node.next=old_to_new[cur.next] if cur.next else None
        #     new_node.random=old_to_new[cur.random] if cur.random else None
        #     cur=cur.next
        
        # return old_to_new[head]



        if not head:
            return None
        
        curr=head
        old_to_new={}

        while curr:
            node=Node(x=curr.val)
            old_to_new[curr]=node
            curr=curr.next
        
        curr=head
        while curr:
            node=old_to_new[curr]
            node.next=old_to_new[curr.next] if curr.next else None
            node.random=old_to_new[curr.random] if curr.random else None
            curr=curr.next
        
        return old_to_new[head]
        