__author__ = 'sridhar'
"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current.next:
            if current.next.val>current.val:
                pre = dummy
                while pre.next.val <current.next.val:
                    pre = pre.next
                temp = current.next
                current.next = temp.next
                temp.next=pre.next
                pre.next = temp
            else:
                current = current.next
        return dummy.next