# https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
# https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/
"""
Given two arrays of integers, compute the pair of values
 (one value in each array) with the smallest (non-negative) difference. 
 Return the difference.

Examples :
Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8} 
Output : 3  
That is, the pair (11, 8) 

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80} 
Output : 10
That is, the pair (40, 50)
"""

from sys import maxsize

def get_diff(a, b):
    if a>b: return a-b
    else: return b-a

def find_closest_pair(l1, l2, x):
    pair = [-maxsize, maxsize]
    min_diff = maxsize
    l1.sort()
    l2.sort()
    len1, len2 = len(l1), len(l2)
    i, j = 0, len2-1
    while i<len1 and j>=0:
        diff = get_diff(l1[i]+l2[j], x)
        if diff<min_diff:
            min_diff = diff
            pair = [l1[i], l2[j]]
        if l1[i]+l2[j]>x: j-=1
        else: i+=1
    return pair, min_diff

# This logic is not as efficient and comprehensive as above one.
def find_closest(arr1, arr2, k):
    min_diff = maxsize
    a, b = maxsize, -maxsize
    n1, n2 = len(arr1), len(arr2)
    arrs = [arr1, arr2]
    pointers = [[0, n1-1],[0, n2-1]]
    while pointers[0][0]<=pointers[0][1] and pointers[1][0]<=pointers[1][1]:
        if arrs[0][pointers[0][0]]<=arrs[1][pointers[1][0]]:
            # Here i points to arr with smaller num
            # Here j points to arr with larger num
            i, j = 0, 1
            t_sum = arrs[i][pointers[i][0]] + arrs[j][pointers[j][1]]
        else:
            # Here i points to arr with smaller num
            # Here j points to arr with larger num
            i, j = 1, 0
            t_sum = arrs[i][pointers[i][0]] + arrs[j][pointers[j][1]]
        t_diff = abs(k-t_sum)
        if t_diff<min_diff:
            min_diff = t_diff
            a, b = arrs[i][pointers[i][0]], arrs[j][pointers[j][1]]
        if t_sum<=k:
            pointers[i][0] = pointers[i][0] + 1
        else:
            pointers[j][1] = pointers[j][1] - 1
    return min_diff, a, b

def main():
    l1 = [1, 4, 5, 7]
    l2 = [10, 20, 30, 40]
    x = 50
    print('l1>',l1)
    print('l2>',l2)
    print('X=',x)
    print('Closest pair>', find_closest_pair(l1, l2, x))
    print(find_closest(l1, l2, x))

if __name__ == '__main__':
    main()