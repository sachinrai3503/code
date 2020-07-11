# https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/
"""
Given an array of positive integers. 
We need to make the given array a ‘Palindrome’. 
Only allowed operation on array is merge. 
Merging two adjacent elements means replacing them with their sum.
The task is to find minimum number of merge operations 
    required to make given array a ‘Palindrome’.

Input : arr[] = {15, 4, 15}
Output : 0

Input : arr[] = {1, 4, 5, 1}
Output : 1

Input : arr[] = {11, 14, 15, 99}
Output : 3
"""

def get_min_operation(ip_list):
    count = 0
    i, j = 0, len(ip_list)-1
    temp_i, temp_j = 0, len(ip_list)-1
    left_sum, right_sum = 0, 0
    while i<j:
        if i>=temp_i:
            left_sum+=ip_list[i]
            temp_i+=1
        if j<=temp_j:
            right_sum+=ip_list[j]
            temp_j-=1
        if(left_sum==right_sum):
            i+=1
            j-=1
            left_sum, right_sum = 0, 0
        elif(left_sum<right_sum):
            i+=1
            count+=1
        else:
            j-=1
            count+=1
    return count

def main():
    ip_list = [3,4,5,1,2]
    print('ip>',ip_list)
    print('Min Oper=',get_min_operation(ip_list))

if __name__ == '__main__':
    main()

