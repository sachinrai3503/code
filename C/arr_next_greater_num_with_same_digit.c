//https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
/*
Given a number n, find the smallest number that 
    has same set of digits as n and is greater than n. 
If n is the greatest possible number with its set of digits,
 then print “not possible”.

Examples:
For simplicity of implementation, we have considered input number as a string.

Input:  n = '218765'
Output: '251678'
*/

// Python sol. - <>

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void swap(int *a, int *b){
    (*a)^=(*b)^=(*a)^=(*b);
}

void reverse(int ip[], int s, int e){
    while(s<e){
        swap(ip+s,ip+e);
        s++;e--;
    }
}

int get_ceil_index(int ip[], int s, int e, int num){
    int ceil_index = INT_MIN;
    while(s<=e){
        int mid = (s+e)/2;
        if(ip[mid]<=num){
            e = mid-1;
        }else{
            ceil_index = mid;
            s = mid+1;
        }
    }
    return ceil_index;
}

int get_smaller_index(int ip[], int length){
    int i = length-1;
    for(;i>0 && ip[i]<=ip[i-1];i--);
    return i;
}

int* next_greater_num_with_same_digit(int ip[], int length){
    if(length<=0){
        printf("Invalid\n");
        return NULL;
    }
    int smaller_index = get_smaller_index(ip,length);
    if(smaller_index==0){
        printf("Not Possible\n");
        return ip;
    }
    int ceil_index = get_ceil_index(ip,smaller_index,length-1,ip[smaller_index-1]);
    swap(ip+ceil_index,ip+smaller_index-1);
    reverse(ip,smaller_index,length-1);
    return ip;
}

int main(){
    int ip[] = {5,3,4,9,7,6};
    int length = sizeof(ip)/sizeof(ip[0]);
    print_arr(ip,length);
    int *op = next_greater_num_with_same_digit(ip,length);
    print_arr(op,length);
}