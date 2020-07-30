# https://www.geeksforgeeks.org/number-swaps-sort-adjacent-swapping-allowed/
"""
Given an array arr[] of non negative integers. 
We can perform a swap operation on any two adjacent elements in the array.
Find the minimum number of swaps needed to sort the array in ascending order.

Examples :
Input  : arr[] = {3, 2, 1}
Output : 3

Input  : arr[] = {1, 20, 6, 4, 5}
Output : 5
"""

class Bit:
    def __init__(self, max_size):
        self.arr = [0 for i in range(max_size)]
        self.max_size = max_size

    def update_bit(self, index, value):
        if index<=0:
            print('Invalid Index')
            return
        while index<self.max_size:
            self.arr[index]+=value
            index = index + (index&-index)

    def query_bit(self, index):
        sum = 0
        while index>0:
            sum+=self.arr[index]
            index = index - (index&-index)
        return sum

def sort(list1, list2):
    """
    Sort list1 and modify list2 based on that sorting.
    """
    i = 0
    for i in range(len(list1)):
        min = i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[min]:
                min = j
        list1[i], list1[min] = list1[min], list1[i]
        list2[i], list2[min] = list2[min], list2[i]

def get_min_swap_to_sort(ip_list):
    index_list = [(i+1) for i in range(len(ip_list))]
    sort(ip_list,index_list)
    bit_tree = Bit(len(ip_list)+1)
    print(ip_list)
    print(index_list)
    min_swap = 0
    for i in range(len(index_list)-1,-1,-1):
        min_swap+=bit_tree.query_bit(index_list[i]-1)
        bit_tree.update_bit(index_list[i],1)
    return min_swap

def main():
    ip_list = [1, -20, 6, 4, 5]
    print('Ip=>',ip_list)
    print('Min swap=>',get_min_swap_to_sort(ip_list))

if __name__ == '__main__':
    main()