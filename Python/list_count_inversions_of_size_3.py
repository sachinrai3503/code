# https://www.geeksforgeeks.org/count-inversions-of-size-three-in-a-give-array/
# https://www.geeksforgeeks.org/find-number-of-triplets-in-array-such-that-aiajak-and-ijk/
"""
Given an array arr[] of size n. Three elements arr[i], arr[j] and arr[k] form 
an inversion of size 3 if a[i] > a[j] >a[k] and i < j < k. 

Find total number of inversions of size 3.

Example :
Input:  {8, 4, 2, 1}
Output: 4
The four inversions are (8,4,2), (8,4,1), (4,2,1) and (8,2,1).

Input:  {9, 6, 4, 5, 8}
Output:  2
The two inversions are {9, 6, 4} and {9, 6, 5}
"""

# Note - Assumes arr/list has only unique elements.
# Duplicate elements can be handled as done in arr_inversion_count.c

def get_greater_num_count_to_left(ip_list, length, from_index, num):
    count = 0
    for i in range(from_index, -1, -1):
        if ip_list[i] > num:
            count += 1
    return count


def get_smaller_num_count_to_right(ip_list, length, from_index, num):
    count = 0
    for i in range(from_index, length, 1):
        if ip_list[i] < num:
            count += 1
    return count

# O(n2) method.
def count_size_3_inversion_1(ip_list):
    count = 0
    length = len(ip_list)
    for i in range(length):
        greater_count = get_greater_num_count_to_left(ip_list, length,
                                                      i-1, ip_list[i])
        smaller_count = get_smaller_num_count_to_right(ip_list, length,
                                                       i+1, ip_list[i])
        count += (greater_count*smaller_count)
    return count


def update(bit, bit_length, index, value):
    i = index
    while i < bit_length:
        bit[i] += value
        i = i + (i & -i)


def query(bit, length, index):
    count = 0
    i = index
    while i > 0:
        count += bit[i]
        i = i - (i & -i)
    return count

# Time - O(nLog(n)) method - Same thing as above using BIT.
# Space - O(n)
def count_size_3_inversion_BIT(ip_list):
    count = 0
    length = len(ip_list)
    pos_list = [(ip_list[i], i+1) for i in range(length)]
    sorted_pos_list = sorted(pos_list, key=lambda pos: pos[0])
    # print(sorted_pos_list)
    greater_smaller_count_list = [[0, 0] for i in range(length)]
    bit_smaller = [0]*(length+1)
    bit_greater = [0]*(length+1)
    bit_len = length+1
    i, j = length-1, 0
    while i >= 0 and j < length:
        update(bit_greater, bit_len, sorted_pos_list[i][1], 1)
        update(bit_smaller, bit_len, length - sorted_pos_list[j][1] + 1, 1)
        greater_smaller_count_list[i][0] = query(bit_greater, bit_len,
                                                 sorted_pos_list[i][1]-1)
        greater_smaller_count_list[j][1] = query(bit_smaller, bit_len,
                                                 length - sorted_pos_list[j][1])
        i -= 1
        j += 1
    # print('bit_smaller>>', bit_smaller)
    # print('bit_greater>>', bit_greater)
    # print('Greater smaller list =', greater_smaller_count_list)
    i = 0
    while i < length:
        count = count + \
            (greater_smaller_count_list[i][0]*greater_smaller_count_list[i][1])
        i += 1
    return count


def main():
    ip_list = [7, 3, 4, 3, 3, 1]
    print('ip>', ip_list)
    print('Inversion count iterative =', count_size_3_inversion_1(ip_list))
    print('Inversion count BIT =', count_size_3_inversion_BIT(ip_list))


if __name__ == '__main__':
    main()
