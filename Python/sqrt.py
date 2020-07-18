# https://www.geeksforgeeks.org/square-root-of-a-number-without-using-sqrt-function/
"""
Given a number N, the task is to find the square root of N 
without using sqrt() function.

Examples:
Input: N = 25
Output: 5
Input: N = 3
Output: 1.73205
Input: N = 2.5
Output: 1.58114
"""

def get_nearest_root(num):
    start, end = 0, num
    while(start<end):
        mid = (start+end)//2
        sqr = mid**2
        if sqr==num:
            return mid
        elif sqr<num:
            start=mid+1
        else:
            end=mid-1
    # print('Start = ',start,'end',end)
    return start

def get_sqrt_with_precision(s, e, num):
    start, end = s, e
    while(start<end):
        mid = (start+end)/2
        sqr = mid**2
        if sqr==num:
            return mid
        elif sqr<num:
            start=mid+.000001
        else:
            end=mid-.000001
    # print('Start = ',start,'end',end)
    return start

def get_sqrt(num):
    nearest_root = get_nearest_root(num)
    sqr = nearest_root**2
    if sqr==num:
        return nearest_root
    elif sqr>num:
        return get_sqrt_with_precision(nearest_root-1,nearest_root,num)
    else:
        return get_sqrt_with_precision(nearest_root,nearest_root+1,num)

def main():
    for i in range(101):
        print('Sqrt(',i,')= ',get_sqrt(i),sep='')

if __name__=='__main__':
    main()