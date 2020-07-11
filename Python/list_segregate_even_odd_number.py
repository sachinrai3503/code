# https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/
"""
Given an array A[], write a function that segregates even and odd numbers. 
The functions should put all even numbers first, and then odd numbers.
Example:

Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}
In the output, the order of numbers can be changed, i.e.,
 in the above example, 34 can come before 12 and 3 can come before 9.
"""

def segregate_even_odd_num(ip_list):
    even_index, odd_index = 0, len(ip_list)-1
    i = 0
    while i <= odd_index:
        if ip_list[i]%2==0:
            ip_list[i], ip_list[even_index] = ip_list[even_index], ip_list[i]
            if i==even_index:
                i+=1
            even_index+=1
        else:
            ip_list[i], ip_list[odd_index] = ip_list[odd_index], ip_list[i]
            if i==odd_index:
                i+=1
            odd_index-=1

def main():
    ip_list = [1 ,3 ,2 ,4 ,7 ,6 ,9 ,10]
    print(ip_list)
    segregate_even_odd_num(ip_list)
    print('After segregating')
    print(ip_list)

if __name__ == '__main__':
    main()
