# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque

        if root is None:
            return []

        queue=deque([root])

        rightMost=[]

        while queue:
            n=len(queue)

            for i in range(n):

                node=queue.popleft()

                if i==n-1:
                    rightMost.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)



        return rightMost
        