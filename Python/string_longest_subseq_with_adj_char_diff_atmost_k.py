# https://www.geeksforgeeks.org/longest-subsequence-having-difference-atmost-k/
"""
Given a string S of length N and an integer K, 
the task is to find the length of longest sub-sequence 
such that the difference between the ASCII values of adjacent
 characters in the subsequence is not more than K.

Examples:

Input: N = 7, K = 2, S = "afcbedg"
Output: 4
Input: N = 13, K = 3, S = "geeksforgeeks"
Output: 7
"""

def get_diff(a, b):
    return (a-b) if a>b else (b-a)

def get_max(a, b):
    return a if a>b else b

def get_min(a, b):
    return a if a<b else b

def longest_subseq_with_adj_diff_atmost_k(text,k):
    max_subseq_len = 0
    subseq_len_list = [0]*len(text)
    for i in range(len(text)-1,-1,-1):
        t_len = 0
        for j in range(i+1,len(text),1):
            if get_diff(ord(text[j]),ord(text[i]))<=k:
                t_len = get_max(t_len,subseq_len_list[j])
        subseq_len_list[i] = t_len+1
        max_subseq_len = get_max(max_subseq_len,subseq_len_list[i])
    # print(subseq_len_list)
    return max_subseq_len

def longest_subseq_with_adj_diff_atmost_k_2(text,k):
    max_subseq_len = 0
    subseq_len_list = [0]*26
    for i in range(len(text)-1,-1,-1):
        t_len = 0
        char_index = get_diff(ord(text[i]),ord('a'))
        s = get_max(0,char_index-k)
        e = get_min(25,char_index+k)
        for j in range(s,e+1):
            t_len = get_max(t_len,subseq_len_list[j])
        subseq_len_list[char_index] = t_len+1
        max_subseq_len = get_max(max_subseq_len,subseq_len_list[char_index])
    return max_subseq_len

def main():
    text = 'zgeeksforgeeks'
    k = 3
    print('ip=>',text)
    print('k=',k)
    print('Longest subseq len =>',longest_subseq_with_adj_diff_atmost_k(text,k))
    print('Longest subseq len 2nd method =>',longest_subseq_with_adj_diff_atmost_k_2(text,k))

if __name__ == '__main__':
    main()