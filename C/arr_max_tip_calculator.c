// https://www.hackerearth.com/problem/algorithm/maximum-tip-calculator-tcs-amazon/
// https://www.geeksforgeeks.org/maximum-tip-calculator-2/
// https://www.geeksforgeeks.org/maximum-tip-calculator/

/*
Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant
 received N orders. The amount of tips may differ when handled by different waiters,
 if Rahul takes the ith order, he would be tipped Ai rupees and if Ankit takes this order, 
 the tip would be Bi rupees.
In order to maximize the total tip value they decided to distribute the order among themselves.
 One order will be handled by one person only. Also, due to time constraints Rahul cannot 
 take more than X orders and Ankit cannot take more than Y orders. It is guaranteed that X + Y
 is greater than or equal to N, which means that all the orders can be handled by either Rahul
 or Ankit. Find out the maximum possible amount of total tip money after processing all the orders.

Input:

•    The first line contains one integer, number of test cases.
•    The second line contains three integers N, X, Y.
•    The third line contains N integers. The ith integer represents Ai.
•    The fourth line contains N integers. The ith integer represents Bi.

Output:
Print a single integer representing the maximum tip money they would receive.

Constraints:
1 ≤ N ≤ 105
1 ≤ X, Y ≤ N; X + Y ≥ N
1 ≤ Ai, Bi ≤ 104

Example:
Input:
1
5 3 3
1 2 3 4 5
5 4 3 2 1

Output:
21
*/

#include <stdio.h>
#include <malloc.h>

int get_max(int a, int b){
	if(a>b)  return a;
	return b;
}

int max_tip_calculator(int *A, int *B, int n, int x, int y){
    int *dp_op = (int*)calloc(n, sizeof(int));
	int max_tip = 0;
    int i = 0;
	for(;i<n;i++){
        int prev = 0;
        int j = n-1;
		for(;j>=0;j--){
            int with_A = 0;
			int without_A = 0;
            if(i>0) with_A = A[j] + prev;
            without_A = B[j] + ((j<n-1)?dp_op[j+1]:0);
            int t_prev = dp_op[j];
            dp_op[j] = get_max(with_A, without_A);
            prev = t_prev;
		}
        if(i<=x && (n-i)<=y)
            max_tip = get_max(max_tip, dp_op[0]);
	}
    return max_tip;
}

int main(){
    int tc_count = 0;
	scanf("%d\n",&tc_count);
    int i = 0;
	for(;i<tc_count;i++){
        int n,x,y;
		scanf("%d %d %d\n",&n, &x, &y);
        int *A = (int*)calloc(n, sizeof(int));
		int *B = (int*)calloc(n, sizeof(int));
		int j = 0;
		for(;j<n;j++){
			if(j<n-1) scanf("%d ",A+j);
			else scanf("%d\n",A+j);
		}
		j = 0;
		for(;j<n;j++){
			if(j<n-1) scanf("%d ",B+j);
			else scanf("%d\n",B+j);
		}
		printf("%d", max_tip_calculator(A, B, n, x, y));
	}
	return 0;
}