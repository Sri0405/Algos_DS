class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """

    def partition(self, head, x):
        # write your code here
        head1 = ListNode(0)
        head2 = ListNode(0)
        temp = head
        phead1 = head1
        phead2 = head2

        while (temp):
            if temp.val < x:
                phead1.next = temp
                temp = temp.next
                phead1 = phead1.next
                phead1.next = None

            else:
                phead2.next = temp
                temp = temp.next
                phead2 = phead2.next
                phead2.next = None

        phead1.next = head2.next

        return head1.next
