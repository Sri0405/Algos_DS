class Solution(object):
	def checkrot(self,str1,str2):
		string_new = str1+str1
		len1 = len(str1)
		len2 = len(str2)
		if len1==len2 and len1>0:
			if str2 in string_new:
				print True
			else:
				print False
		else:
			print False


test = Solution()
test.checkrot('waterbottle','eebottlewat')