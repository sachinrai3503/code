# https://www.geeksforgeeks.org/length-of-the-longest-substring-with-consecutive-characters/
"""
Given a string str of lowercase alphabets, the task is to find the length of
 the longest sub-string of characters in alphabetical order i.e. string “dfabck”
  will return 3. 
  
Note that the alphabetical order here is considered circular 
i.e. a, b, c, d, e, …, x, y, z, a, b, c, ….

Examples:

Input: str = “abcabcdefabc”
Output: 6
Input: str = “zabcd”
Output: 5
"""

def get_length(ip_str):
    if not len(ip_str):
        return 0, ''
    s, e = 0, -1
    ts = 0
    count = 0
    expected_char = '\0'
    for i in range(len(ip_str)):
        if expected_char=='\0' or expected_char!=ip_str[i]:
            ts = i
        if (i-ts+1)==2:
            count+=1
        if (i-ts+1)>(e-s+1):
            e = i
            s = ts
        if ip_str[i]=='z':
            expected_char = 'a'
        else:
            expected_char = chr(ord(ip_str[i])+1)
    return (e-s+1), ip_str[s:e+1], count

def main():
    ip_str = 'qwertyuiopasdfghjklzxcvbnm'
    print('Ip=',ip_str)
    max_len, substr, substr_count = get_length(ip_str)
    print('Length=',max_len)
    print('Substr=',substr)
    print('Count=',substr_count)

if __name__ == '__main__':
    main()