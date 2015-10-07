__author__ = 'sridhar'

import sys

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here

        flag =0
        if n < 0:
            flag = 1
            n = -n
            string = str(n)
        else:
            string =str(n)

        rev= int(string[::-1])
        nmbr =0
        if flag:
            nmbr= -rev
        else:
            nmbr= rev

        if abs(nmbr) >2147483647:
            return 0
        else:
            return nmbr


print Solution().reverseInteger(-100)
