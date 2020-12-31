// https://leetcode.com/problems/count-and-say/
// https://www.geeksforgeeks.org/look-and-say-sequence/
/*
The count-and-say sequence is a sequence of digit strings defined by the 
recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from
 countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of
 groups so that each group is a contiguous section all of the same character.

Then for each group, say the number of characters, then say the character. To 
 convert the saying into a digit string, replace the counts with a number
 and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 
Constraints:
1 <= n <= 30
*/

#include <string.h>
#include <stdio.h>

int count(char *ip, int length, int from , char c){
    int _count = 0;
    int i = from;
    for(;i<length && ip[i]==c;i++){
        _count++;
    }
    return _count;
}

void reverse(char *ip, int s, int e){
    for(;s<e;s++,e--){
        char temp = ip[s];
        ip[s] = ip[e];
        ip[e] = temp;
    }
}

int appendToSeq(char *ip, int curLen, int count, char c){
    int i = curLen;
    while(count>0){
        ip[i++] = count%10 + 48;
        count/=10;
    }
    reverse(ip,curLen,i-1);
    ip[i++] = c;
    return i;
}

char * countAndSay(int n){
    if(n<=0) return '\0';
    char *op1 = (char*)calloc(5000,sizeof(char));
    char *op2 = (char*)calloc(5000,sizeof(char));
    int k1 = 0, k2 = 0;
    op1[0] = '1';
    k1 = 1;
    int i = 1;
    for(;i<n;i++){
        int k = 0;
        while(k<k1){
            int _count = count(op1, k1, k, op1[k]);
            k2 = appendToSeq(op2, k2, _count, op1[k]);
            k = k + _count;
        }
        char *temp = op1;
        op1 = op2;
        k1 = k2;
        op2 = temp;
        k2 = 0;
    }
    // printf("Len=%d\n",k1);
    return op1;
}