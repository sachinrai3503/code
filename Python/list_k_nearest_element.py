# https://www.geeksforgeeks.org/find-k-closest-elements-given-value/
"""
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
Examples:

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
Note that if the element is present in array, then it should not be in output,
 only the other closest elements are required.
"""

INT_MAX = 99999999999

def get_ceil_index(ip_list, num):
    ceil_index = -1
    s, e = 0, len(ip_list)-1
    while(s<=e):
        mid = (s+e)//2
        if ip_list[mid]>num:
            ceil_index = mid
            e = mid-1
        else:
            s = mid+1
    return ceil_index

def k_nearest_element_in_list(ip_list, left, right, num, k):
    # print(left,right,k)
    op_list = list()
    length = len(ip_list)
    i = 0
    while i<k and (left>=0 or right<length):
        left_diff, right_diff = INT_MAX, INT_MAX
        if left>=0:
            left_diff = num - ip_list[left]
        if right<length:
            right_diff = ip_list[right] - num
        if left_diff < right_diff:
            op_list.append(ip_list[left])
            left-=1
        else:
            op_list.append(ip_list[right])
            right+=1
        i+=1
    return op_list

def get_k_nearest_element(ip_list, num, k):
    ceil_index = get_ceil_index(ip_list, num)
    # print('ceil_index = ',ceil_index)
    length = len(ip_list)
    left , right = -1, length
    if ceil_index==-1:
        right = length
    else:
        right = ceil_index
    left = right-1
    if left>=0 and ip_list[left]==num:
        left-=1
    return k_nearest_element_in_list(ip_list,left,right,num,k)

def main():
    ip_list = [12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56]
    print('ip=>',ip_list)
    num = 56
    k = 4
    print("op=>",get_k_nearest_element(ip_list,num,k))

if __name__ == '__main__':
    main()