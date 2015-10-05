__author__ = 'sridhar'


def comparestrings(s, t):
    list1 = {}
    list2 = {}

    for i in s:
        list1[i]=list1.get(i,0)+1

    for i in t:
        list2[i]=list2.get(i,0)+1

    for key,val in list2.iteritems():
        if list1.__contains__(key) and list1.get(key)>=val:
           continue
        else:
            return False
    return True

s = "abcd"
t = "aabc"

print comparestrings(s, t)
