__author__ = 'sridhar'


class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):

        res = [1 for i in range(len(A))]
        res1 = [1 for i in range(len(A))]

        for i in range(1, len(A)):
            last = len(A) - i
            # print i , last
            if A[i] < A[i - 1]:
                res[i] =res[i-1]+ 1
            if A[last-1] < A[last ]:
                res1[i] =res1[i-1]+ 1

        return max((max(res),max(res1)))


print Solution().longestIncreasingContinuousSubsequence([5,4,2,1,3])
