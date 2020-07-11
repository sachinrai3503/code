// https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
/*
Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[]) 
that prints all occurrences of pat[] in txt[].
You may assume that n > m.

Examples:

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
*/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>
#include <string.h>

void print_int_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int* get_longest_proper_prefix(char *ip, int length){
    int *lps = (int*)calloc(length,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        int j = i-1;
        while(j>0 && ip[lps[j]]!=ip[i]){
            j = lps[j]-1;
        }
        if(j==-1){
            lps[i] = 0;
        }else if(ip[lps[j]]==ip[i]){
            lps[i] = lps[j] + 1;
        }else{
            lps[i] = 0;
        }
    }
    return lps;
}

void find_substring_positions(char *text, int txt_len, char *pat, int pat_len){
    int *longest_proper_prefix = get_longest_proper_prefix(pat,pat_len);
    // print_int_arr(longest_proper_prefix,pat_len);
    int j = 0;
    int i = 0;
    for(;i<txt_len;){
        if(text[i]==pat[j]){
            i++;
            j++;
        }else if(j==0){
            i++;
        }else{
            j = longest_proper_prefix[j-1];
        }
        if(j==pat_len){
            printf("Pattern %s found in text %s at %d.\n",pat,text,i-pat_len);
            j = longest_proper_prefix[j-1];
        }
    }
}

int main(){
    char *text = "GeeksforGeeks A computer science portal for geeks";
    int txt_len = strlen(text);
    char *pat = "technical";
    int pat_len = strlen(pat);

    printf("text = %s\n",text);
    printf("pat = %s\n",pat);

    find_substring_positions(text,txt_len,pat,pat_len);

    return 0;
}