"""
Definition of ListNode
"""


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        else:
            head = ListNode(0)
            if l1.val < l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next

            temp = head
            while l1 is not None or l2 is not None:
                if l1 is None:
                    temp.next = l2
                    return head
                if l2 is None:
                    temp.next = l1
                    return head

                else:
                    if l1.val < l2.val:
                        temp.next = l1
                        temp = temp.next
                        l1 = l1.next
                    else:
                        temp.next = l2
                        temp = temp.next
                        l2 = l2.next
        return head
