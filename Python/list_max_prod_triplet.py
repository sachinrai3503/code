# https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
"""
Given an integer array, find a maximum product of a triplet in array.

Examples:

Input:  [10, 3, 5, 6, 20]
Output: 1200
Multiplication of 10, 6 and 20
 
Input:  [-10, -3, -5, -6, -20]
Output: -90

Input:  [1, -4, 3, -6, 7, 0]
Output: 168
"""
import sys
import math

INT_MAX = sys.maxsize
INT_MIN = sys.maxsize*-1

def process_max(ip_list, num):
    prev = num
    for i in range(len(ip_list)-1,-1,-1):
        if ip_list[i]<prev:
            ip_list[i], prev = prev, ip_list[i]

def process_min(ip_list, num):
    prev = num
    for i in range(len(ip_list)):
        if ip_list[i]>prev:
            ip_list[i], prev = prev, ip_list[i]

def  get_max_prod_triplet(ip_list) -> list:
    if len(ip_list)<3:
        print('Len of list is <3.')
        return []
    pos_max_list = [INT_MIN]*3
    neg_max_list = [INT_MIN]*3
    neg_min_list = [INT_MAX]*2
    neg_count, pos_count = 0, 0
    for i in range(len(ip_list)):
        if ip_list[i]<0:
            process_max(neg_max_list,ip_list[i])
            process_min(neg_min_list,ip_list[i])
            neg_count+=1
        else:
            process_max(pos_max_list,ip_list[i])
            pos_count+=1
    print('pos_max_list',pos_max_list)
    print('neg_max_list',neg_max_list)
    print('neg_min_list',neg_min_list)
    if pos_count==0:
        return neg_max_list
    if neg_count==0:
        return pos_max_list
    if pos_count<=1 or (neg_count>=2 and pos_count>=2 and \
            neg_min_list[0]*neg_min_list[1]>pos_max_list[-2]*pos_max_list[-1]):
            return [neg_min_list[0],neg_min_list[1],pos_max_list[-1]]
    if neg_count<=1 or (neg_count>=2 and pos_count>=2 and \
            neg_min_list[0]*neg_min_list[1]<pos_max_list[-2]*pos_max_list[-1]):
        if pos_count>2:
            return pos_max_list
        else:
            return [neg_max_list[-1],pos_max_list[-2],pos_max_list[-1]]

def main():
    ip_list = [1, -4, 3, -6, 7, 0]
    print('ip>',ip_list)
    op_list = get_max_prod_triplet(ip_list)
    print(op_list)
    print(math.prod(op_list))

if __name__ == '__main__':
    main()
