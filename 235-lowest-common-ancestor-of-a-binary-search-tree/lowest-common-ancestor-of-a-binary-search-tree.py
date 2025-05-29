# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca=[root]

        def search(root):
            if not root:
                return
            lca[0]=root
            value=root.val
            if value< p.val and value<q.val:
                search(root.right)
            elif value>p.val and value>q.val:
                search(root.left)
            else:
                return
        
        search(root)
        return lca[0]




        

        