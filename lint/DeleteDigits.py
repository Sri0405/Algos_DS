__author__ = 'sridhar'

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        ls = list(str(A))

        print int("".join(map(str,ls[:-k])))

Solution().DeleteDigits(12345,2)