# https://www.geeksforgeeks.org/finding-k-modulus-array-element/
"""
Given an array of n integers .We need to find all ‘k’ such that 
arr[0] % k = arr[1] % k = ....... = arr[n-1] % k 

Examples: 
Input  : arr[] = {6, 38, 34}
Output : 1 2 4
        6%1 = 38%1 = 34%1 = 0
        6%2 = 38%2 = 34%2 = 0
        6%4 = 38%4 = 34%2 = 2

Input  : arr[] = {3, 2}
Output : 1
"""

from math import sqrt
from sys import maxsize

def get_factors(n):
    factors = list()
    s, e = 1, int(sqrt(n))
    print(s, e, n)
    while s<=e:
        if n%s==0: 
            factors.append(s)
            if n//s != s: factors.append(n//s)
        s+=1
    print(f'{factors=}')
    return factors

def get_min_max(arr):
    _min, _max = maxsize, -maxsize
    for num in arr:
        _min = min(_min, num)
        _max = max(_max, num)
    return _min, _max

def find_k(arr):
    op = list()
    len_arr = len(arr)
    _min, _max = get_min_max(arr)
    diff = _max - _min
    if diff==0: return 'Infinite factors'
    diff_factors = get_factors(diff)
    for factor in diff_factors:
        exp_rem = arr[0]%factor
        i = 1
        while i<len_arr: 
            if (arr[i]%factor)!=exp_rem: break
            i+=1
        if i==len_arr: op.append(factor)
    return op

def main():
    arr = [3,2]
    op = find_k(arr)
    print(op)

if __name__ == "__main__":
    main()