class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here

        M = len(A)
        N = len(B)
        
        if A == " " or B == " " or A == B:
            return 0
            
        res = [[0 for i in range(M + 1)] for j in range(N + 1)]
        
        maxl =0 
        for i in range(1, M+1 ):
            
            for j in range(1, N+1 ):
            
                if A[i - 1] == B[j - 1]:
                
                    res[i][j] = res[i - 1][j - 1] + 1
                    maxl = max(res[i][j],maxl)
                else:
                
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])
        
        return maxl
        
           