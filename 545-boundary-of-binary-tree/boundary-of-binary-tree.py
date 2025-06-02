# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        def isLeaf(node):
            return node and not node.left and not node.right

        boundary = []

        # 1. Root
        if not isLeaf(root):
            boundary.append(root.val)

        # 2. Left boundary (excluding leaves & root)
        def addLeft(node):
            while node:
                if not isLeaf(node):
                    boundary.append(node.val)
                node = node.left if node.left else node.right

        # 3. Leaves (left to right)
        def addLeaves(node):
            if isLeaf(node):
                boundary.append(node.val)
                return
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)

        # 4. Right boundary (excluding leaves & root, reversed)
        def addRight(node):
            stack = []
            while node:
                if not isLeaf(node):
                    stack.append(node.val)
                node = node.right if node.right else node.left
            while stack:
                boundary.append(stack.pop())

        if root.left:
            addLeft(root.left)
        addLeaves(root)
        if root.right:
            addRight(root.right)

        return boundary
        