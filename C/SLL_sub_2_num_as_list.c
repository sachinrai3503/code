// https://www.geeksforgeeks.org/subtract-two-numbers-represented-as-linked-lists/
/*
Given two linked lists that represent two large positive numbers. Subtract the
 smaller number from the larger one and return the difference as a linked list.

Note that the input lists may be in any order, but we always need to subtract
 smaller from the larger ones.
It may be assumed that there are no extra leading zeros in input lists.

Examples: 
Input: l1 = 1 -> 0 -> 0 -> NULL,  l2 = 1 -> NULL
Output: 0->9->9->NULL
Explanation: Number represented as lists are 100 and 1, so 100 - 1 is 099

Input: l1 = 7-> 8 -> 6 -> NULL,  l2 = 7 -> 8 -> 9 NULL
Output: 3->NULL
Explanation: Number represented as 
lists are 786 and  789, so 789 - 786 is 3, as the smaller value is subtracted from 
the larger one.
*/

#include <stdio.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *next;
}list_node;

list_node* make_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

list_node* to_list(int *ip, int length){
    list_node *head = NULL;
    list_node *prev = NULL;
    int i = 0;
    for(;i<length;i++){
        list_node *temp = make_list_node(ip[i]);
        if(head==NULL) head = temp;
        else prev->next = temp;
        prev = temp;
    }
    return head;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

int get_len(list_node *head){
    int len = 0;
    for(;head;head=head->next, len++);
    return len;
}

int compare(list_node *l1, int len1, list_node *l2, int len2){
    if(len1>len2) return 1;
    else if(len2>len1) return 0;
    while(l1 && l2){
        if(l1->data>l2->data) return 1;
        else if(l2->data>l1->data) return 0;
        l1 = l1->next;
        l2 = l2->next;
    }
    return 0;
}

list_node* subtract(list_node *l1, int len1, list_node *l2, int len2, int *borrow){
    if(len1==0 && len2==0) return NULL;
    if(len1==0 || len2==0){
        printf("Fatal\n");
        return NULL;
    }
    int a = 0, b = 0, t_a = 0, sub = 0;
    list_node *cur_node = NULL;
    list_node *next_node = NULL;
    if(len1==len2){
        a = l1->data;
        b = l2->data;
        next_node = subtract(l1->next, len1-1, l2->next, len2-1, borrow);
    }else if(len1>len2){
        a = l1->data;
        next_node = subtract(l1->next, len1-1, l2, len2, borrow);
    }else{
        b = l2->data;
        next_node = subtract(l1, len1, l2->next, len2-1, borrow);
    }
    if(*borrow==1){
        t_a = (a!=0)?a-1:9;
    }else t_a = a;
    if(t_a<b){
        *borrow = 1;
        sub = ((*borrow)*10)+t_a - b;
    }else{
        if(a!=0) *borrow = 0;
        sub = t_a - b;
    }
    cur_node = make_list_node(sub);
    cur_node->next = next_node;
    return cur_node;
}

list_node* subtract_2_no(list_node *l1, list_node *l2){
    int borrow = 0;
    int len1 = get_len(l1);
    int len2 = get_len(l2);
    if(compare(l1, len1, l2, len2)==1) return subtract(l1, len1, l2, len2, &borrow);
    else return subtract(l2, len2, l1, len1, &borrow);
}

int main(){
    int ip1[] = {1,0,9,2,0};
    int l1 = sizeof(ip1)/sizeof(ip1[0]);
    int ip2[] = {2,0,0,2,0,0};
    int l2 = sizeof(ip2)/sizeof(ip2[0]);
    
    list_node *list1 = to_list(ip1, l1);
    list_node *list2 = to_list(ip2, l2);

    print_list(list1);
    print_list(list2);

    list_node *new_list = subtract_2_no(list1, list2);
    print_list(new_list);

    return 0;
}