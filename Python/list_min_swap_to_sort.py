#  https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
"""
Given an array of n distinct elements, find the minimum number of swaps
 required to sort the array.

Examples:
Input : {4, 3, 2, 1}
Output : 2

Input : {1, 5, 4, 3, 2}
Output : 2
"""

def count_swaps(arr):
    length = len(arr)
    index_arr = [i for i in range(length)]
    index_arr.sort(key = lambda x : arr[x])
    print(arr)
    print(index_arr)
    swap_count = 0
    i = 0
    while i<length:
        while i!=index_arr[i]:
            temp = index_arr[i]
            index_arr[i] = index_arr[index_arr[i]]
            index_arr[temp] = temp
            # print(index_arr)
            swap_count+=1
        i+=1
    return swap_count

def main():
    arr = [1,10,4,2,5,6,8]
    print(count_swaps(arr))

if __name__ == '__main__':
    main()
