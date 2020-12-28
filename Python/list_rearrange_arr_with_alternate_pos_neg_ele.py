
def swap(ip_list, index1, index2):
    ip_list[index1], ip_list[index2] = ip_list[index2], ip_list[index1] 

def right_rotate_by_1(ip_list, from_index, to_index):
    while to_index>from_index:
        swap(ip_list, to_index-1, to_index)
        to_index-=1

# https://www.geeksforgeeks.org/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/
# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/
"""
Given an array of positive and negative numbers, arrange them in an alternate
 fashion such that every positive number is followed by negative and vice-versa.

Order of elements in output doesn’t matter. 
Extra positive or negative elements should be moved to end.

Examples: 

Input :
arr[] = {-2, 3, 4, -1}
Output :
arr[] = {-2, 3, -1, 4} OR {-1, 3, -2, 4} OR ..

Input :
arr[] = {-2, 3, 1}
Output :
arr[] = {-2, 3, 1} OR {-2, 1, 3} 

Input : 
arr[] = {-5, 3, 4, 5, -6, -2, 8, 9, -1, -4}
Output :
arr[] = {-5, 3, -2, 5, -6, 4, -4, 9, -1, 8} 
        OR ..
"""
# NOTE - Here order of elements is not imp.
# BUT complexity should be O(n) time and O(1) extra space.
def rearrange_list_no_order(ip_list):
    length = len(ip_list)
    req_num = -1 # -1 : neg, 1 : pos
    for i in range(length):
        if req_num==-1 and ip_list[i]>=0:
            j = i+1
            while j<length and ip_list[j]>=0: j+=1
            if j<length: swap(ip_list, i, j)
        elif req_num==1 and ip_list[i]<0:
            j = i+1
            while j<length and ip_list[j]<0: j+=1
            if j<length: swap(ip_list, i, j)
        req_num = -1 if req_num==1 else 1

# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
"""
Given an array of positive and negative numbers, arrange them in an alternate 
fashion such that every positive number is followed by negative and vice-versa 
maintaining the order of appearance. 

Number of positive and negative numbers need not be equal. 
If there are more positive numbers they appear at the end of the array.
 If there are more negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0} 
"""
# NOTE - Order of element has to be maintained.
# Space complexity - O(1)
def rearrange_list_with_order(ip_list):
    length = len(ip_list)
    req_num = -1 # -1 : neg, 1 : pos
    for i in range(length):
        if req_num==-1 and ip_list[i]>=0:
            j = i+1
            while j<length and ip_list[j]>=0: j+=1
            if j<length: right_rotate_by_1(ip_list, i, j)
        elif req_num==1 and ip_list[i]<0:
            j = i+1
            while j<length and ip_list[j]<0: j+=1
            if j<length: right_rotate_by_1(ip_list, i, j)
        req_num = -1 if req_num==1 else 1

def main():
    ip_list = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    print('ip>',ip_list)
    # rearrange_list_no_order(ip_list)
    # print('After rearrange no order>',ip_list)
    rearrange_list_with_order(ip_list)
    print('After rearrange with order',ip_list)

if __name__ == '__main__':
    main()