# https://leetcode.com/problems/valid-perfect-square/
# https://www.geeksforgeeks.org/program-for-bisection-method/
"""
Given a positive integer num, write a function which returns True if num is a
 perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1
"""

# Note
"""
We can use bisection method as - 

Given num>0
Equation - f(x, num) = x^2 - num = 0
Possible bisection range = [a, b] = [0, num] because
    - f(0,num)*f(num,num)<0
    - f(x, num) is continuous in [a,b]
"""

class Solution:
    
    def fx(self, x, num):
        return x**2 - num
    
    # This is simple bisection method based solution
    def isPerfectSquare(self, num: int) -> bool:
        a, b = 0, num
        while a<=b:
            mid = a + (b-a)//2
            f_mid = self.fx(mid, num)
            f_a = self.fx(a, num)
            f_a_mid = f_mid*f_a
            # print(a, b, mid, f_a, f_mid, f_a_mid)
            if f_mid == 0: return True
            if f_a_mid==0: return True # root is a 
            elif f_a_mid<0: b = mid-1
            else: a = mid+1
        return False
    
    
    def isPerfectSquare1(self, num: int) -> bool:
        a, b = 0, num
        while a<=b:
            mid = a + (b-a)//2
            mid_sqr = mid**2
            # print(a, b, mid, mid_sqr)
            if mid_sqr==num: return True
            if mid_sqr<num: a = mid+1
            else: b = mid-1
        return False