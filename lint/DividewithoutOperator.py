
# correct overflow
class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result

    def divide(self, dividend, divisor):
        # Write your code here
        denom = divisor
        current = 1
        ans = 0
        flag = False

        if divisor == 1:
            return dividend

        if dividend < 0 and divisor > 0:
            flag = True

        if dividend > 0 and divisor < 0:
            flag = True

        # print flag

        if abs(dividend) >= 2147483647:
            return 2147483647

        dividend = abs(dividend)
        divisor = abs(divisor)

        if denom > dividend:
            return 0

        if dividend == divisor:
            if flag:
                return -1
            return 1

        while (denom <= dividend):
            denom <<= 1
            current <<= 1

        denom >>= 1
        current >>= 1

        while current != 0:
            if dividend >= denom:
                dividend -= denom
                ans |= current

            current >>= 1
            denom >>= 1

        if flag is True:
            return -ans
        return ans

print Solution().divide(0, -1)