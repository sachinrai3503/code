# https://www.geeksforgeeks.org/find-union-and-intersection-of-two-unsorted-arrays/
"""
Find Union and Intersection of two unsorted arrays
Given two unsorted arrays that represent two sets 
(elements in every array are distinct), 

find union and intersection of two arrays.
For example, if the input arrays are:
arr1[] = {7, 1, 5, 2, 3, 6}
arr2[] = {3, 8, 6, 20, 7}
Union as {1, 2, 3, 5, 6, 7, 8, 20} 
Intersection as {3, 6, 7}. 
Note that the elements of union and intersection can be printed in any order.
"""

def get_last_occurance(ip_list, from_index, num):
    i = from_index
    while i<len(ip_list):
        if ip_list[i]!=num:
            return i-1
        i+=1
    return i-1

def get_union_intersection(list1, list2):
    list1.sort()
    list2.sort()
    union = list()
    intersection = list()
    i, j = 0, 0
    while i<len(list1) and j<len(list2):
        i = get_last_occurance(list1,i,list1[i])
        j = get_last_occurance(list2,j,list2[j])
        if list1[i]<list2[j]:
            union.append(list1[i])
            i+=1
        elif list1[i]>list2[j]:
            union.append(list2[j])
            j+=1
        else:
            intersection.append(list1[i])
            union.append(list1[i])
            i+=1
            j+=1
    while i<len(list1):
        i = get_last_occurance(list1,i,list1[i])
        union.append(list1[i])
        i+=1
    while j<len(list2):
        j = get_last_occurance(list2,j,list2[j])
        union.append(list2[j])
        j+=1
    return union, intersection

def main():
    list1 = [7, 1, 5, 2, 3, 6]
    list2 = [3, 8, 6, 20, 7]
    print('list1 >',list1)
    print('list2 >',list2)
    union, intersection = get_union_intersection(list1,list2)
    print('union >',union)
    print('intersection >',intersection)

if __name__ == '__main__':
    main()