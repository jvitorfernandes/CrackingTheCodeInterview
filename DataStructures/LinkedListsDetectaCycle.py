"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

sawyou = []
def has_cycle(head):
    
    if(head is None or head.next is None):
        return False
    
    fast = head.next.next
    
    while(fast != None and fast.next != None):
        fast = fast.next.next
        head = head.next
        
        if(fast == head):
            return True
        
        return False
        