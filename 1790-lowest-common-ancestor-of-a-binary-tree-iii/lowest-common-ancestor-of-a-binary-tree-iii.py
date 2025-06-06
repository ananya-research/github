"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        a, b = p, q

        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p

        return a

        # if p and q and p==q.parent:
        #     return p
        
        # elif p and q and q==p.parent:
        #     return q
        
        # elif p and q and p==q:
        #     return p
        
        # else:
        #     return self.lowestCommonAncestor(p.parent, q.parent)
        
        # return None

        