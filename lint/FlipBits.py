__author__ = 'sridhar'


class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        if a == b:
            return 0

        bits = a^b
        count =0

        num =32
        while(num>0):
            count += bits &1
            bits = bits>>1
            num-=1

        print count

Solution().bitSwapRequired(-2147483648, 2147483647)
Solution().bitSwapRequired(1, -1)
Solution().bitSwapRequired(-2147483648, -1)
