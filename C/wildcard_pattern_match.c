// https://www.geeksforgeeks.org/wildcard-pattern-matching/
// https://www.geeksforgeeks.org/dynamic-programming-wildcard-pattern-matching-linear-time-constant-space/
// https://leetcode.com/problems/wildcard-matching/
/*
Given an input string (s) and a pattern (p), implement wildcard pattern matching
 with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false

Constraints:
0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
*/

// Note - Do check the related regular_expression_match.c. 
// That is more difficult than this but around the same logic.

#include <string.h>
#define false 0
#define true 1

typedef int bool;

bool isMatch(char * s, char * p){
    int l1 = strlen(s);
    int l2 = strlen(p);
    int i = 0, j = 0;
    int last_astric_index = -1;
    int chr_index_to_ignore = -1;
    while(i<l1){
        char a = s[i];
        char b = (j==l2)?'\0':p[j];
        if(b=='*'){
            last_astric_index = j;
            j++;
            chr_index_to_ignore = i;
        }else if(a==b || b=='?'){
            i++;
            j++;
        }else{
            if(last_astric_index==-1) return false;
            j = last_astric_index+1;
            i = ++chr_index_to_ignore;
        }
    }
    while(j<l2){
        if(p[j]!='*') return false;
        j++;
    }
    return true;
}