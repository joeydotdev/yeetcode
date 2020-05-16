"""
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        def dfs(node, level):
            nonlocal max_depth
            if node is None:
                return level - 1
            
            max_depth = max(max_depth, level)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 1)
        return max_depth
        