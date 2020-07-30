# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such
that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements,
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2))
 should be minimum.

Example:
Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11   
"""

# Note - All the below soln. handle -ve integers.

import sys

INT_MAX = sys.maxsize

def get_abs_diff(a, b):
    if a>b:
         return a-b
    return b-a

def get_list_sum(ip_list):
    sum = 0
    for num in ip_list:
        sum+=num
    return sum

def get_min(a, b):
    return a if a<b else b

def get_max_pos_min_neg_sum(ip_list):
    pos_sum = 0
    neg_sum = 0
    for num in ip_list:
        if num>=0:
            pos_sum+=num
        else:
            neg_sum+=num
    return pos_sum, neg_sum

def get_min_diff_rec(ip_list, index, total_sum, set1_sum):
    if len(ip_list)==0:
        return INT_MAX
    if index==len(ip_list):
        return get_abs_diff(set1_sum,total_sum-set1_sum)
    min_diff = INT_MAX
    diff_with_index = get_min_diff_rec(ip_list,index+1,total_sum,
            set1_sum+ip_list[index])
    diff_without_index = get_min_diff_rec(ip_list,index+1,total_sum,set1_sum)
    return diff_with_index if diff_with_index<diff_without_index \
            else diff_without_index

def is_sum_valid(sum_list, index):
    if sum_list[index]==INT_MAX:
        return False
    return True

def mark_sum_valid(sum_list, index, sum):
    sum_list[index] = sum

def _compute_diff(sum_list, zero_index, cur_s1_sum, num, total_sum):
    cur_s1_sum_index = zero_index + cur_s1_sum
    # print('zeroindex',zero_index)
    # print('cur_s1_sum=',cur_s1_sum)
    # print('cur_s1_sum_index=',cur_s1_sum_index)
    new_s1_sum = INT_MAX
    if is_sum_valid(sum_list,cur_s1_sum_index):
        new_s1_sum = cur_s1_sum + num
    elif cur_s1_sum==num:
        new_s1_sum = num
    if new_s1_sum!=INT_MAX:
        # print('new_s1_sum',new_s1_sum)
        # print('new_s1_sum index>',zero_index+new_s1_sum)
        mark_sum_valid(sum_list,zero_index+new_s1_sum,new_s1_sum)
        # print(sum_list)
        return get_abs_diff(new_s1_sum,total_sum-new_s1_sum)
    else:
        return INT_MAX

def get_min_diff_DP(ip_list):
    min_diff = INT_MAX
    total_sum = get_list_sum(ip_list)
    pos_sum, neg_sum = get_max_pos_min_neg_sum(ip_list)
    # print(total_sum,pos_sum,neg_sum)
    sum_list = [INT_MAX for i in range((-1*neg_sum)+1+pos_sum)]
    zero_index = -1*neg_sum
    for num in ip_list:
        if num<0:
            for cur_s1_sum in range(neg_sum,pos_sum+1,1):
                t_diff = _compute_diff(sum_list,zero_index,cur_s1_sum,num,
                                            total_sum)
                min_diff = get_min(min_diff,t_diff)       
        else:
            for cur_s1_sum in range(pos_sum,neg_sum-1,-1):
                t_diff = _compute_diff(sum_list,zero_index,cur_s1_sum,num,
                                            total_sum)
                min_diff = get_min(min_diff,t_diff)
    return min_diff

def get_min_diff_2(ip_list):
    min_diff = INT_MAX
    total_sum = get_list_sum(ip_list)
    sum_list = list()
    for num in ip_list:
        new_list = list()
        for sum in sum_list:
            new_list.append(sum+num)
            t_diff = get_abs_diff(sum+num,total_sum-sum-num)
            min_diff = t_diff if t_diff<min_diff else min_diff
        new_list.append(num)
        t_diff = get_abs_diff(num,total_sum-num)
        min_diff = t_diff if t_diff<min_diff else min_diff
        sum_list.extend(new_list)
        del(new_list)
    return min_diff

def main():
    ip_list = [-1, -3, -5, -6, 4, 11, 17, 23, 27, 19]
    print('Ip>>',ip_list)
    total_sum = get_list_sum(ip_list)
    min_diff_rec = get_min_diff_rec(ip_list,0,total_sum,0)
    min_diff_dp = get_min_diff_DP(ip_list)
    min_diff_2 = get_min_diff_2(ip_list)

    print('Rec min diff =',min_diff_rec)
    print('Min Diff DP =',min_diff_dp)
    print('Min Diff 2 =',min_diff_2)

if __name__ == '__main__':
    main()