// https://www.geeksforgeeks.org/burst-balloon-to-maximize-coins/
// https://leetcode.com/problems/burst-balloons/
/*
We have been given N balloons, each with a number of coins associated with it.
On bursting a balloon i, the number of coins gained = to A[i-1]*A[i]*A[i+1].
Also, balloons i-1 and i+1 now become adjacent. 

Find the maximum possible profit earned after bursting all the balloons. 
Assume an extra 1 at each boundary.

Examples: 
Input : 5, 10
Output : 60
Explanation - First Burst 5, Coins = 1*5*10
              Then burst 10, Coins+= 1*10*1
              Total = 60

Input : 1, 2, 3, 4, 5
Output : 110
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_2D(int (*ip)[50], int row, int col){
    int i = 0;
    for(;i<row;i++){
        print_arr(ip[i],col);
    }
}

int get_max_coins(int *balloons, int count){
    if(count<=0){
        printf("Invalid count\n");
        return INT_MIN;
    }
    int op[50][50];
    int k = 0;
    for(;k<count;k++){
        int i = (count-1) - k;
        int j = count-1;
        for(;i>=0 && j>=0;i--,j--){
            int max_coins = INT_MIN;
            int left_i = (i>0)?balloons[i-1]:1;
            int right_j = (j<count-1)?balloons[j+1]:1;
            int p = i;
            for(;p<=j;p++){
                int left_p = 0;
                int right_p = 0;
                int with_p = 0;
                if(p>i) left_p = op[i][p-1];
                if(p<j) right_p = op[p+1][j];
                with_p = balloons[p]*left_i*right_j;
                int t_coins = left_p + with_p + right_p;
                if(t_coins>max_coins) max_coins = t_coins;
            }
            op[i][j] = max_coins;
        }
    }
    print_2D(op,count,count);
    return op[0][count-1];
}

int main(){

    int balloons[] = {3,1,5,8};
    int length = sizeof(balloons)/sizeof(balloons[0]);

    printf("balloons >>");
    print_arr(balloons,length);

    int max_coin = get_max_coins(balloons,length);
    printf("Max Coins = %d",max_coin);

    return 0;
}