__author__ = 'sridhar'

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here

        if len(nums) ==0:
            return None
        elif len(nums) ==1:
            return nums[0]
        else:
            maj_elem = 0
            count =1
            for i in range(len(nums)):
                if nums[i]==nums[maj_elem]:
                    count+=1
                else:
                    count -=1
                if count ==0:
                    maj_elem =i
                    count =1

            majorty = nums[maj_elem]
            res_c =0
            for i in nums:
                if majorty ==i:
                    res_c+=1
                if res_c >=(len(nums)/2):
                    return majorty

print Solution().majorityNumber([2, 2, 3, 5, 2, 2, 6])