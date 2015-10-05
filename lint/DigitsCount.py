__author__ = 'sridhar'


class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        res = 0
        for i in range(n + 1):
            string = str(i)
            string =list(string)
            print string
            res += string.count(str(k))

        return res


Solution().digitCounts(1,12)