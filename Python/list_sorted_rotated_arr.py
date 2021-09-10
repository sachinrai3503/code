# Also see arr_sorted_rotated_arr_multi.c

# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""
Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8
Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 30
Output : Not found
Input : arr[] = {30, 40, 50, 10, 20}
        key = 10   
Output : Found at index 3
"""
def find_element(ip_list, num):
    s, e = 0, len(ip_list)-1
    while s<=e:
        if s==e and ip_list[s]==num:
            return s
        elif s==e:
            return -1
        mid = (s+e)//2
        if ip_list[s]<ip_list[mid]:
            if ip_list[s]<=num and ip_list[mid]>=num:
                e = mid
            else:
                s = mid+1
        else:
            if ip_list[mid+1]<=num and ip_list[e]>=num:
                s = mid+1
            else:
                e = mid
    return -1

def is_max(ip_list, s, e, i):
    """
    Returns 1 if the element at i'th index is
        greater than both adjacent element
    else returns 0
    s : Start index
    e : End index
    i : Current index
    """
    if s!=i and ip_list[i-1]>=ip_list[i]:
        return 0
    if e!=i and ip_list[i+1]>=ip_list[i]:
        return 0
    return 1

# https://www.geeksforgeeks.org/maximum-element-in-a-sorted-and-rotated-array/
"""
Input: arr[] = {3, 4, 5, 1, 2}
Output: 5
Input: arr[] = {1, 2, 3}
Output: 3
"""
def find_max_element(ip_list):
    s, e = 0 ,len(ip_list)-1
    while s<=e:
        mid = (s+e)//2
        if is_max(ip_list,s,e,mid):
            return mid
        if ip_list[s]>ip_list[mid]:
            e = mid-1
        else:
            s = mid+1
    return -1

def is_min(ip_list, s, e, i):
    """
    Returns 1 if the element at i'th index is
        smaller than both adjacent element
    else returns 0
    s : Start index
    e : End index
    i : Current index
    """
    if s!=i and ip_list[i-1]<=ip_list[i]:
        return 0
    if e!=i and ip_list[i+1]<=ip_list[i]:
        return 0
    return 1

# https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
"""
Input: {5, 6, 1, 2, 3, 4}
Output: 1
Input: {1, 2, 3, 4}
Output: 1
Input: {2, 1}
Output: 1
"""
def find_min_element(ip_list):
    s, e = 0, len(ip_list)-1
    while s<=e:
        mid = (s+e)//2
        if is_min(ip_list,s,e,mid):
            return mid
        if ip_list[mid]<ip_list[e]:
            e = mid-1
        else:
            s = mid+1
    return -1

# Duplicates in list are not handled
def main():
    ip_list = [2, 3, 4, 5, 6, 7, 8, 1]
    print('ip=>',ip_list)
    num = 100
    max_element_index = find_max_element(ip_list)
    min_element_index = find_min_element(ip_list)
    num_index = find_element(ip_list,num)
    print('max element index = ',max_element_index)
    print('min element index = ',min_element_index)
    print('num index = ',num_index)

if __name__ == '__main__':
    main()