__author__ = 'sridhar'

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here

        curr = head
        prev = None

        while curr is not None:
            nnext = curr.next
            curr.next = prev
            prev =curr
            curr =nnext

        return prev