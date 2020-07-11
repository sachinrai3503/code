# https://www.geeksforgeeks.org/sorted-merge-one-array/
""" 
Given two sorted arrays, A and B,  
where A has a large enough buffer at the end to hold B.
Merge B into A in sorted order.
Examples:

Input : a[] = {10, 12, 13, 14, 18, NA, NA, NA, NA, NA}   
        b[] = {16, 17, 19, 20, 22};;
Output : a[] = {10, 12, 13, 14, 16, 17, 18, 19, 20, 22}
"""

def merge_2nd_list_in_1st(list1, list1_num_count, list2):
    i, j = list1_num_count-1, len(list2)-1
    k = len(list1)-1
    while i>=0 and j>=0:
        if list1[i]>list2[j]:
            list1[k] = list1[i]
            i-=1
            k-=1
        else:
            list1[k] = list2[j]
            j-=1
            k-=1
    while j>=0:
        list1[k] = list2[j]
        k-=1
        j-=1

def main():
    list1 = [10, 12, 13, 14, 18, 0, 0, 0, 0, 0]
    list2 = [16, 17, 19, 20, 22]
    list1_element_count = 5  ## DON'T FORGET TO CHANGE
    print('list1 = ',list1)
    print('list2 = ',list2)
    merge_2nd_list_in_1st(list1,list1_element_count,list2)
    print('After merge list1 = ',list1)

if __name__ == '__main__':
    main()
