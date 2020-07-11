# https://www.geeksforgeeks.org/even-numbers-even-index-odd-numbers-odd-index/
"""
Given an array of size n containing equal number of odd and even numbers.
The problem is to arrange the numbers in such a way that all 
the even numbers get the even index and odd numbers get the odd index.

Required auxiliary space is O(1).

Examples :

Input : arr[] = {3, 6, 12, 1, 5, 8}
Output : 6 3 12 1 8 5 

Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
Output : 10 9 18 7 20 19 4 13 14 21 
"""

def is_correct_position(index, num):
    if num%2==0 and index%2==0:
        return True
    elif num%2==1 and index%2==1:
        return True
    else:
        return False

def arrange_list(ip_list):
    if len(ip_list)%2==1:
        print('Provide equal even and odd numbers')
        return
    even_index, odd_index = 0, 1
    i = 0
    while i<len(ip_list):
        if(ip_list[i]%2==0):
            if is_correct_position(i,ip_list[i]):
                if i==even_index:
                    even_index+=2
                i+=1
                
            else:
                ip_list[i], ip_list[even_index] = ip_list[even_index], ip_list[i]
                even_index+=2
        else:
            if is_correct_position(i,ip_list[i]):
                if i==odd_index:
                    odd_index+=2
                i+=1
            else:
                ip_list[i], ip_list[odd_index] = ip_list[odd_index], ip_list[i]
                odd_index+=2

def main():
    ip_list = [10, 9, 7, 18, 13, 19, 4, 20, 21, 14]
    print('ip =>',ip_list)
    arrange_list(ip_list)
    print('op =>',ip_list)

if __name__ == '__main__':
    main()