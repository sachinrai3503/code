# https://www.geeksforgeeks.org/check-possible-sort-array-conditional-swapping-adjacent-allowed/?ref=rp
"""
We are given an unsorted array of integers in the range from 0 to n-1.
We are allowed to swap adjacent elements in array many number of times but 
only if the absolute difference between these element is 1. 

Check if it is possible to sort the array.If yes then print “yes” else “no”.

Examples:
Input : arr[] = {1, 0, 3, 2}
Output : yes

Input : arr[] = {2, 1, 0}
Output : no
"""

def get_diff(a, b):
    return (a-b) if a>b else (b-a)

def can_be_sorted(ip_list):
    for i in range(len(ip_list)-1,0,-1):
        if ip_list[i] < ip_list[i-1]:
            if get_diff(ip_list[i],ip_list[i-1])>1:
                return False
            else:
                ip_list[i], ip_list[i-1] = ip_list[i-1], ip_list[i]
    return True

def main():
    ip_list = [1, 0, 2, 5, 3, 4]
    print('Ip>',ip_list)
    print('Can be sorted =',can_be_sorted(ip_list))
    print('op>',ip_list)

if __name__ == '__main__':
    main()