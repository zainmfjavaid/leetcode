# Problem 2: Add Two Numbers
# Solution Runtime: 67ms (beats 46.7%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_l1 = l1
        current_l2 = l2
        linked1 = []
        linked2 = []
        
        while current_l1:
            linked1.append(current_l1.val)
            current_l1 = current_l1.next
        while current_l2:
            linked2.append(current_l2.val)
            current_l2 = current_l2.next
            
        list1_int_form = int(''.join(reversed([str(x) for x in linked1])))
        list2_int_form = int(''.join(reversed([str(x) for x in linked2])))
        
        list_form = [int(x) for x in str(list1_int_form + list2_int_form)]
        
        last_node = None
        for i, value in enumerate(list_form):
            if not last_node:
                last_node = ListNode(value, None)
            else:
                last_node = ListNode(value, last_node)
        return last_node