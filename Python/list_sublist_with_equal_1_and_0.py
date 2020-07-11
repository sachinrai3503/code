# https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/
"""
Given an array arr[] of size n containing 0 and 1 only. The problem is to count the subarrays having equal number of 0’s and 1’s.

Examples:

Input : arr[] = {1, 0, 0, 1, 0, 1, 1}
Output : 8
The index range for the 8 sub-arrays are:
(0, 1), (2, 3), (0, 3), (3, 4), (4, 5)
(2, 5), (0, 5), (1, 6)
"""

def count_sublist_with_equal_1_and_0(ip_list):
    count = 0
    sum_map = dict()
    sum = 0
    for num in ip_list:
        if num==0:
            num = -1
        sum+=num
        if sum==0:
            count+=1
        if sum in sum_map.keys():
            count+=sum_map[sum]
        if sum not in sum_map.keys():
            sum_map[sum] = 1
        else:
            sum_map[sum] = sum_map[sum] + 1
    return count

def main():
    ip_list = [1, 0, 0, 1]
    print('ip=>',ip_list)
    print('sub arr count=',count_sublist_with_equal_1_and_0(ip_list))

if __name__ == '__main__':
    main()