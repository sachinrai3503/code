# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray
 that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""

class Solution:
    
    def search_for_k_len_subarr(self, nums1, nums1_len, nums2, nums2_len, k):
        hash_set = set()
        d = 101 # no. of char in char set
        h = d**(k-1)
        hash1 = 0
        for i in range(nums1_len):
            hash1 = hash1*d + nums1[i] # Here not using mod to keep it simple
            if i>=(k-1):
                hash_set.add(hash1)
                hash1 = hash1 - nums1[i-(k-1)]*h
        # print(hash_set, k)
        hash2 = 0
        for i in range(nums2_len):
            hash2 = hash2*d + nums2[i] # Here not using mod to keep it simple
            # print(hash2)
            if i>=(k-1):
                if hash2 in hash_set: return True
                hash2 = hash2 - nums2[i-(k-1)]*h
        return False
    
    # This is based on binary search + rolling hash(Rabin Karp)
    # O((M+N)*log(min(M,N))) where M, NM,N are the lengths of A, B.
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        max_len = 0
        nums1_len, nums2_len = len(nums1), len(nums2)
        s, e = 1, min(nums1_len, nums2_len)
        while s<=e:
            mid = s + (e-s)//2
            if self.search_for_k_len_subarr(nums1, nums1_len, nums2, nums2_len, mid):
                max_len = mid
                s = mid+1
            else:
                e = mid-1
        return max_len

    # This is DP solution with O(mn) time and O(m) space complexity.
    def findLength_dp(self, nums1: list[int], nums2: list[int]) -> int:
        max_len = 0
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        dp = [0 for i in range(nums2_len)]
        for i in range(nums1_len-1, -1, -1):
            prev = 0
            for j in range(nums2_len-1, -1, -1):
                t_prev   = dp[j]
                diagonal = None
                if i==(nums1_len-1) or (j==nums2_len-1):diagonal = 0
                else: diagonal = prev
                if nums1[i]==nums2[j]:
                    dp[j] = 1 + diagonal
                else: dp[j] = 0
                prev = t_prev
                max_len = max(max_len, dp[j])
        return max_len