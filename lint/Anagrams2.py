__author__ = 'sridhar'

def anagrams(strs):

        d = dict()
        for str in strs:
            sortstr = ''.join(sorted(str))
            d[sortstr] = [str] if sortstr not in d else d[sortstr] + [str]

        res = []
        for str in d:
            if len(d[str]) >= 2:
                res += d[str]
        return res

print anagrams(["lint", "intl", "inlt", "code"])