# https://www.lintcode.com/problem/281
"""
You want to build yourself a house. The building company you hired can 
 only build houses with sides from their specific set ss. That means
 they can build you a square house or a rectangular one but if and
 only if its length and width belong to the sets.

This month, they have a special promotion: they will paint the ceiling
 of a new house for free... but only if its area is not more than a.

You want them to do it for free but you also want to be sure that the
 house will be comfortable and not too small. How many possible house
 configurations can you create to have the ceiling painted for free given
 the side lengths offered?

There is a method to how the company decides what lengths of sides to produce.
 To determine n lengths of wall segments to offer, they start with a seed value s0,
 some variables k, b and m, and use the following equation to determine all other 
 side lengths si:
 
 s[i]= ((k*prev + b)%m + 1 + prev) for all 1<=i<n and prev = s[i-1]
    
Example 1
Input:
s0 = 2
n = 3
k = 3
b = 3
m = 2
a = 15
Output: 5 as s=[2,4,6]

Constraints-
1<=n<=6*10^6
1<=si<=10^9
1<=k,b,m<=10^9
1<=a<=10^18
"""

class Solution:

    def binary_search(self, dp, s, e, a):
        t_s = s
        _floor = s-1
        n1 = dp[s]
        while s<=e:
            mid = s + (e-s)//2
            if n1*dp[mid]<=a:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor - t_s + 1

    """
    @param s0: the number s[0]
    @param n: the number n
    @param k: the number k
    @param b: the number b
    @param m: the number m
    @param a: area
    @return: the way can paint the ceiling
    """
    # This will timeout - O(nlog(n))
    def paintthe_ceiling_1(self, s0: int, n: int, k: int, b: int, m: int, a: int) -> int:
        count = 0
        dp = [0 for i in range(n)]
        dp[0] = s0
        for i in range(1, n):
            dp[i] = dp[i-1] + 1 + (k*dp[i-1] + b)%m
        print(f'{dp=}')
        for i in range(n):
            t_count = self.binary_search(dp, i, n-1, a)
            # print(f"{t_count=}")
            if t_count: count+=(2*t_count - 1)
            else: break
        return count

    def paintthe_ceiling(self, s0: int, n: int, k: int, b: int, m: int, a: int) -> int:
        if s0*s0>a: return 0
        count = 1
        j = 0
        dp = [s0]
        for i in range(1, n):
            dp.append(dp[-1] + 1 + (k*dp[-1]+b)%m)
            while j>=0 and dp[j]*dp[-1]>a:
                j-=1
            if j<0: break
            count+=((j+1)*2)
            if dp[-1]**2<=a: 
                count+=1
                j = i
        return count