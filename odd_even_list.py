"""
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL


i = 1

odd_list_head = Node()
even_list_head = Node()

while cur:
    if i % 2 ==
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def print_list(self, head: ListNode):
        print("------------")
        while head:
            print(head.val)
            head = head.next
            
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        odd_list_head = ListNode()
        odd_list_cur = odd_list_head

        even_list_head = ListNode()
        even_list_cur = odd_list_head

        i = 1
        cur = head

        while cur:
            self.print_list(odd_list_head)
            if i % 2 == 0:
                # even
                even_list_cur.next = cur
                even_list_cur = even_list_cur.next
            else:
                # odd
                odd_list_cur.next = cur
                odd_list_cur = odd_list_cur.next
            
            cur = cur.next
            i += 1

        odd_list_cur.next = even_list_head.next
        
        return odd_list_head.next