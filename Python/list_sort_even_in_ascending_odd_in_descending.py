# https://www.geeksforgeeks.org/sort-even-numbers-ascending-order-sort-odd-numbers-descending-order/
"""
Given an array of integers (both odd and even), 
sort them in such a way that the first part of the array contains
 odd numbers sorted in descending order,
rest portion contains even numbers sorted in ascending order.

Examples:

Input  : arr[] = {1, 2, 3, 5, 4, 7, 10}
Output : arr[] = {7, 5, 3, 1, 2, 4, 10}

Input  : arr[] = {0, 4, 5, 3, 7, 2, 1}
Output : arr[] = {7, 5, 3, 1, 0, 2, 4} 
"""

def cusomized_sort(ip_list):
    for i in range(len(ip_list)):
        req_index = i
        for j in range(i+1,len(ip_list)):
            if ip_list[req_index]%2==0 and ip_list[j]%2==0:
                req_index = req_index if ip_list[req_index]<ip_list[j] else j
            elif ip_list[req_index]%2==1 and ip_list[j]%2==1:
                req_index = j if ip_list[req_index]<ip_list[j] else req_index
            else:
                req_index = j if ip_list[req_index]%2==0 else req_index
        ip_list[i], ip_list[req_index] = ip_list[req_index], ip_list[i]

def arrange_list(ip_list):
    cusomized_sort(ip_list)

def main():
    ip_list = [0, 4, 5, 3, 7, 2, 1]
    print('ip=>',ip_list)
    arrange_list(ip_list)
    print('op=>',ip_list)

if __name__ == '__main__':
    main()