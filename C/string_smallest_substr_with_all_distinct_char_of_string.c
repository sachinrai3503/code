// https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
// https://www.geeksforgeeks.org/length-smallest-sub-string-consisting-maximum-distinct-characters/
/*
Given a string, find the smallest window length with all distinct characters 
of the given string. 

Examples:

Input: aabcbcdbca
Output: dbca

Input: aaab
Output: ab
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

int minWindow(char * s){
    int len_s = strlen(s);
    if(len_s==0) return 0;
    int *cur_count = (int*)calloc(52,sizeof(int));
    int min_s = 0, min_e = -1;
    int t_s = 0, count = 0;
    int max_count = 0; // Count of max distinct char so far
    int i = 0;
    for(;i<len_s;i++){
        int index = to_index(s[i]);
        cur_count[index]++;
        if(cur_count[index]==1)
            count++;
        int ts_index = to_index(s[t_s]);
        while(t_s<=i && cur_count[ts_index]>1){
            cur_count[ts_index]--;
            ts_index = to_index(s[++t_s]);
        }
        if(count>max_count || (i-t_s+1)<(min_e-min_s+1)){
            min_e = i;
            min_s = t_s;
            max_count = count;
        }
    }
    print_arr(s,min_s,min_e);
    return min_e-min_s+1;
}

int main(){
    char *str = "GEEKSGEEKSFOR";
    printf("Str>>%s\n",str);

    int len = minWindow(str);
    printf("Min window len=%d\n",len);

    return 0;
}