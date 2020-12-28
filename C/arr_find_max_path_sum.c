// https://www.geeksforgeeks.org/maximum-path-sum-matrix/
// https://www.geeksforgeeks.org/maximum-path-sum-starting-cell-0-th-row-ending-cell-n-1-th-row/
/*
Given a matrix of N * M. Find the maximum path sum in matrix. 
The maximum path is sum of all elements from first row to last row where you
 are allowed to move only down or diagonally to left or right.

You can start from any element in first row.

Examples:

Input : mat[][] = 10 10  2  0 20  4
                   1  0  0 30  2  5
                   0 10  4  0  2  0
                   1  0  2 20  0  4
Output : 74
The maximum sum path is 20-30-4-20.

Input : mat[][] = 1 2 3
                  9 8 7
                  4 5 6
Output : 17
The maximum sum path is 3-8-6.
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

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

int find_max_path_sum(int (*ip)[50], int row, int col){
    int max_sum = INT_MIN;
    int op[2][50] = {{0},{0}};
    int i = row-1;
    for(;i>=0;i--){
        int cur_row = (i%2);
        int prev_row = (cur_row==1)?0:1;
        int j = 0;
        for(;j<col;j++){
            int left = INT_MIN, right = INT_MIN, down = INT_MIN;
            if(i==row-1) op[cur_row][j] = ip[i][j];
            else{
                if(j>0) left = op[prev_row][j-1];
                if(j<col-1) right = op[prev_row][j+1];
                down = op[prev_row][j];
                op[cur_row][j] = ip[i][j] + get_max(get_max(left,down),right);
            }
            if(i==0) max_sum = get_max(max_sum,op[cur_row][j]); 
        }
    }
    return max_sum;
}

int main(){
    int ip[50][50] = { {4, 2, 3, 4},
                      {2, 9, 1, 10},
                      {15, 1, 3, 0},
                      {16, 92, 41, 44} };
    int row = 4;
    int col = 4;

    print_2D(ip,row,col);
    printf("Max path sum = %d\n",find_max_path_sum(ip,row,col));
}