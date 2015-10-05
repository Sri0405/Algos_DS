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
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        # write your code here
        slow = head
        fast = head

        if fast != None:
            fast = fast.next

        while fast != None:
            slow = slow.next

            if fast.next != None:
                fast = fast.next.next
            else:
                return False

            if slow is fast:
                return True

        return False
