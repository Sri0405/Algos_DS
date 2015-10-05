__author__ = 'sridhar'


class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """

    def hashCode(self, key, HASH_SIZE):
        l = list(key)
        length = l.__len__()
        power = length
        res = 0
        for i in range(length):
            res =res*33 + ord(l[i])
            res = res % HASH_SIZE
            power -=1

        print res

Solution().hashCode("abcd",100)