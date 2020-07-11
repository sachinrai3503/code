# https://www.geeksforgeeks.org/find-element-bitonic-array/
"""
Given a bitonic sequence of n distinct elements, 
write a program to find a given element x in the bitonic sequence 
in O(log n) time. 

A Bitonic Sequence is a sequence of numbers which is 
first strictly increasing then after a point strictly decreasing.

Examples:
Input :  arr[] = {-3, 8, 9, 20, 17, 5, 1};
         key = 20
Output : Found at index 3
"""
def binary_search_increasing_arr(ip_list,s,e,num):
    while s<=e:
        mid = (s+e)//2
        if ip_list[mid]==num:
            return mid
        if ip_list[mid]>num:
            e = mid-1
        else:
            s = mid+1
    return -1

def binary_search_decreasing_arr(ip_list,s,e,num):
    while s<=e:
        mid = (s+e)//2
        if ip_list[mid]==num:
            return mid
        if ip_list[mid]>num:
            s = mid+1
        else:
            e = mid-1
    return -1

def check_peak(ip_list,s,e,i):
    """
    Returns 0 if the element at index i is max
    else return -1 if the max element is on left
    else return 1 if the max elemet is on right
    s : Start index
    e : End index
    i : Current index
    """
    if s!=i and ip_list[i-1]>ip_list[i]:
        return -1
    elif e!=i and ip_list[i+1]>ip_list[i]:
        return 1
    return 0

def get_peak(ip_list):
    s, e = 0, len(ip_list)-1
    while s<=e:
        mid = (s+e)//2
        peak_side = check_peak(ip_list,s,e,mid)
        if peak_side==0:
            return mid
        elif peak_side==-1:
            e = mid-1
        else:
            s = mid+1
    return -1

def find_element(ip_list,num):
    peak_index = get_peak(ip_list)
    print("Peak index = ",peak_index)
    if peak_index==-1 or ip_list[peak_index]<num:
        return -1
    is_present = binary_search_increasing_arr(ip_list,0,peak_index,num)
    if(is_present!=-1):
        return is_present
    is_present = binary_search_decreasing_arr(ip_list,peak_index+1,len(ip_list)-1,num)
    return is_present

def main():
    ip_list = [120, 100, 80, 20, 0]
    print('ip=>',ip_list)
    num = -2
    print('num index = ',find_element(ip_list,num))

if __name__ == '__main__':
    main()