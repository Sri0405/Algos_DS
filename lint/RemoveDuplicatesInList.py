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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        temp = head
        if temp is None or temp.next is None:
            return temp
        else:
            while(temp is not None or temp.next is not None):
                if temp.val == temp.next.val:
                    temp.next=temp.next.next
                else:
                    temp =temp.next

        return  head

