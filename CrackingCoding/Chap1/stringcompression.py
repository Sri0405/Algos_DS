
class Solution(object):

    def compress(self, inp):
        string_in = (inp)
        last_seen = string_in[0]
        count = 1
        result = ""

        for i in range(1, len(string_in)):
            if string_in[i] == last_seen:
                count += 1
            else:
                result += last_seen + str(count)
                last_seen = string_in[i]
                count = 1
        result += last_seen + str(count)
        print result

test = Solution()
test.compress('aabbbcccad')
