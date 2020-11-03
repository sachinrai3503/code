# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/
"""
Given an array of size n and an integer k, return the count of distinct numbers
 in all windows of size k.
Example:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
       k = 4
Output: 3 4 4 3
"""

def dNums(A, B):
    length = len(A)
    if length <= 0 or B <= 0:
        return []
    count_map = dict()
    op = list()
    distinct = 0
    for i in range(length):
        count = count_map.get(A[i], None)
        if count is None:
            distinct += 1
            count_map[A[i]] = 1
        else:
            count_map[A[i]] = count+1
        if i >= B-1:
            op.append(distinct)
            t_count = count_map.get(A[i-(B-1)])
            if t_count == 1:
                distinct -= 1
                count_map.pop(A[i-(B-1)])
            else:
                count_map[A[i-(B-1)]] = t_count-1
        # print(count_map)
    return op

def main():
    ip = [1, 2, 4, 4]
    k = 2
    print('ip>',ip)
    print('k>',k)
    print(dNums(ip,k))

if __name__ == '__main__':
    main()