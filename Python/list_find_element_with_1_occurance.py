#  https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/
"""
Given a sorted array in which all elements 
appear twice (one after one) and one element appears only once. 
Find that element in O(log n) complexity.

Example:
Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}
Output:  4
"""

def check(ip_list, s, e, i):
    """
    Checks if the current element is occurring once
    else decides which side(left/right) to move.
    s = start index
    e = end index
    i = current index
    """
    print('id(s),id(e),id(i)',id(s),id(e),id(i))
    if i<e and ip_list[i]==ip_list[i+1]:
        if i%2==0:
            s = i+2
        else:
            e = i-1
    elif i>s and ip_list[i]==ip_list[i-1]:
        if i%2==0:
            e = i-2
        else:
            s = i+1
    else:
        print('id(s),id(e),id(i)',id(s),id(e),id(i))
        return True
    print('id(s),id(e),id(i)',id(s),id(e),id(i))
    return False

def get_element_occuring_1s(ip_list):
    s, e = 0, len(ip_list)-1
    while s<=e:
        mid = (s+e)//2
        print('id(s),id(e),id(mid)',id(s),id(e),id(mid))
        is_occuring_1s = check(ip_list,s,e,mid)
        if is_occuring_1s:
            return mid
    else:
        return None

def  main():
    ip_list = [5,5]
    print('ip = ',ip_list)
    req_element_index = get_element_occuring_1s(ip_list)
    if req_element_index is None:
        print('All element occur twice')
    else:
        print(ip_list[req_element_index])

if __name__ == '__main__':
    main()
