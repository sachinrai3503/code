// https://www.geeksforgeeks.org/largest-number-possible-after-removal-of-k-digits/
/*
 *Given a positive number N, the target is to find the largest number that can be formed
  after removing any K digits from N.

Examples: 
Input: N = 6358, K = 1 
Output: 658

Input: N = 2589, K = 2 
Output: 89   
 */

// Better stack based solution in str_smallest_num_after_removing_k_digit.py

#include <stdio.h>
#include <limits.h>

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int get_max_num_after_k_removal(int num, int k){
    int max_num = INT_MIN;
    int t_num = num;
    int i = 0;
    for(;i<k;i++){
        max_num = INT_MIN;
        int j = 1;
        while(t_num/j>0){
            int op = (t_num/(j*10))*j + (t_num%j);
            max_num = get_max(max_num, op);
            j*=10;
        }
        t_num = max_num;
        printf("%d\n", t_num);
    }
    return max_num;
}

int main(){
    int num = 2589;
    int k = 5;
    printf("%d ",get_max_num_after_k_removal(num, k));
    return 0;
}