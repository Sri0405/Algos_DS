__author__ = 'sridhar'

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x ==1:
            return 1
        low = 0.
        high =x
        nm = (low+high)/2.0
        while(abs(nm**2-x)>0.001):
            if nm**2<x:
                low = nm
            else:
                high =nm
            nm = low+(high-low)/2.0
        return int(nm)

Solution().sqrt(3)
