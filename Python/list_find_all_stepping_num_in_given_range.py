# https://www.geeksforgeeks.org/stepping-numbers/
# https://www.interviewbit.com/problems/stepping-numbers/
"""
Given two integers ‘n’ and ‘m’, find all the stepping numbers in range [n, m].
A number is called stepping number if all adjacent digits have an absolute
 difference of 1. 321 is a Stepping Number while 421 is not.

Examples :

Input : n = 0, m = 21
Output : 0 1 2 3 4 5 6 7 8 9 10 12 21

Input : n = 10, m = 15
Output : 10, 12
"""

class Solution:
	
	def find_step_num(self, a, b, num, prev, op):
	    if num>b: return
	    if num>=a and num<=b: op.append(num)
	    if prev==-1:
	        for i in range(1,10):
	            self.find_step_num(a,b,i,i,op)
	    else:
	        if prev!=0:
	            self.find_step_num(a,b,num*10+prev-1,prev-1,op)
	        if prev!=9:
	            self.find_step_num(a,b,num*10+prev+1,prev+1,op)
	# @param A : integer
	# @param B : integer
	# @return a list of integers
	def stepnum(self, A, B):
	    op = list()
	    self.find_step_num(A,B,0,-1,op)
	    op.sort()
	    return op
        