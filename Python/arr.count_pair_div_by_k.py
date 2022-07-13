# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
"""
Given a 0-indexed integer array nums of length n and an integer k, return the number 
 of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.

Example 1:
Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    

Example 2:
Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^5
"""

from math import sqrt
from collections import Counter

class Solution:
    
    def get_all_factors(self, num):
        factors = dict()
        for i in range(1, int(sqrt(num))+1):
            # print(i)
            if num%i==0:
                factors[i] = 0
                if i!=(num//i): factors[num//i] = 0
        # print(factors)
        return factors
    
    def gcd(self, a, b):
        # print(a,b)
        if b==0: return a
        return self.gcd(b, a%b)
    
    # Will take lot of time
    def countPairs1(self, nums: list[int], k: int) -> int:
        count = 0
        factors = self.get_all_factors(k)
        for num in nums:
            _gcd = self.gcd(num, k)
            count+=factors.get(k//_gcd)
            for factor in factors:
                if num%factor==0: factors[factor]+=1
            # print(factors)
        return count

    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        gcd_cnt = Counter(self.gcd(num,k) for num in nums)
        # print(gcd_cnt)
        for a in gcd_cnt:
            for b in gcd_cnt:
                if a<=b and a*b%k==0:
                    count+=(gcd_cnt[a]*gcd_cnt[b]) if a!=b else gcd_cnt[a]*(gcd_cnt[a]-1)//2
        return count