# Problem 21: Merge Two Sorted Lists
# Solution Runtime: 41ms (beats 73.0%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    current_node = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            current_node.next = list1
            list1, current_node = list1.next, list1
        else:
            current_node.next = list2
            list2, current_node = list2.next, list2

    if list1 or list2:
        current_node.next = list1 if list1 else list2
    
    return dummy.next