# https://www.geeksforgeeks.org/place-k-elements-such-that-minimum-distance-is-maximized/
"""
Given an array representing n positions along a straight line. 
Find k (where k <= n) elements from the array such that the minimum distance
 between any two (consecutive points among the k points) is maximized.

Examples :  

Input : arr[] = {1, 2, 8, 4, 9}
            k = 3
Output : 3
Largest minimum distance = 3
3 elements arranged at positions 1, 4 and 8, 
Resulting in a minimum distance of 3

Input  : arr[] = {1, 2, 7, 5, 11, 12}
             k = 3
Output : 5
Largest minimum distance = 5
3 elements arranged at positions 1, 7 and 12, 
resulting in a minimum distance of 5 (between
7 and 12)
"""

# Below sol. assumes all the elements are unique in the arr

from sys import maxsize
import random

def is_possible(arr, k, diff):
    count, prev = 0, maxsize*-1
    for num in arr:
        if (num-prev)>=diff:
            count+=1
            prev=num
            if count==k: return True
    return False

def find_k_ele_with_max_min_diff(arr, k):
    max_min_diff = maxsize*-1
    if k<=1: return max_min_diff
    arr.sort()
    # s = 1 as min_diff can be one
    # e = (high-low)//(k-1) because this is the max diff. in best possible arrangement
    s, e = 1, (arr[-1]-arr[0])//(k-1)
    while s<=e:
        mid = s + (e-s)//2
        if is_possible(arr, k, mid):
            max_min_diff = mid
            s = mid+1
        else: e = mid-1
    return max_min_diff

def main():
    arr = random.sample(range(50,511), 20)
    print(arr)
    for k in range(1,len(arr)+1):
        print('k =',k,' max_min_diff = ',find_k_ele_with_max_min_diff(arr, k))

if __name__ == '__main__':
    main()