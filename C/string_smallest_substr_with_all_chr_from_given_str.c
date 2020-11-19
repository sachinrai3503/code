// https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
// https://leetcode.com/problems/minimum-window-substring/
/*
Given two strings string1 and string2, the task is to find the smallest 
substring in string1 containing all characters of string2 efficiently.

Examples:

Input: string = “this is a test string”, pattern = “tist”
Output: Minimum window is “t stri”
Explanation: “t stri” contains all the characters of pattern.

Input: string = “geeksforgeeks”, pattern = “ork”
Output: Minimum window is “ksfor”
*/

#include <stdio.h>
#include <malloc.h>
#include <string.h>

void print_arr(char *ip, int s, int e){
    int i = s;
    for(;i<=e;i++){
        printf("%c",ip[i]);
    }
    printf("\n");
}

int to_index(char c){
    if(c>=65 && c<=90) return 26 + c-65;
    if(c>=97 && c<=122) return c-97;
    return -1;
}

int* get_count_arr(char *ip, int length){
    int *count = (int*)calloc(52,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        count[to_index(ip[i])]++;
    }
    return count;
}


int minWindow(char * s, char * t){
    int len_s = strlen(s);
    int len_t = strlen(t);
    if(len_t==0 || len_s==0) return 0;
    if(len_s<len_t){
       return -1;
    }
    int *req_count = get_count_arr(t,len_t);
    int *cur_count = (int*)calloc(52,sizeof(int));
    int min_s = 0, min_e = -1;
    int t_s = 0, count = 0;
    int _1st_occ_flag = 1;
    int i = 0;
    for(;i<len_s;i++){
        if(s[i]==' ') continue;
        int index = to_index(s[i]);
        cur_count[index]++;
        if(cur_count[index]<=req_count[index])
            count++;
        int ts_index = to_index(s[t_s]);
        while(t_s<=i && (s[t_s]==' ' || 
              cur_count[ts_index]>req_count[ts_index])){
            if(s[t_s]!=' ')
                cur_count[ts_index]--;
            t_s++;
            ts_index = to_index(s[t_s]);
        }
        if(count==len_t && (_1st_occ_flag || (i-t_s+1)<(min_e-min_s+1))){
            _1st_occ_flag = 0;
            min_e = i;
            min_s = t_s;
        }
    }
    print_arr(s,min_s,min_e);
    return min_e-min_s+1;
}

int main(){
    char *str = "    this is a tes t  st  ring";
    char *pat = "tist";
    printf("Str>>%s\n",str);
    printf("Path>>%s\n",pat);

    int len = minWindow(str,pat);
    printf("Min window len=%d\n",len);

    return 0;
}