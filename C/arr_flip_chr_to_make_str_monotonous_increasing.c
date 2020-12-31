//  https://leetcode.com/problems/flip-string-to-monotone-increasing/
/*
A string of '0's and '1's is monotone increasing if it consists of some number 
of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or 
a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

Example 1:
Input: "00110"
Output: 1

Example 2:
Input: "010110"
Output: 2

Example 3:
Input: "00011000"
Output: 2

Note:
1 <= S.length <= 20000
S only consists of '0' and '1' characters.
*/

#include <string.h>

int getMin(int a, int b){
    return (a<b)?a:b;
}

int minFlipsMonoIncr(char * S){
    int length = strlen(S);
    int cost_0 = 0;
    int cost_1 = 0;
    int i = length-1;
    for(;i>=0;i--){
        if(S[i]=='0'){
            cost_0 = getMin(cost_0, cost_1);
            cost_1 = 1 + cost_1;
        }else{
            cost_0 = 1 + getMin(cost_0, cost_1);
        }
    }
    return getMin(cost_0, cost_1);
}