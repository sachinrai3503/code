// https://leetcode.com/problems/multiply-strings
// https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists
/**
Given two non-negative integers num1 and num2 represented as strings, return the
 product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself. 
*/

#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef struct List_Node{
    int val;
    struct List_Node *next;
}list_node;

list_node* init_node(int value){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->val = value;
        node->next = NULL;
    }
    return node;
}

int get_len(list_node *head){
    int len = 0;
    for(;head;head=head->next)
        len+=1;
    return len;
}

char* to_chars(list_node *head){
    char *nums = (char*)calloc(get_len(head)+1, sizeof(char));
    while(head){
        if(head->val!=0) break;
        head = head->next;
    }
    if(!head) return "0";
    int i = 0;
    for(;head;head=head->next){
        nums[i] = (head->val)+48;
        i+=1;
    }
    nums[i] = '\0';
    return nums;
}

list_node* to_list(char* nums, int nums_len){
    list_node *head = NULL, *prev = NULL;
    int i = nums_len-1;
    for(;i>=0;i--){
        list_node *node = init_node(nums[i]-48);
        if(!head) head = node;
        else prev->next = node;
        prev = node;
    }
    return head;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->val);
    }
    printf("\n");
}

list_node* reverse_list(list_node* head){
    list_node *p = head;
    list_node *q = NULL, *r = NULL;
    while(p){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
    }
    return q;
}

list_node* multiple_list_with_num(list_node *head, int num, list_node *op){
    if(!head) return op;
    list_node *new_head = op;
    int carry = 0, a = 0;
    list_node *prev = NULL;
    while(head){
        a = head->val;
        if(!op){
            op = init_node(0);
            if(!new_head) new_head = op;
            if(prev) prev->next = op;
        }
        int t_op = op->val + (a*num) + carry;
        op->val = (t_op)%10;
        carry = (t_op)/10;
        prev = op;
        op = op->next;
        head = head->next;
    }
    if(carry){
        prev->next = init_node(carry);
    }
    // print_list(new_head);
    return new_head;
}

list_node* multiply_list(list_node *list1, list_node *list2){
    if(!list2 || !list1) return NULL;
    list_node *head = NULL;
    list_node *op = NULL, *prev = NULL;
    while(list2){
        int num = list2->val;
        op = multiple_list_with_num(list1, num, op);
        if(!head) head = op;
        else prev->next = op;
        prev = op;
        op = op->next;
        list2 = list2->next;
    }
    // print_list(head);
    return head;
}

char * multiply(char * num1, char * num2){
    int num1_len = strlen(num1);
    int num2_len = strlen(num2);
    list_node *list1 = to_list(num1, num1_len);
    list_node *list2 = to_list(num2, num2_len);
    // print_list(list1);
    // print_list(list2);
    list_node *op = reverse_list(multiply_list(list1, list2));
    // print_list(op);
    return to_chars(op);   
    // return NULL;
}