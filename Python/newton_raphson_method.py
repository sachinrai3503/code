# https://leetcode.com/problems/valid-perfect-square/
# https://www.geeksforgeeks.org/program-for-newton-raphson-method
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

from lib2to3.pgen2.token import NOTEQUAL


# NOTE
"""
Below solution uses Newton Raphson method.

f(x) = x^2 - c
f`(x) = 2x # Derivative of f(x)

We would chose x1 = num//2, Tolerance = 1e-6 & iteration count = 50
Tolerance level is needed so that f`(x) doesn't becomes 0
Iteration count is needed to stop Oscillation between 2 points. eg - sqr root of 8
"""

class Solution:
    
    def fx(self, x, c):
        return x**2 - c

    def fdx(self, x):
        return 2*x
    
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        x = num/2
        prev = None
        TOL = 1e-6
        ITER_COUNT = 50
        f_dx = self.fdx(x)
        while i<ITER_COUNT and abs(f_dx)>TOL:
            # print(prev, x, f_dx)
            prev = x
            x = x - (self.fx(x, num)/f_dx)
            if prev==x: break
            f_dx = self.fdx(x)
            i+=1
        return (x-int(x))==0