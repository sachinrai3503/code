// https://leetcode.com/problems/regular-expression-matching/
/*
Given an input string (s) and a pattern (p), implement regular expression
 matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false
 
Constraints:
0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
*/

// Note - Do check the related wildcard_pattern_match.c

#include <string.h>
#define false 0
#define true 1

typedef int bool;

bool isMatch(char * s, char * p){
    int l1 = strlen(s);
    int l2 = strlen(p);
    int dot_astric_index_p = -1;
    int chr_astric_index_p = -1;
    int chr1_index_to_ignore = -1;
    int chr2_index_to_ignore = -1;
    int i = 0;
    int j = 0;
    while(i<l1){
        char a = s[i];
        char b = (j<l2)?p[j]:'\0';
        if(j+1<l2 && p[j+1]=='*')
            b = '-';
        if(b=='-'){
            if(p[j]=='.'){
                dot_astric_index_p = j;
                chr1_index_to_ignore = i;
                chr_astric_index_p = chr2_index_to_ignore = -1;
            }else if(a==p[j]){
                chr_astric_index_p = j;
                chr2_index_to_ignore = i;
            }
            j+=2;
        }else if(a==b || b=='.'){
            i+=1;
            j+=1;
        }else{
            if(chr_astric_index_p!=-1){
                i = ++chr2_index_to_ignore;
                j = chr_astric_index_p+2;
                if(s[chr2_index_to_ignore]!=p[chr_astric_index_p]){
                    chr2_index_to_ignore=chr_astric_index_p=-1;
                }
            }else if(dot_astric_index_p!=-1){
                i = ++chr1_index_to_ignore;
                j = dot_astric_index_p+2;
            }else{
                return false;
            }
        }
    }
    while(j<l2){
        if(j+1<l2 && p[j+1]!='*') return false;
        else if(j+1>=l2) return false;
        j+=2;
    }
    return true;
}