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

def main():
    l1 = [1, 4, 5, 7]
    l2 = [10, 20, 30, 40]
    x = 50
    print('l1>',l1)
    print('l2>',l2)
    print('X=',x)
    print('Closest pair>', find_closest_pair(l1, l2, x))

if __name__ == '__main__':
    main()