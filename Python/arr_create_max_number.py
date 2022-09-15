# https://leetcode.com/problems/create-maximum-number
# https://www.geeksforgeeks.org/maximum-k-digit-number-possible-from-subsequences-of-two-given-arrays
"""
You are given two integer arrays nums1 and nums2 of lengths m and n respectively.
 nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. 
 The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

Example 1:
Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]

Example 2:
Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]

Example 3:
Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]

Constraints:
m == nums1.length
n == nums2.length
1 <= m, n <= 500
0 <= nums1[i], nums2[i] <= 9
1 <= k <= m + n
"""

class Solution:
    
    def to_list(self, n):
        n_str_list = list(str(n))
        op = [int(item) for item in n_str_list]
        return op
    
    def add(self, a, b):
        if b==None: return None
        return a+b
    
    def get_max_in_2(self, a, b):
        if a==None and b==None: return None
        if a==None: return b
        if b==None: return a
        return max(a,b)
    
    def get_max(self, a, b, c, d):
        return self.get_max_in_2(self.get_max_in_2(a,b),self.get_max_in_2(c,d))
    
    def maxNumber_dp(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        m = len(nums1)
        n = len(nums2)
        dp = [[[None for j in range(n+1)] for i in range(m+1)] for t in range(2)]
        # print(dp, end = "\n***************************\n")
        for t_k in range(1, k+1):
            cur_mat = t_k%2
            prev_mat = 0 if cur_mat==1 else 1
            t_place = 10**(t_k-1)
            for i in range(m, -1, -1):
                a = nums1[i] if i<m else None
                for j in range(n, -1, -1):
                    b = nums2[j] if j<n else None
                    if a==None and b==None: t_num = None
                    else:
                        with_a, with_b, without_a, without_b = None, None, None, None
                        if a is not None:
                            with_a = a if t_k==1 else self.add(a*t_place, dp[prev_mat][i+1][j])
                            without_a = dp[cur_mat][i+1][j]
                        if b is not None:
                            with_b = b if t_k==1 else self.add(b*t_place, dp[prev_mat][i][j+1])
                            without_b = dp[cur_mat][i][j+1]
                        t_num = self.get_max(with_a, with_b, without_a, without_b)
                        # print(i, j, with_a, with_b, without_a, without_b, t_num)
                    dp[cur_mat][i][j] = t_num
            # print(dp[cur_mat])
        result = dp[k%2][0][0]
        return self.to_list(result)

    def compare(self, num1, num1_len, i, num2, num2_len, j):
        while i<num1_len and j<num2_len:
            if num1[i]<num2[j]: return -1
            if num1[i]>num2[j]: return 1
            i+=1
            j+=1
        if j==num2_len: return 1
        return -1
    
    def combine(self, num1, num1_len, num2, num2_len, k):
        if num1 is None or not num1: return num2
        if num2 is None or not num2: return num1
        op = list()
        i, j = 0, 0
        while i<num1_len and j<num2_len:
            if num1[i]>num2[j]:
                op.append(num1[i])
                i+=1
            elif num1[i]<num2[j]:
                op.append(num2[j])
                j+=1
            else:
                is_num1_geeq = self.compare(num1, num1_len, i, num2, num2_len, j)
                if is_num1_geeq in [0, 1]:
                    op.append(num1[i])
                    i+=1
                else:
                    op.append(num2[j])
                    j+=1
        while i<num1_len:
            op.append(num1[i])
            i+=1
        while j<num2_len:
            op.append(num2[j])
            j+=1
        return op
    
    def get_max_k_digit_num(self, num_list, num_len, k):
        stck = list()
        for i in range(num_len):
            while stck and stck[-1]<num_list[i] and (num_len-i)>(k-len(stck)): # available_count>req_count
                stck.pop()
            if len(stck)<k:
                stck.append(num_list[i])
        return stck
    
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        op = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        start = max(0, k-nums2_len)
        end = min(k, nums1_len) + 1
        for i in range(start, end):
            n1 = self.get_max_k_digit_num(nums1, nums1_len, i)
            n2 = self.get_max_k_digit_num(nums2, nums2_len, k-i)
            t_op = self.combine(n1, i, n2, k-i, k)
            if self.compare(op, len(op), 0, t_op, len(t_op), 0)==-1:
                op = t_op
        return op
            