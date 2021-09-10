// https://leetcode.com/problems/k-th-symbol-in-grammar/
/**
On the first row, we write a 0. Now in every subsequent row, we look at the
 previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row n and index k, return the kth indexed symbol in row n. 
(The values of k are 1-indexed.) (1 indexed).

Examples:
Input: n = 1, k = 1
Output: 0

Input: n = 2, k = 1
Output: 0

Input: n = 2, k = 2
Output: 1

Input: n = 4, k = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:
n will be an integer in the range [1, 30].
k will be an integer in the range [1, 2n-1].
 * 
*/
int calculate(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    int prev = calculate(n/2);
    if(prev==1){
        if(n%2==0) return 1;
        return 0;
    }else{
        if(n%2==0) return 0;
        return 1;
    }
}

int kthGrammar(int n, int k){
    return calculate(k-1);
}