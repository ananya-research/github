# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        nodes = []  # list of tuples: (col, row, val)

        # BFS with position tracking
        queue = deque([(root, 0, 0)])  # (node, row, col)

        while queue:
            node, row, col = queue.popleft()
            if node:
                nodes.append((col, row, node.val))
                queue.append((node.left, row+1, col-1))
                queue.append((node.right, row+1, col+1))

        # Sort by col, then row, then val
        nodes.sort()

        res = defaultdict(list)
        for col, row, val in nodes:
            res[col].append(val)

        return [res[x] for x in sorted(res)]