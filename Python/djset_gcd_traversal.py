# https://leetcode.com/problems/greatest-common-divisor-traversal
"""
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse 
 between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of
 traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

Example 1:
Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to 
 index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 
 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, 
 to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.

Example 2:
Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.

Example 3:
Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), 
 and (2, 3). A valid sequence of traversals exists for each pair, so we return true.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

from typing import List
from math import sqrt

class DJSet:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj: return
        pi_rank = self.rank[pi]
        pj_rank = self.rank[pj]
        if pi_rank>pj_rank:
            self.parent[pj] = pi
        elif pi_rank<pj_rank:
            self.parent[pi] = pj
        else:
            self.parent[pj] = pi
            self.rank[pi]+=1

class Solution:

    def gcd(self, i, j):
        while j!=0:
            temp = i
            i = j
            j = temp%j
        return i

    # Will time out
    def canTraverseAllPairs1(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        dj_set = DJSet(nums_len)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                gcd_ij = self.gcd(nums[i], nums[j])
                # print(f'{nums[i]=} {nums[j]=} {gcd_ij=}')
                if gcd_ij>1:
                    dj_set.union(i, j)
        # print(f"{dj_set.parent=}")
        # print(f"{dj_set.rank=}")
        root_count = 0
        for i in range(nums_len):
            if dj_set.find_parent(i)!=root:
                root_count+=1
                if root_count>1: return False
        return True
    
    def get_all_factors(self, num):
        factors = set()
        a = 1
        b = sqrt(num)
        while a<=b:
            if (num%a)==0:
                factors.add(a)
                factors.add(num//a)
            a+=1
        # print(f'{num=} {factors=}')
        return factors

    # This will also time out
    def canTraverseAllPairs2(self, nums: List[int]) -> bool:
        factors_map = dict()
        unique_nums = list()
        for num in nums:
            if num not in factors_map:
                factors_map[num] = self.get_all_factors(num)
                unique_nums.append(num)
        # if 1 in factors_map: return False # Fails for [1]
        unique_nums_len = len(unique_nums)
        dj_set = DJSet(unique_nums_len)
        for i in range(unique_nums_len):
            num_i_factors = factors_map.get(unique_nums[i])
            for j in range(unique_nums_len):
                num_j_factors = factors_map.get(unique_nums[j])
                if num_i_factors.intersection(num_j_factors)!={1}:
                    dj_set.union(i, j)
        # print(f"{dj_set.parent=}")
        # print(f"{dj_set.rank=}")
        root_count = 0
        for i in range(unique_nums_len):
            if dj_set.find_parent(i)!=root:
                root_count+=1
                if root_count>1: return False
        return True
    
    # This is slow
    def canTraverseAllPairs3(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        factors_map = dict()
        for num in nums:
            if num not in factors_map:
                factors_map[num] = self.get_all_factors(num)
        first_occ_of_factor = dict()
        dj_set = DJSet(nums_len)
        for i in range(nums_len):
            for factor in factors_map.get(nums[i]):
                if factor==1: continue
                if factor not in first_occ_of_factor:
                    first_occ_of_factor[factor] = i
                else:
                    dj_set.union(i, first_occ_of_factor[factor])
                    # first_occ_of_factor[factor] = i # Works when last occ is used also
        # print(f'{first_occ_of_factor=}')
        # print(f"{dj_set.parent=}")
        # print(f"{dj_set.rank=}")
        root_count = 0
        for i in range(nums_len):
            if dj_set.find_parent(i)==i:
                root_count+=1
                if root_count>1: return False
        return True
    
    # Will return an arr of size n where arr[i] = largest prime factor for i
    def get_largest_prime_factor_for(self, n):
        op = [0 for _ in range(n+1)]
        for i in range(2, n+1):
            if op[i]==0:
                for j in range(i, n+1, i):
                    op[j] = i
        return op
    
    def get_prime_factors(self, sieve, num):
        if num in self.num_factors_map: return self.num_factors_map[num]
        prime_factors = list()
        i = num
        while i>1:
            prime_factor = sieve[i]
            prime_factors.append(prime_factor)
            while i % prime_factor == 0:
                i//=prime_factor
        self.num_factors_map[num] = prime_factors
        return prime_factors

    # This will use Eratosthenes Sieve method to find all the prime factors only for a number
    # Refer - https://www.geeksforgeeks.org/sieve-of-eratosthenes/ for finding prime number till small range
    # Below uses similar technique to find the prime factors directly
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        max_num = max(nums)
        prime_factors = self.get_largest_prime_factor_for(max_num)
        # print(f'{prime_factors=}')
        dj_set = DJSet(nums_len)
        self.num_factors_map = dict()
        prime_factor_1st_index = dict()
        for i in range(nums_len):
            num = nums[i]
            pfs = self.get_prime_factors(prime_factors, num)
            # print(f'{num=} PF = {pfs=}')
            for num_prime_factor in pfs:
                if num_prime_factor not in prime_factor_1st_index:
                    prime_factor_1st_index[num_prime_factor] = i
                else:
                    dj_set.union(i, prime_factor_1st_index[num_prime_factor])
        # print(f'{self.num_factors_map=}')
        # print(f'{prime_factor_1st_index=}')
        root_count = 0
        for i in range(nums_len):
            if dj_set.find_parent(i)==i:
                root_count+=1
                if root_count>1: return False
        return True