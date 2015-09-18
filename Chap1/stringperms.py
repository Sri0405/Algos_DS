
class Solution(object):
	def checkstrings(self,str1,str2):
		str1 = sorted(str1)
		str2 = sorted(str2)

		if str1 == str2:
			print True
		else:			
			print False

test = Solution()
test.checkstrings("test1","test1")