__author__ = 'sridhar'


class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here

        x = 0
        y = 1

        if n ==1:
            return x
        if n==2:
            return y

        while (n - 2 > 0):
            val = x + y
            x = y
            y = val
            n -= 1

        print val


Solution().fibonacci(10)