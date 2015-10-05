__author__ = 'sridhar'


class Solution:
    # @param A: An integers list.
    # @return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        # target element prop = A[P] > A[P-1] && A[P] > A[P+1]

        low = 0
        high = len(A) - 1

        while (low <= high):
            mid = low + (high - low) / 2
            if (mid == 0 or A[mid] >= A[mid - 1]) and (mid == len(A) - 1 or A[mid] >= A[mid + 1]):
                return mid
            elif mid > 0 and A[mid] > A[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1


print Solution().findPeak([1, 2, 1, 3, 4, 5, 7, 6])
