# https://www.geeksforgeeks.org/count-inversions-of-size-k-in-a-given-array/
"""
Given an array of n distinct integers a_{1}, a_{2}, ..., a_{n} and an integer k.
Find out the number of sub-sequences of a such that
 a_{i_{1}} > a_{i_{2}} > ... > a_{i_{k}}, & 1<= i_{1} < i_{2} < ... < i_{k}<= n.

In other words output the total number of inversions of length k.

Examples:

Input : a[] = {9, 3, 6, 2, 1}, k = 3        
Output : 7
The seven inversions are {9, 3, 2}, {9, 3, 1}, 
{9, 6, 2}, {9, 6, 1}, {9, 2, 1}, {3, 2, 1} and
{6, 2, 1}.

Input : a[] = {5, 6, 4, 9, 2, 7, 1}, k = 4
Output : 2
The two inversions are {5, 4, 2, 1}, {6, 4, 2, 1}.
"""

# Below sol. assumes arr/list elements are unique.

# Time - O(kn2) && space - O(n)
def count_size_k_inversion_DP(ip_list, k):
    length = len(ip_list)
    if length <= 0 or k <= 1:
        print('Invalid input')
        return None
    count = 0
    op = [[0]*length, [0]*length]
    for i in range(k-1):
        count = 0
        cur_row = 0 if i % 2 == 0 else 1
        prev_row = 0 if cur_row == 1 else 1
        for j in range(length):
            smaller_count = 0
            for p in range(j+1, length):
                if ip_list[p] < ip_list[j]:
                    if i == 0:
                        smaller_count += 1
                    else:
                        smaller_count += op[prev_row][p]
            op[cur_row][j] = smaller_count
            count += op[cur_row][j]
            # print(op)
    return count


def update(bit, bit_len, index, value):
    i = index
    while i < bit_len:
        bit[i] += value
        i = i + (i & -i)


def query(bit, bit_len, index):
    sum = 0
    i = index
    while i > 0:
        sum += bit[i]
        i = i - (i & -i)
    return sum

# Time = O(nklog(n)) && Space - O(kn)
# Same logic as above but using BIT
def count_size_k_inversion_BIT(ip_list, k):
    length = len(ip_list)
    if length <= 0 or k <= 1:
        print("Invalid input")
        return None
    pos_list = [[ip_list[i], length-i] for i in range(length-1, -1, -1)]
    sorted_pos_list = sorted(pos_list, key=lambda pos: pos[0])
    # print(sorted_pos_list)
    # Here bit_op[i][j] gives no. of req. seq. starting with j and of length i.
    bit_op = [[0]*(length+1) for i in range(k)]
    bit_row_len = length+1
    for i in range(length):
        pos = sorted_pos_list[i][1]
        update(bit_op[0], bit_row_len, pos, 1)
        for j in range(1, k):
            update(bit_op[j], bit_row_len, pos, 
                   query(bit_op[j-1], bit_row_len, pos-1))
        # print(bit_op)
    return query(bit_op[k-1], bit_row_len, length)


def main():
    ip_list = [5, 6, 4, 9, 3, 7, 2, 1 ]
    k = 10
    print('ip>>', ip_list)
    print('k=', k)
    print('K len inversion count DP =', count_size_k_inversion_DP(ip_list, k))
    print('K len inversion count BIT =', count_size_k_inversion_BIT(ip_list, k))


if __name__ == '__main__':
    main()
