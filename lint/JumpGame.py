class Solution:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      class Solution:
	
	def canJump(self,A):
		if len(A)==0 or len(A)==1:
			return False
		else:
			self.ComputeJump(A,0,A[0],len(A)-1)

	def ComputeJump(self,A,presentpos,maxJump,target):
		if presentpos>target:
			return False
		
		for i in range(1,maxJump+1):
			if i+presentpos == target:
				return True
			if self.ComputeJump(A,presentpos+i,A[i+presentpos],target):
				return True	

		return False

Solution().canJump([0,8,2,0,9])
