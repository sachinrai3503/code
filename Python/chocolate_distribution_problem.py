# Chocolate Distribution Problem
"""
Given an array of n integers where each value represents number of chocolates in a packet. 
Each packet can have variable number of chocolates. 

There are m students, the task is to distribute chocolate packets such that:
 - Each student gets one packet.
 - The difference between the number of chocolates in packet with maximum chocolates
 and packet with minimum chocolates given to the students is minimum.

Input : arr[] = {7, 3, 2, 4, 9, 12, 56}
m = 3
Output: Minimum Difference is 2

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12}
m = 5
Output: Minimum Difference is 6

Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41,
30, 40, 28, 42, 30, 44, 48,
43, 50}
m = 7
Output: Minimum Difference is 10
"""

def distribute_chocolate_with_min_inequality(ip_list, m):
    if m<=0:
        print('Invalid no. of students.')
        return -99999999999
    min_diff = 99999999999999
    s, e = 0, -1
    ip_list.sort()
    i, j = 0, m-1
    while j<len(ip_list):
        if (ip_list[j]-ip_list[i]) < min_diff:
            min_diff = ip_list[j]-ip_list[i]
            s, e = i, j
        j+=1
        i+=1
    print(ip_list[s:e+1])
    return min_diff

def main():
    ip_list = [12, 4, 7, 9, 2, 23, 25, 41,30, 40, 28, 42, 30, 44, 48,43, 50]
    m = 7
    print('ip=>',ip_list)
    print('min diff =>',distribute_chocolate_with_min_inequality(ip_list,m))

if __name__ == '__main__':
    main()

