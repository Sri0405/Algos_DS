__author__ = 'sridhar'

class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        maximum = len(nums)
        print max(nums)
        res = 0
        for i in range(maximum+1):
            res = res ^ i
        for i in nums:
            res = res ^ i

        print res

