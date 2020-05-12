# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
	3 -> 2 -> 0 -> 4
	               s
	               f

"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    	if head is None or head.next is None:
    		return False
    	slow = head
    	fast = head

    	while slow and fast and fast.next:
    		slow = slow.next
    		fast = fast.next.next
    		if slow == fast:
    			return True

    	return False
