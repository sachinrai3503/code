// https://leetcode.com/problems/generate-parentheses/
// https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/
/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed
 parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
*/

void print_arr(char *arr, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%c",arr[i]);
    }
    printf("\n");
}

char* clone_arr(char *arr, int length){
    char *op = (char*)calloc(length+1, sizeof(char));
    if(op){
        int i = 0;
        for(;i<length;i++){
            op[i] = arr[i];
        }
        op[i] = '\0';
    }
    return op;
}

void get_all_parantheses(int rem_open, int rem_close, char *op, int i, int length, char **op_list, int *index){
    if(i==length){
        op_list[(*index)++] = clone_arr(op,length);
    }else{
        if(rem_open>0){
            op[i] = '(';
            get_all_parantheses(rem_open-1, rem_close, op, i+1, length, op_list, index);
        }
        if(rem_close>0 && rem_close>rem_open){
            op[i] = ')';
            get_all_parantheses(rem_open, rem_close-1, op, i+1, length, op_list, index);
        }
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** generateParenthesis(int n, int* returnSize){
    char *op = (char*)calloc(n*2, sizeof(char));
    char **op_list = (char**)calloc(10000, sizeof(char*));
    int index = 0;
    get_all_parantheses(n, n, op, 0, n*2, op_list, &index);
    // printf("%d", index);
    *returnSize = index;
    return op_list;
}