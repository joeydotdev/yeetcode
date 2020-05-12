import collections

class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    	if root is None:
    		return True

    	q = collections.deque()
    	# [Node, Parent]
    	q.append([root, None])

    	"""
    		q: [
				[4, 2]
				[5, 3]
    		]
			size: 2
    		found_x = [False, None]
    		found_y = [False, None]
    		node = 4, parent = 2

    	"""
    	while len(q) > 0:
    		size = len(q)
    		found_x = [False, None]
    		found_y = [False, None]
    		for i in range(size):
	    		node, parent = q.popleft()
	    		print("PROCESSING NODE " + str(node.val))
	    		if node.val == x:
	    			found_x[0] = True
	    			found_x[1] = parent
	    		if node.val == y:
	    			found_y[0] = True
	    			found_y[1] = True
	    		if found_x[0] and found_y[0]:
	    			return found_x[1] != found_y[1]
	    		if node.left is not None:
		    		q.append([node.left, node])
		    	if node.right is not None:
		    		q.append([node.right, node])

    		found_x = [False, None]
    		found_y = [False, None]


    	return False	