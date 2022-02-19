# https://www.geeksforgeeks.org/maximum-product-subsequence-size-k
"""
Given an array A[] of n integers, the task is to find a subsequence of size k
 whose product is maximum among all possible k sized subsequences of the given array.

Constraints 
1 <= n <= 10^5
1 <= k <= n
Examples: 
Input : A[] = {1, 2, 0, 3}, 
        k = 2
Output : 6
Explanation : Subsequence containing elements
{2, 3} gives maximum product : 2*3 = 6

Input : A[] = {1, 2, -1, -3, -6, 4}, 
        k = 4
Output : 144
Explanation : Subsequence containing {2, -3, 
-6, 4} gives maximum product : 2*(-3)*(-6)*4 
= 144
"""

from sys import maxsize

def binary_search(arr):
    s, e = 0, len(arr)-1
    index = -1
    while s<=e:
        mid = s + (e-s)//2
        if arr[mid]<0:
            index = mid
            s = mid+1
        else:
            e = mid-1
    return index

def max_prod_subseq_size_k(arr, k):
    if k<=0:    return maxsize*-1
    length = len(arr)
    arr.sort()
    neg_count = binary_search(arr)+1
    pos_count = length - neg_count
    pos_prod = [None for i in range(pos_count)]
    neg_prod_LR = [None for i in range(neg_count)]
    neg_prod_RL = [None for i in range(neg_count)]
    prev = 1
    for i in range(pos_count):
        pos_prod[i] = prev*arr[-(i+1)]
        prev = pos_prod[i]
    prev1, prev2 = 1, 1
    for i in range(neg_count):
        neg_prod_LR[i] = prev1*arr[i]
        neg_prod_RL[i] = prev2*arr[-(pos_count+i+1)]
        prev1 = neg_prod_LR[i]
        prev2 = neg_prod_RL[i]
    # print(pos_prod, neg_prod_LR, neg_prod_RL)
    max_prod = maxsize * -1
    for p in range(min(k, pos_count), -1, -1):
        pos_p_prod = 1 if p==0 else pos_prod[p-1]
        n = k-p
        if n>neg_count: return max_prod
        if n==0: neg_n_prod = 1
        else:
            neg_n_prod = neg_prod_LR[n-1] if n%2==0 else neg_prod_RL[n-1]
        max_prod = max(max_prod, neg_n_prod*pos_p_prod)
    return max_prod

def main():
    arr = [1,3,0,0,-1,-5]
    for k in range(len(arr)+1):
        max_prod = max_prod_subseq_size_k(arr, k)
        print(k, max_prod)

if __name__ == '__main__':
    main()
