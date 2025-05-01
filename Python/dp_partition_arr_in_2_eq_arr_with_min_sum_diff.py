# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference
"""
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n
 to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into
 one of the two arrays.

Return the minimum possible absolute difference.

Example 1:
example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

Example 2:
Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.

Example 3:
example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
 
Constraints:
1 <= n <= 15
nums.length == 2 * n
-107 <= nums[i] <= 107
"""

from sys import maxsize
from typing import List

class Solution:

    def count_set_bits(self, num):
        count = 0
        while num:
            count+=1
            num = num&(num-1)
        return count

    # mem limit exceed
    def minimumDifference_2(self, nums: List[int]) -> int:
        op = maxsize
        nums_len = len(nums)
        nums_sum = sum(nums)
        mid = nums_len//2
        dp_len = 1<<nums_len
        dp = [maxsize for i in range(dp_len)]
        dp[0] = 0
        for i in range(dp_len):
            # print(f'{i=} {dp=}')
            if dp[i] is maxsize: continue
            i_set_bits = self.count_set_bits(i)
            if i_set_bits>=mid: continue # as count of items in set will become >mid
            for j in range(nums_len):
                if i&(1<<j)==0:
                    t_sum = dp[i] + nums[j]
                    dp[i|(1<<j)] = t_sum
                    if (i_set_bits==(mid-1)):
                        op = min(op, abs(nums_sum-(2*t_sum)))
        return op
    
    # retuns a dict with key as number of elements, value is all sum combination that can be made
    # this will timeout. See below for simple and fast solution
    def get_all_sum_combinations_dp(self, nums, nums_len) -> int:
        op = dict()
        dp_len = (1<<nums_len)
        dp = [None for i in range(dp_len)]
        dp[0] = 0
        for i in range(dp_len):
            # print(f'{i=} {dp=}')
            if dp[i] is None: continue
            i_set_bits = self.count_set_bits(i)
            for j in range(nums_len):
                if i&(1<<j)==0:
                    t_sum = dp[i] + nums[j]
                    dp[i|(1<<j)] = t_sum
                    sum_set = op.get(i_set_bits+1, set())
                    sum_set.add(t_sum)
                    op[i_set_bits+1] = sum_set
        return op

    # retuns a list with index as number of elements, value is all sum combination 
    # that can be made with those number of element
    def get_all_sum_combinations(self, nums, nums_len) -> int:
        dp = [list() for i in range(nums_len+1)] 
        for num in nums:
            for i in range(nums_len, 0, -1):
                if i==1:
                    dp[i].append(num)
                elif len(dp[i-1])>0:
                    for t_num in dp[i-1]:
                        dp[i].append(t_num+num)
        return dp
    
    def get_nearest_num_to_target(self, nums, nums_len, k, target):
        _floor = -1
        nums.sort()
        s, e = 0, nums_len-1
        while s<=e:
            mid = s + (e-s)//2
            if (nums[mid]+k)==target: return nums[mid]
            if (nums[mid]+k)<target:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        # print(f'{s=} {e=} {_floor=}')
        return nums[_floor] if (_floor==e) or ((_floor>-1) and (k-nums[_floor])<=(nums[_floor+1]-k)) else nums[_floor+1]


    # Same but more clean logic below
    def minimumDifference1(self, nums: List[int]) -> int:
        op = maxsize
        nums_len = len(nums)
        nums_sum = sum(nums)
        mid = nums_len//2
        mid_sum = nums_sum//2
        arr1_sum_combinations = self.get_all_sum_combinations(nums[:mid], mid)
        arr2_sum_combinations = self.get_all_sum_combinations(nums[mid:], mid)
        # print(f'{arr1_sum_combinations=}')
        # print(f'{arr2_sum_combinations=}')
        # print(f'{nums_sum=} {mid_sum=}')
        for num_count in range(1, mid+1):
            arr1_sum_combination = arr1_sum_combinations[num_count]
            arr2_sum_combination = arr2_sum_combinations[mid-num_count]
            if not arr2_sum_combination: # Case when num_count == mid
                # print(f'{num_count=} {arr1_sum_combination=} {arr2_sum_combination=}')
                for arr1_sum in arr1_sum_combination:
                    op = min(op, abs(nums_sum - 2*arr1_sum))
                    # print(f'{nums_sum=} {2*arr1_sum=} {abs(nums_sum - 2*arr1_sum)=}')
            else:
                arr1_sum_combination.sort()
                arr2_sum_combination.sort()
                arr1_sum_combination_count = len(arr1_sum_combination)
                arr2_sum_combination_count = len(arr2_sum_combination)
                # print(f'{num_count=} {mid=} {arr1_sum_combination=} {arr2_sum_combination=}')
                i, j = 0, arr2_sum_combination_count-1
                while i<arr1_sum_combination_count and j>=0:
                    x, y = arr1_sum_combination[i], arr2_sum_combination[j]
                    z = x+y
                    # print(f'{x=} {y=} {z=} {i=} {j=} {op=}')
                    if z==mid_sum:
                        op = min(op, abs(nums_sum - 2*z))
                        break
                    elif z<mid_sum:
                        i+=1
                        op = min(op, abs(nums_sum - 2*z))
                    else:
                        j-=1
                        op = min(op, abs(nums_sum - 2*z))
                # print(f'{nums_sum=} {arr1_sum+arr2_sum=} {abs(nums_sum - (arr1_sum+arr2_sum))=}')
        return op

    # New code with more simple implementation

    def get_sum_combination_new(self, nums, s, e):
        n = e-s+1
        op = [list() for i in range(n+1)]
        op[0].append(0)
        for i in range(s, e+1):
            for j in range(n, 0, -1):
                for t_sum in op[j-1]:
                    op[j].append(t_sum+nums[i])
            # print(f'{op=}')
        return op

    def minimumDifference(self, nums: List[int]) -> int:
        op = maxsize
        nums_len = len(nums)
        nums_len_half = nums_len//2
        nums_sum = sum(nums)
        nums_sum_half = (nums_sum+1)//2
        sum_combination_left = self.get_sum_combination_new(nums, 0, nums_len_half-1)
        sum_combination_right = self.get_sum_combination_new(nums, nums_len_half, nums_len-1)
        for i in range(1, nums_len_half+1):
            left_sums = sum_combination_left[i]
            right_sums = sum_combination_right[nums_len_half-i]
            left_sums.sort()
            right_sums.sort()
            left_sums_count, right_sums_count = len(left_sums), len(right_sums)
            s, e = 0, right_sums_count-1
            spread = maxsize
            # print(f'{i=} {left_sums=} {right_sums=}')
            while s<left_sums_count and e>-1:
                t_half_sum = left_sums[s] + right_sums[e]
                # print(f'{s=} {e=} {t_half_sum=} {nums_sum_half=} {spread=}')
                if t_half_sum == nums_sum_half:
                    return abs(2*t_half_sum-nums_sum) # don't return 0. won't work for odd sums
                elif t_half_sum>nums_sum_half:
                    e-=1
                else:
                    s+=1
                if abs(t_half_sum-nums_sum_half)<spread:
                    op = min(op, abs(2*t_half_sum-nums_sum))
                    spread = abs(t_half_sum-nums_sum_half)
        return op