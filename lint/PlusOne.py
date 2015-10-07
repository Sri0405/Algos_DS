__author__ = 'sridhar'

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        string = "".join(map(str,digits))
        ans = int(string)+1
        lst = [int(i) for i in str(ans)]
        return lst

print Solution().plusOne([1,2,3])
