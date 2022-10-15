# https://leetcode.com/problems/longest-palindromic-subsequence-ii/
# https://leetcode.ca/2020-07-08-1682-Longest-Palindromic-Subsequence-II/
"""
A subsequence of a string s is considered a good palindromic subsequence if:
	It is a subsequence of s.
	It is a palindrome (has the same value if reversed).
	It has an even length.
	No two consecutive characters are equal, except the two middle ones.

For example, if s = "abcabcabb", then "abba" is considered a good palindromic subsequence,
 while "bcb" (not even length) and "bbbb" (has equal consecutive characters) are not.

Given a string s, return the length of the longest good palindromic subsequence in s.

Example 1:
Input: s = “bbabab”
Output: 4
Explanation: The longest good palindromic subsequence of s is “baab”.

Example 2:
Input: s = “dcbccacdb”
Output: 4
Explanation: The longest good palindromic subsequence of s is “dccd”.

Constraints:
1 <= s.length <= 250
s consists of lowercase English letters.
"""

# NOTE - This might not be correct solution but has passed all the test cases till now.

def get_len_of_good_palin(s):
    s_len = len(s)
    dp = [(0, 0) for i in range(s_len)] # (length, 1st chr of palin)
    for i in range(s_len-1, -1, -1):
        prev = (0, 0)
        for j in range(i+1, s_len):
            t_prev = dp[j]
            shift_by = ord(s[j])-97
            j_bit_set = 1<<shift_by
            if s[i]==s[j]:
                if j==(i+1): dp[j] = (2, j_bit_set)
                else:
                    if prev[0]==0: # no palin from s[i+1:j-1]
                        dp[j] = (2, j_bit_set)
                    elif prev[1] & j_bit_set == 0: # palin in s[i+1:j-1] starts with char!=s[j]
                        dp[j] = (prev[0]+2, j_bit_set)
                    elif prev[1] | j_bit_set == j_bit_set: # palin in s[i+1:j-1] start with only char==s[j]
                        dp[j] = (prev[0], j_bit_set)
                    else:# palin in s[i+1:j-1] start with s[j] and other chars
                        dp[j] = (prev[0]+2, j_bit_set)
            else:
                v1 = dp[j-1] # s[i:j-1]
                v2 = dp[j] # s[i+1:j]
                if v1[0]>v2[0]:
                    dp[j] = (v1[0], v1[1])
                elif v1[0]<v2[0]:
                    dp[j] = (v2[0], v2[1])
                else:
                    dp[j] = (v1[0], v1[1]|v2[1])
            prev = t_prev
    print(dp)
    return dp[-1]

def main():
    s = 'bbabab'
    print(get_len_of_good_palin(s))

if __name__ == '__main__':
    main()