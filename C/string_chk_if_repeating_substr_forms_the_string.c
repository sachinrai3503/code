// https://www.geeksforgeeks.org/find-given-string-can-represented-substring-iterating-substring-n-times/
// https://leetcode.com/problems/repeated-substring-pattern/
/*
Given a string ‘str’, check if it can be constructed by taking a substring of
 it and appending multiple copies of the substring together.

Examples:
Input: str = "abcabcabc"
Output: true
The given string is 3 times repetition of "abc"

Input: str = "abadabad"
Output: true
The given string is 2 times repetition of "abad"

Input: str = "aabaabaabaab"
Output: true
The given string is 4 times repetition of "aab"

Input: str = "abcdabc"
Output: false
*/

// Related - string_count_str_a_repeatation_to_make_str_b_its_substr.c

#include <stdio.h>
#include <malloc.h>
#define false 0
#define true 1

typedef int bool;

void printArr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int* lps(char *s, int length){
    int *_lps = (int*)calloc(length,sizeof(int));
    int i = 0;
    while(i<length){
        int j = i-1;
        while(j>0 && s[_lps[j]]!=s[i]){
            j = _lps[j]-1;
        }
        if(j==-1) _lps[i] = 0;
        else if(s[_lps[j]]==s[i]) _lps[i] = _lps[j] + 1;
        else _lps[i] = 0;
        i++;
    }
    return _lps;
}

bool repeatedSubstringPattern(char * s){
    int length = strlen(s);
    int *_lps = lps(s, length);
    // printArr(_lps, length);
    int tLps = _lps[length-1];
    int expLPS = (length%2)?(length/2)+1:(length/2);
    if(tLps<expLPS) return false;
    int repeatingLength = length-tLps;
    if(length%repeatingLength) return false;
    return true;
}