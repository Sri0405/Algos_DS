__author__ = 'sridhar'


class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        end = len(nums) - 1
        start = 0
        while (end >= start):
            if nums[start] % 2 == 0 and nums[end] % 2 == 1:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
            elif nums[start] % 2 == 0 and nums[end] % 2 == 0:
                end -= 1
            elif nums[end] % 2 == 1 and nums[start] % 2 == 1:
                start += 1
            else:
                start +=1
                end -=1
        print nums

Solution().partitionArray([1,2,3,4])