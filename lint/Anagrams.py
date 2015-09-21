__author__ = 'sridhar'


def anagram(s, t):
    if (len(s) != len(t)):
        return False
    else:
        count1 = [0] * 256
        count2 = [0] * 256

        for i in s:
            count1[ord(i)] += 1

        for i in t:
            count2[ord(i)] += 1

        if count1 == count2:
            return True
        else:
            return False


s = "abcd"
t = "dcax"

print anagram(s, t)
