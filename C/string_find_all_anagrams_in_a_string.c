// https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

/*
Given a string s and a non-empty string p, find all the start indices of p's 
anagrams in s.

Strings consists of lowercase English letters only and the length of both 
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]
*/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void printArr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int* getCountArr(char *ip, int length){
    int *op = (int*)calloc(26,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        op[ip[i]-97]++;
    }
    return op;
}

int isEqual(int *ip, int *ip2, int length){
    int i = 0;
    for(;i<length;i++){
        if(ip[i]!=ip2[i]) return 0;
    }
    return 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findAnagrams(char * s, char * p, int* returnSize){
    int lengthS = strlen(s);
    int lengthP= strlen(p);
    int *op = (int*)calloc(lengthS, sizeof(int));
    int k = 0;
    int *countArrP = getCountArr(p, lengthP);
    int *countArrS = (int*)calloc(26,sizeof(int));
    int i = 0;
    for(;i<lengthS;i++){
        countArrS[s[i]-97]++;
        if(i>=lengthP-1){
            if(isEqual(countArrS, countArrP, 26)) op[k++] = i-(lengthP-1);
            countArrS[s[i-(lengthP-1)]-97]--;
        }
    }
    *returnSize = k;
    return op;
}

int main(){
    char *text = "abab";
    char *pat = "ab";

    printf("Text=%s\n",text);
    printf("Pat=%s\n",pat);

    int k = 0;
    int *op = findAnagrams(text,pat,&k);
    printArr(op,k);
    return 0;
}