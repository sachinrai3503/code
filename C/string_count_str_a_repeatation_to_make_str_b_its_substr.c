// https://leetcode.com/problems/repeated-string-match/
/*
Given two strings a and b, return the minimum number of times you should repeat
 string a so that string b is a substring of it. If it is impossible for b​​​​​​ to 
 be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and 
repeated 2 times is "abcabc".

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd",
 b is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2
Example 3:

Input: a = "a", b = "a"
Output: 1
Example 4:

Input: a = "abc", b = "wxyz"
Output: -1
*/

// Related question - string_chk_if_repeating_substr_forms_the_string.c
// Not an optimized solution

#include<string.h>

int repeatedStringMatch(char * a, char * b){
    int len_a = strlen(a);
    int len_b = strlen(b);
    int i = 0;
    for(;i<len_a;i++){
        int count = 1;
        int j = i;
        int k = 0;
        while(k<len_b && a[j]==b[k]){
            j++;
            k++;
            if(j==len_a && k!=len_b){
                count++;
                j = 0;
            }
        }
        if(k==len_b) return count;
    }
    return -1;
}