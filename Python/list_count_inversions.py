# https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/
"""
Inversion Count for an array indicates – 
how far (or close) the array is from being sorted. 

If the array is already sorted then inversion count is 0.
 If the array is sorted in the reverse order 
    that inversion count is the maximum.

Two elements a[i] and a[j] form an inversion if
     a[i] > a[j] and i < j. For simplicity, 
     we may assume that all elements are unique.

Example:
Input: arr[] = {8, 4, 2, 1}
Output: 6
Input: arr[] = {3, 1, 2}
Output: 2
"""

# Note - This won't work for list/arr with duplicates.
# See - arr_inversion_count.c for handling of duplicates.

def _sort(list1,list2):
    """
    Sort list1 and also update the elements of list2
        as per sorting of list1.
    list1 - elements to be sorted
    list2 - index of the elements in the list1
    """
    for i in range(0,len(list1)):
        min = i
        for j in range(i+1,len(list2)):
            if list1[j]<list1[min]:
                min = j
        list1[i], list1[min] = list1[min], list1[i]
        list2[i], list2[min] = list2[min], list2[i]

def query_bit(bit_list, index):
    sum = 0
    i = index
    while i>0:
        sum+=bit_list[i]
        i = i - (i&-i)
    return sum

def update_bit(bit_list, index, value):
    i = index
    while i<len(bit_list):
        bit_list[i]+=value
        i = i + (i&-i)

def count_inversion(ip_list):
    index_list = [i for i in range(1,len(ip_list)+1)]
    _sort(ip_list,index_list)
    print(index_list)
    bit_list = [0 for i in range(len(ip_list)+1)]
    count = 0
    for i in range(len(ip_list)-1,-1,-1):
        count+=query_bit(bit_list,index_list[i]-1)
        update_bit(bit_list,index_list[i],1)
    print(bit_list)
    return count

def main():
    ip_list = [7, -90, 100, 1]
    print('ip=>',ip_list)
    print('Count => ',count_inversion(ip_list))

if __name__ == '__main__':
    main()