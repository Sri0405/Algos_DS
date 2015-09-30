class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        
		m = len(A)
		n = len(B)

		if m ==0 or n ==0:
			return 0

		res = [[0 for i in range(n+1)] for k in range(m+1)]
		length =0

		for i in range(1,m+1):
			for j in range(1,n+1):

				if A[i-1]==B[j-1]:
					res[i][j]=res[i-1][j-1]+1
					length= max(res[i][j],length)
				else:
					res[i][j]=0
					length = max(0,length)

		return length
