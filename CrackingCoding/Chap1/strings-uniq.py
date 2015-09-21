
class Solution(object):
	def StringUniq(self,inp):
		strn_inp = sorted(inp)
		last_char = strn_inp[0]
		flag = True
		for i in range(1,len(strn_inp)):
			if strn_inp[i]==last_char:
				flag = False
			else:
				last_char = strn_inp[i]
		print flag

test =Solution()
test.StringUniq("2341")
