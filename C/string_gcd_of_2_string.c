// https://leetcode.com/problems/greatest-common-divisor-of-strings/
/*
For two strings s and t, we say "t divides s" if and only if s = t + ... + t
  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides 
both str1 and str2. 

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:
Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
 
Constraints:
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1 and str2 consist of English uppercase letters.
*/

//  Python version in str_gcd_of_2_string.py

#include <stdio.h>
#include <malloc.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int gcd(int a, int b){
    if(b==0) return a;
    return gcd(b,a%b);
}

int compare(char *s1, char *s2, int len){
    int i = 0;
    for(;i<len;i++){
        if(s1[i]!=s2[i]) return 0;
    }
    return 1;
}

int* lps(char *str, int length){
    int *op = (int*)calloc(length,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        int j = i-1;
        while(j>0 && str[op[j]]!=str[i]){
            j = op[j]-1;
        }
        if(j==-1){
            op[i] = 0;
        }else if(str[op[j]]==str[i]){
            op[i] = op[j]+1;
        }else{
            op[i] = 0;
        }
    }
    return op;
}

char * gcdOfStrings(char * str1, char * str2){
    int l1 = strlen(str1);
    int l2 = strlen(str2);
    int *lps1 = lps(str1, l1);
    int *lps2 = lps(str2, l2);
    // print_arr(lps1, l1);
    // print_arr(lps2, l2);
    int t_mid1 = l1/2;
    int t_mid2 = l2/2;
    if(l1%2) t_mid1++;
    if(l2%2) t_mid2++;
    if((lps1[l1-1] && lps1[l1-1]<t_mid1) || (lps2[l2-1] && lps2[l2-1]<t_mid2)) return "";
    int tl1 = l1 - lps1[l1-1];
    int tl2 = l2 - lps2[l2-1];
    if(tl1!=tl2) return "";
    else if(compare(str1, str2, tl1)){
        int t_l = tl1*gcd(l1/tl1, l2/tl2);
        str1[t_l] = '\0';
        return str1;
    }
    return "";
}