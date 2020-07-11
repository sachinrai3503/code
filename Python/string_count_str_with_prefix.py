# https://www.geeksforgeeks.org/count-of-strings-whose-prefix-match-with-the-given-string-to-a-given-length-k/
"""
Find the count of strings in arr[]
 whose prefix of length k matches with the k 
    length prefix of str.

Examples:
Input: arr[] = {“abba”, “abbb”, “abbc”, “abbd”, “abaa”, “abca”}
        str = “abbg”
        k = 3
Output: 4
“abba”, “abbb”, “abbc” and “abbd” are the matching strings.

Input: arr[] = {“geeks”, “geeksforgeeks”, “forgeeks”}, str = “geeks”, k = 2
Output: 2
"""

def is_prefix(str1, str2, k):
    """
    Checks if 1st k char in str2 is prefix in str1.
    """
    if k>len(str1) or k>len(str2):
        return False
    for i in range(k):
        if str1[i] != str2[i]:
            return False
    return True

def count_string_with_prefix(str_list, ip_str, k):
    count = 0
    for string in str_list:
        if is_prefix(string,ip_str,k):
            print(string)
            count+=1
    return count

def main():
    str_list = ['abba', 'abbb', 'abbc', 'abbd', 'abaa', 'abca','geeksforgeeks','geeks','forgeeks']
    ip_string = 'geeks'
    k = 2
    print("str list>",str_list)
    print('ip_string>',ip_string)
    print('Prefix count with k as ',k,' = ',count_string_with_prefix(str_list,ip_string,k))

if __name__ == '__main__':
    main()