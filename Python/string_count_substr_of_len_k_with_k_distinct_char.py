# https://www.geeksforgeeks.org/count-of-substrings-of-length-k-with-exactly-k-distinct-characters/
"""
Given a string str of lowercase alphabets and an integer K, the task is to
 count all substrings of length K which have exactly K distinct characters.

Example:

Input: str = “abcc”, K = 2
Output: 2
Only two valid substrings exist {“ab”, “bc”}.

Input: str = “aabab”, K = 3
Output: 0
"""

def get_index(chr):
    index = ord(chr)
    if index>96 and index<123: return index-97
    else: return index-65


def get_substr_count_with_k_distinct_char_with_len_k(ip_str, k):
    count = 0
    s = 0
    char_count_list = [0 for i in range(26)]
    dist_char = 0
    for i in range(len(ip_str)):
        char_index = get_index(ip_str[i])
        char_count_list[char_index]+=1
        if char_count_list[char_index]==1:
            dist_char+=1
        if (i-s+1)==k:
            if dist_char==k:
                count+=1
            char_index = get_index(ip_str[s])
            char_count_list[char_index]-=1
            if char_count_list[char_index]==0:
                dist_char-=1
            s+=1
    return count

def main():
    ip_str = "aabcdabbcdc"
    print('ip=',ip_str)
    for k in range(len(ip_str)+1):
        print('k=',k,'count=',
            get_substr_count_with_k_distinct_char_with_len_k(ip_str,k))

if __name__ == '__main__':
    main()