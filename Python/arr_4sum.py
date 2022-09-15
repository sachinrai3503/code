# https://leetcode.com/problems/4sum
"""
Given an array nums of n integers, return an array of all the unique quadruplets
 [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution:
    
    def get_next_i(self, i, cur_num):
        while i<self.nums_len and self.nums[i]==cur_num:
            i+=1
        return i
    
    def get_prev_j(self, j, cur_num):
        while j>=0 and self.nums[j]==cur_num:
            j-=1
        return j
    
    def check_2_sum(self, s, e, target, op):
        while s<e:
            t_sum = self.nums[s] + self.nums[e]
            if t_sum==target:
                self.op.append(list(op))
                self.op[-1].append(self.nums[s])
                self.op[-1].append(self.nums[e])
                s = self.get_next_i(s, self.nums[s])
                e = self.get_prev_j(e, self.nums[e])
            elif t_sum>target:
                e = self.get_prev_j(e, self.nums[e])
            else:
                s = self.get_next_i(s, self.nums[s])
    
    def check_n_sum(self, i, target, n, op):
        if i==self.nums_len:
            return
        if n<2:
            print('Error')
            return
        if n==2:
            self.check_2_sum(i, self.nums_len-1, target, op)
        else:
            while i<self.nums_len:
                op.append(self.nums[i])
                self.check_n_sum(i+1, target-self.nums[i], n-1, op)
                op.pop()
                i = self.get_next_i(i, self.nums[i])
    
    # O(n^3) solution
    def fourSum_n3(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        self.nums = nums
        self.nums_len = len(nums)
        self.op = list()
        op = list()
        self.check_n_sum(0, target, 4, op)
        return self.op
    
    # O(n2). a+b+c+d = target -> To maintain unique (a,b) should be before (c,d)
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        op = set()
        nums.sort()
        two_sum_dict = dict()
        self.nums = nums
        self.nums_len = len(nums)
        i = 0
        while i<self.nums_len:
            j = i+1
            while j<self.nums_len:
                t_sum = nums[i]+nums[j]
                req_sum = target - t_sum
                two_sums = two_sum_dict.get(req_sum, None)
                if two_sums:
                    for two_sum in two_sums:
                        if two_sum[1]>=i: continue # (a,b) not before (c,d)
                        t_op = [nums[i],nums[j],nums[two_sum[0]],nums[two_sum[1]]]
                        t_op.sort()
                        op.add(tuple(t_op)) # this too handle [2,2,2,2,2] target = 8
                t_list = two_sum_dict.get(t_sum, list())
                t_list.append([i,j])
                two_sum_dict[t_sum] = t_list
                # print(two_sum_dict)
                # print(i, j, op)
                j = self.get_next_i(j, nums[j])
                # j+=1
            # i = self.get_next_i(i, nums[i])
            i+=1
        return op