# https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
# https://www.geeksforgeeks.org/rearrange-characters-in-a-string-such-that-no-two-adjacent-are-same-using-hashing/
# https://leetcode.com/problems/reorganize-string/
"""
Given a string S, check if the letters can be rearranged so that two characters
 that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].
"""

def get_freq_and_max_freq_char(S):
    freq = [0]*26
    if not S or len(S)==0: return freq, None
    max_freq_char = None
    max_freq = 0
    for char in S:
        index = ord(char)-97
        freq[index]+=1
        if freq[index]>max_freq:
            max_freq = freq[index]
            max_freq_char = char
    return freq, max_freq_char

class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        if S is None or length==0: return ''
        freq, max_freq_char = get_freq_and_max_freq_char(S)
        chr_index = ord(max_freq_char)-97
        if (length%2==0 and freq[chr_index]>(length//2)) or\
           (length%2==1 and freq[chr_index]>((length-1)//2 + 1)): return ''
        op = [None]*length
        i = 0
        while freq[chr_index]>0:
            op[i] = max_freq_char
            freq[chr_index]-=1
            i+=2
        for j in range(26):
            if freq[j]==0: continue
            else:
                while(freq[j]>0):
                    i = i if i<length else 1
                    op[i] = chr(j+97)
                    i+=2
                    freq[j]-=1
        return ''.join(op)