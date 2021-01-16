// https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
/*
Given two strings A and B, the task is to convert A to B if possible. 
The only operation allowed is to put any character from A and insert it
 at front. Find if it’s possible to convert the string. If yes, then output min
 no. of operations required for transformation.

Examples:
Input:  A = "ABD", B = "BAD"
Output: 1
Explanation: Pick B and insert it at front.

Input:  A = "EACBD", B = "EABCD"
Output: 3
Explanation: Pick B and insert at front, EACBD => BEACD
             Pick A and insert at front, BEACD => ABECD
             Pick E and insert at front, ABECD => EABCD
*/

#include <stdio.h>
#include <string.h>
#include <malloc.h>

int* get_freq(char *ip, int length){
    int *freq = (int*)calloc(26, sizeof(int));
    int i = 0;
    for(;i<length;i++){
        freq[i-65]++;
    }
    return freq;
}

int compare_freq(char *ip1, int l1, char *ip2, int l2){
    int *freq1 = get_freq(ip1, l1);
    int *freq2 = get_freq(ip2, l2);
    int i = 0;
    for(;i<26;i++){
        if(freq1[i]!=freq2[i]) return 0;
    }
    return 1;
}

int get_min_operation_count(char *ip1, int l1, char *ip2, int l2){
    int count = 0;
    if(compare_freq(ip1,l1,ip2,l2)==0) return -1;
    int i = l1-1;
    int j = l2-1;
    while(i>=0 && j>=0){
        if(ip1[i]==ip2[j]){
            i--;
            j--;
        }else{
            count++;
            i--;
        }
    }
    return count;
}

int main(){
    char *ip1 = "AABDFSA";
    char *ip2 = "ABADFAS";
    int l1 = strlen(ip1);
    int l2 = strlen(ip2);

    printf("ip1 = %s\n",ip1);
    printf("ip2 = %s\n",ip2);

    printf("Min operation = %d\n",get_min_operation_count(ip1,l1,ip2,l2));

    return 0;
}