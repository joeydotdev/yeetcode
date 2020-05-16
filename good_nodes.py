"""

    we care about the maximum value up to a node
        - only one path to get to a node

    map<node, int> - the maximum value seen to get to this node
        - to save on space we could just pass in a func arg that contains the max val in the recursion, but either way we would be using linear memory bc of call stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # lookup = {}

        # def populate(node: TreeNode, parent: TreeNode):
        #     if node is None:
        #         return

        #     if parent is not None:
        #         max_val_to_this_point = max(node.val, lookup[parent])
        #     else:
        #         max_val_to_this_point = node.val
            
        #     lookup[node] = max_val_to_this_point
        #     populate(node.left, node)
        #     populate(node.right, node)

        def count(node: TreeNode, max_val: int):
            num = 0
            if node is None:
                return num
            if node.val >= max_val:
                num += 1

            max_val_to_this_point = max(node.val, max_val)
            num += count(node.left, max_val_to_this_point) + count(node.right, max_val_to_this_point)
            return num

        if root is None:
            return 0

        # populate(root, None)
        return count(root, root.val)