# https://www.geeksforgeeks.org/merging-two-unsorted-arrays-sorted-order/
"""
Write a SortedMerge() function that takes two lists,
 each of which is unsorted, and merges the two together 
 into one new list which is in sorted (increasing) order.
  SortedMerge() should return the new list.

Examples :

Input : a[] = {10, 5, 15}
        b[] = {20, 3, 2}
Output : Merge List :
        {2, 3, 5, 10, 15, 20}
"""

def sort_list(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1,len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

def merge_sorted_list(list1, list2):
    new_list = list()
    i, j, = 0, 0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            new_list.append(list1[i])
            i+=1
        else:
            new_list.append(list2[j])
            j+=1
    while i<len(list1):
        new_list.append(list1[i])
        i+=1
    while j<len(list2):
        new_list.append(list2[j])
        j+=1
    return new_list

def merge_2_list(list1,list2):
    sort_list(list1)
    sort_list(list2)
    return merge_sorted_list(list1,list2)

def main():
    list1 = [1, 10, 5, 15]
    list2 = [20, 0, 2]
    print('list1 =>',list1)
    print('list2 =>',list2)
    print('merrged list =>',merge_2_list(list1,list2))

if __name__ == '__main__':
    main()