import math

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        # write your code here

            C = [a*b for a,b in zip(A,B)]
            
            if A ==[] or B==[] or sum(A) ==0 or sum(B) ==0:
                return 2
            A2 = [a*b for a,b in zip(A,A)]
            B2 = [a*b for a,b in zip(B,B)]

            if A2 ==0 or B2 == 0:
                return 2
            else:
                return sum(C) /math.sqrt(sum(A2) * sum(B2))