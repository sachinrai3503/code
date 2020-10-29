// https://www.geeksforgeeks.org/product-array-puzzle-set-2-o1-space/
/*
Given an array arr[] of n integers, construct a Product Array prod[] 
(of same size) such that prod[i] is equal to the product of all the 
elements of arr[] except arr[i]. Solve it without division operator and in O(n).

Example:

Input: arr[] = {10, 3, 5, 6, 2}
Output: prod[] = {180, 600, 360, 300, 900}
The elements of output array are 
{3*5*6*2, 10*5*6*2, 10*3*6*2, 
10*3*5*2, 10*3*5*6}
*/

#include <stdio.h>
#include <math.h>
#define EPS 1e-9 // epsilon value to maintain precision 

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void set_product(int ip[], int length){
    int t_prod = 1;
    int i = 0;
    for(;i<length;i++){
        t_prod*=ip[i];
    }
    double log_t_prod = log10(t_prod);
    for(i=0;i<length;i++){
        ip[i] = (int)(EPS + pow(10,log_t_prod-log10(ip[i])));
    }
}

void set_product2(int ip[], int length){
    double t_prod = 1.0;
    int i = 0;
    for(;i<length;i++){
        t_prod*=ip[i];
    }
    for(i=0;i<length;i++){
        ip[i] = (int)(t_prod * pow(ip[i],-1));
    }
}

int main(){
    int ip[] = {1,2,3,4};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    // set_product(ip,length);
    set_product2(ip,length);
    print_arr(ip,length);
}