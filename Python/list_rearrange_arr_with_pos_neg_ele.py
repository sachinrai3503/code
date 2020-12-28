# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/
"""
Given an array of positive and negative numbers, arrange them such that all 
negative integers appear before all the positive integers in the array without
using any additional data structure like hash table, arrays, etc. 
 
The order of appearance should be maintained.

Examples:

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]
"""
# Here 1 way is to solve using modifed insertion sort. Where -ve element is
# inserted before 1st positive element. Shifting of +ve elements is needed.
# Space - O(1) Time - O(n2)

# Below approch uses modified merge sort. Time complexity - O(nlog(n))
# Space - O(log(n)) for recursion stack.

# Assumes ip_list is sorted
def get_first_pos_index(ip_list, from_index, to_index):
    for i in range(from_index, to_index+1):
        if ip_list[i] >= 0:
            return i
    return to_index+1

# Assumes ip_list is sorted
def get_last_neg_index(ip_list, from_index, to_index):
    for i in range(from_index, to_index+1):
        if ip_list[i] >= 0:
            return i-1
    return to_index

def reverse(ip_list, from_index, to_index):
    while from_index<=to_index:
        ip_list[from_index], ip_list[to_index] = \
                                        ip_list[to_index], ip_list[from_index]
        from_index+=1
        to_index-=1

def merge_list(ip_list, s, mid, e):
    first_pos_index = get_first_pos_index(ip_list, s, mid)
    last_neg_index  = get_last_neg_index(ip_list, mid+1, e)
    if first_pos_index==(mid+1) or last_neg_index==mid: return
    reverse(ip_list, first_pos_index, mid)
    reverse(ip_list, mid+1, last_neg_index)
    reverse(ip_list, first_pos_index, last_neg_index)

def rearrange(ip_list, s, e):
    if s>=e: return
    mid = s + (e-s)//2
    rearrange(ip_list, s, mid)
    rearrange(ip_list, mid+1, e)
    merge_list(ip_list, s, mid, e)

def main():
    ip_list = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    print('ip>',ip_list)
    rearrange(ip_list, 0, len(ip_list)-1)
    print('Rearranged list>',ip_list)

if __name__ == '__main__':
    main()