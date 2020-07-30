# https://www.geeksforgeeks.org/partition-problem-dp-18/
"""
Partition problem is to determine whether a given set can be partitioned 
into two subsets such that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
"""
import sys

INT_MAX = sys.maxsize

def get_list_sum(ip_list):
    sum = 0
    for num in ip_list:
        sum+=num
    return sum

def get_max_pos_min_get_sum(ip_list):
    min_neg_sum, max_pos_sum = 0, 0
    for num in ip_list:
        if num<0:
            min_neg_sum+=num
        else:
            max_pos_sum+=num
    return min_neg_sum, max_pos_sum

def _process_num(sum_list, zero_index, cur_sum, num):
    new_sum = INT_MAX
    cur_sum_index = zero_index + cur_sum
    if sum_list[cur_sum_index]:
        new_sum = cur_sum + num
    elif cur_sum==num:
        new_sum = num
    if new_sum!=INT_MAX:
        sum_list[zero_index+new_sum] = True
    
def can_be_divided(ip_list):
    total_sum = get_list_sum(ip_list)
    if total_sum%2!=0:return False
    half_sum = total_sum//2
    min_neg_sum, max_pos_sum = get_max_pos_min_get_sum(ip_list)
    sum_list = [False for i in range((-1*min_neg_sum)+1+max_pos_sum)]
    zero_index = -1*min_neg_sum
    for num in ip_list:
        if num<0:
            for i in range(min_neg_sum,max_pos_sum+1,1):
                _process_num(sum_list,zero_index,i,num)
        else:
            for i in range(max_pos_sum,min_neg_sum-1,-1):
                _process_num(sum_list,zero_index,i,num)
        if sum_list[zero_index+half_sum]:
            return True
    return False

def main():
    ip_list = [1,4,5,-200,500,600,20,-2,-1,20,45,56,89,97,190,85]
    print('Ip>',ip_list)
    print('Is possible>',can_be_divided(ip_list))

if __name__ == '__main__':
    main()