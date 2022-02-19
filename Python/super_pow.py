# https://leetcode.com/problems/super-pow/
"""
Your task is to calculate ab mod 1337 where a is a positive integer and b
 is an extremely large positive integer given in the form of an array.

Example 1:
Input: a = 2, b = [3]
Output: 8

Example 2:
Input: a = 2, b = [1,0]
Output: 1024

Example 3:
Input: a = 1, b = [4,3,3,8,5,2]
Output: 1

Constraints:
1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b does not contain leading zeros.
"""

class Solution:
    
    def __init__(self):
        self.pow_dict = dict()
        
    def findPow(self, x: float, n: int) -> float:
        if n in self.pow_dict: return self.pow_dict[n]
        result = None
        if n==0: result = 1
        elif n==1: result = x
        elif x==0.0: result = 0
        else:
            t_n = n//2
            rem = n%2
            f_tn = self.findPow(x, t_n)
            print(x, n, t_n, f_tn, rem)
            result = f_tn*f_tn*(x if rem==1 else 1)
        self.pow_dict[n] = result
        return result
    
    # This times out
    def superPow1(self, a: int, b: list[int]) -> int:
        result = 1
        length = len(b)
        k = 1
        for i in range(length):
            result*=self.findPow(a, b[length-1-i]*k)
            print(self.pow_dict)
            k*=10
        return result%1337
    
    def to_int(self, b):
        b_int = 0
        for t_b in b:
            b_int = b_int*10 + t_b
        return b_int

    # https://just4once.gitbooks.io/leetcode-notes/content/leetcode/math/372-super-pow.html
    def superPow(self, a:int, b:list[int]) -> int:
        b = self.to_int(b)
        m = 1337
        phi = 1140
        a = a%m
        if a==0: return 0
        b = b%phi
        if b==0: b = phi
        return (a**b)%m
