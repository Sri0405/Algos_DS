__author__ = 'sridhar'

class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        if A == []:
            return 0

        else:

            B =[0]*len(A)

            for i in range(len(A)):

                mul1 =1
                mul2 =1
                for k in range(0,i):
                    print k,"k"
                    mul1 *= A[k]

                for l in range(i+1,len(A)-1):
                    print l,"l"
                    mul2 *= A[l]

                B[i] =mul1 * mul2

                print B[i]
            print B

Solution().productExcludeItself([1,2,3])