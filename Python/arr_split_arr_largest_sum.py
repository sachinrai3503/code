# https://leetcode.com/problems/split-array-largest-sum
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

"""
Given an array nums which consists of non-negative integers and an integer m,
 you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4
 
Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
"""

from sys import maxsize

class Solution:
    
    def get_pre_sum(self):
        pre_sum = list()
        prev = 0
        for num in self.nums:
            pre_sum.append(prev+num)
            prev+=num
        return pre_sum
    
    def find_best_m_partition_sum(self, pre_sum, m, i, j, prev_m_partition_sum):
        # print(f'{m=} {i=} {j=} {prev_m_partition_sum=}')
        best_sum = maxsize
        t_sum = 0 if i==0 else pre_sum[i-1]
        s, e = i, j
        while s<=e:
            mid = s + (e-s)//2
            part1_sum = pre_sum[mid] - t_sum # 1 subarr sum
            part2_sum = maxsize
            if mid==j and m==1: part2_sum = 0 # sum(arr[n:]) is 0 if m==0 else maxsize
            else:
                part2_sum = prev_m_partition_sum[mid+1]
            best_sum = min(best_sum, max(part1_sum, part2_sum))
            # print(f'{s=} {e=} {mid=} {part1_sum=} {part2_sum=} {best_sum=}')
            if part1_sum==part2_sum: break
            elif part1_sum<part2_sum: s = mid+1
            else: e = mid-1
        return best_sum
    
    # DP + binary search - O(mnlog(n))
    def splitArray_DP(self, nums: List[int], m: int) -> int:
        self.nums_len = len(nums)
        self.nums = nums
        pre_sum = self.get_pre_sum()
        prev_m_dp = [maxsize for i in range(self.nums_len)]
        cur_m_dp = [0 for i in range(self.nums_len)]
        for t_m in range(1, m+1):
            j = self.nums_len-t_m # till j'th index nums can be split into t_m subarr
            for i in range(j, -1, -1):
                cur_m_dp[i] = self.find_best_m_partition_sum(pre_sum, t_m, i, j, prev_m_dp)
            # print(t_m, cur_m_dp)
            prev_m_dp, cur_m_dp = cur_m_dp, prev_m_dp
        return prev_m_dp[0]
    
    def get_info(self, nums, nums_len):
        _max, total_sum = 0, 0
        for num in nums:
            _max = max(_max, num)
            total_sum+=num
        return _max, total_sum
    
    
    """
    Checks if arr can be divided into m subarr such that sum of each is <=k
    t_m==m returns True
    t_m>m  returns False
    t_m<m  returns True
    """
    def is_max_k_sum_subarr_possible(self, nums, nums_len, m, k):
        t_m = 0
        i, t_sum = 0, 0
        while i<nums_len:
            t_sum+=nums[i]
            if t_sum>k:
                t_m+=1
                if t_m==m: return False 
                t_sum = nums[i]
            i+=1
        return True
    
    def splitArray(self, nums: List[int], m: int) -> int:
        nums_len = len(nums)
        min_sum, max_sum = self.get_info(nums, nums_len)
        s, e = min_sum, max_sum
        while s<=e:
            mid = s + (e-s)//2
            is_possible = self.is_max_k_sum_subarr_possible(nums, nums_len, m, mid)
            # print(f'{s=} {e=} {mid=} {t_m=}')
            if is_possible: e = mid-1
            else: s = mid+1
        return s