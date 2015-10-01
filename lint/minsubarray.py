
class Solution:

    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here

        minsofar = nums[0]
        currsum = nums[0]

        for i in range(1, len(nums)):
            currsum = min(currsum + nums[i], nums[i])
            minsofar = min(minsofar, currsum)

        return minsofar
