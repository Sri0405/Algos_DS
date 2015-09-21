__author__ = 'sridhar'


def anagrams(strs):

    strs_c = {}

    if strs.__len__()!=0:
        for i in range(len(strs)):
            word = strs[i]
            print word
            if word != "" and word !=" ":
                strs_c[i] = ' '.join(sorted(word))

        indx = strs_c.values()[0]

        # print strs_c

        for i in range(1, strs_c.__len__()):
            if strs_c[i] == indx:
                common = strs_c[i]
                break
            else:
                indx = strs_c[i]

        common_lst = []

        for key, val in strs_c.iteritems():
            if val == common:
                common_lst.append(key)

        # print common_lst

        print list(common_lst)

strs = ["",""]

anagrams(strs)
