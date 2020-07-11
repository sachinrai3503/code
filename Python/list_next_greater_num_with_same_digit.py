# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
"""
Given a number n, find the smallest number that has same 
    set of digits as n and is greater than n. 
If n is the greatest possible number with its set of digits, 
then print “not possible”.

Examples:
For simplicity of implementation, we have considered input number as a string.

Input:  n = "218765"
Output: "251678"
"""

def reverse_list(ip_list, from_index, to_index):
    while from_index<to_index:
        ip_list[from_index], ip_list[to_index] = ip_list[to_index], ip_list[from_index]
        from_index+=1
        to_index-=1

def get_ceil_index(ip_list, from_index, to_index, num):
    ceil_index = -1
    s, e = from_index, to_index
    while s<=e:
        mid = (s+e)//2
        if ip_list[mid]>num:
            ceil_index = mid
            s = mid+1
        else:
            e = mid-1
    return ceil_index

def get_smaller_element_index(ip_list):
    if len(ip_list)<=1:
        return -1
    for i in range(len(ip_list)-1,0,-1):
        if ip_list[i]<=ip_list[i-1]:
            i-=1
        else:
            break
    return i-1

def get_next_greater_num_with_same_digit(ip_list):
    smaller_index = get_smaller_element_index(ip_list)
    if smaller_index==-1:
        print('Not possible')
        return
    ceil_index = get_ceil_index(ip_list,smaller_index+1,len(ip_list)-1,ip_list[smaller_index])
    ip_list[smaller_index], ip_list[ceil_index] = ip_list[ceil_index], ip_list[smaller_index]
    reverse_list(ip_list,smaller_index+1,len(ip_list)-1)

def main():
    ip_list = [2,1,8,7,6,5]
    print('ip>',ip_list)
    get_next_greater_num_with_same_digit(ip_list)
    print('op>',ip_list)

if __name__ == '__main__':
    main()
