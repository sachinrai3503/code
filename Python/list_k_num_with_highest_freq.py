# https://www.geeksforgeeks.org/find-k-most-frequent-in-linear-time/
"""
Given an array of integers, we need to print k most frequent elements. 
Incase of a tie, prefer the elements whose first appearance is first.

Examples:

Input : arr[] = {10, 5, 20, 5, 10, 10, 30}, k = 2
Output : 10 5

Input : arr[] = {7, 7, 6, 6, 6, 7, 5, 4, 4, 10, 5}, k = 3
Output : 7 6 5
Explanation :
In this example, 7 and 6 have same frequencies. 
We print 7 first because first appearance of 7 is first.
5 and 4 have same frequencies but print 5 as occurs first.
"""

# Heap based sol. at arr_k_num_with_highest_freq.c

def print_top_k_freq_num(ip_list, k):
    key_freq_dict = dict()
    freq_key_dict = dict()
    for num in ip_list:
        if key_freq_dict.__contains__(num):
            key_freq_dict[num]+=1
        else:
            key_freq_dict[num] = 1
    for num in ip_list:
        freq = key_freq_dict[num]
        if freq_key_dict.__contains__(freq):
            key_list = freq_key_dict[freq]
            if not key_list.__contains__(num):
                key_list.append(num)
        else:
            key_list = list()
            key_list.append(num)
            freq_key_dict[freq] = key_list
    reversed_sorted_freq_list = reversed(sorted(freq_key_dict.keys()))
    count = 0
    for freq in reversed_sorted_freq_list:
        key_list = freq_key_dict[freq]
        for key in key_list:
            if count>=k:
                return
            print(key,':',freq,sep='',end=' ')
            count+=1

def main():
    ip_list = [7, 7, 6, 6, 6, 7, 5, 4, 4, 10, 5]
    print('ip>>',ip_list)
    for k in range(len(ip_list)+1):
        print('k=',k,end=' >>')
        print_top_k_freq_num(ip_list,k)
        print()

if __name__ == '__main__':
    main()