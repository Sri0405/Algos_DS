__author__ = 'sridhar'


class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        n = n - 1
        m = m - 1
        end = len(A) - 1
        while (end >= 0):
            print m, n
            if n >= 0 and m>=0:
                if A[m] > B[n]:
                    A[end] = A[m]
                    m -= 1
                else:
                    A[end] = B[n]
                    n -= 1
            elif m < 0 and n >= 0:
                A[end] = B[n]
                n -= 1
            elif m>=0 and n<0:
                A[end] = A[m]
                m -= 1

            end -= 1



Solution().mergeSortedArray([9, 10, 11, 12, 13, None, None, None, None], 5, [4, 5, 6, 7], 4)
