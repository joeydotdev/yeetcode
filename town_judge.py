"""
	
	if town judge exist:
		all nodes point point to it
		town judge has no outgoing edges


	build adjacency list:
		iterate through each key
			if key has len of 0 and all other nodes point to key
				return key

		return -1

	
	{1: set()}
"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
    	adjacency_list = {}
    	for i in range(1, N+1):
    		adjacency_list[i] = set([])

    	def all_other_nodes_point_to(k):
    		nonlocal adjacency_list
    		for i in adjacency_list:
    			if i == k:
    				continue
    			if k not in adjacency_list[i]:
    				return False

    		return True

    	for t in trust:
    		node, outgoing = t
    		adjacency_list[node].add(outgoing)

		for k in adjacency_list:
			if len(adjacency_list[k]) == 0 and all_other_nodes_point_to(k):
				return k

		return -1