__author__ = 'sridhar'


class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0

    def binarySearch(self, nums, target):
        # write your code here
        first = 0
        len_list = len(nums)
        last = len_list - 1

        print last

        while first <= last:
            mid = (last + first) / 2
            if nums[mid] == target:
                while mid >= 0 and nums[mid-1] == nums[mid]: mid -= 1
                return mid
            else:
                if nums[mid] < target:
                    first = mid + 1
                else:
                    last = mid - 1

        return -1


test = Solution()
print test.binarySearch([1, 4, 4, 5, 7, 7, 8, 9, 9, 10], 1)

