# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            # Post-order: compute left/right subtree first
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Add the absolute values of imbalance from children
            self.moves += abs(left) + abs(right)
            
            # Return the net excess coins for this subtree
            return node.val + left + right - 1
        
        dfs(root)
        return self.moves
        