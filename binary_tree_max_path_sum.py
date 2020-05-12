# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
    	nodes = {}
    	if root is None:
    		return 0

    	def build_parents(node, parent):
    		if node is None:
    			return
    		nodes[node] = parent
    		build_parents(node.left, node)
    		build_parents(node.right, node)

    	build_parents(root, None)	

    	def find_max_sum(node, cur_sum):
    		if node is None:
    			return sum

    		left = find_max_sum(node.left, cur_sum + node.val)	
    		right = find_max_sum(node.right, cur_sum + node.val)

    		l_r_max = max(left, right)

    		if node not in nodes or nodes[node] is None:
    			return l_r_max
    		return max(l_r_max, find_max_sum(nodes[node]))

    	return find_max_sum(root, 0)
