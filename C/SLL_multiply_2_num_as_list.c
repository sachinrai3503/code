// https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists-third-list/
/*
Given two numbers represented by linked lists, write a function that returns the head
 of the new linked list that represents the number that is the product of those numbers.

Examples: 
Input : 9->4->6
        8->4
Output : 7->9->4->6->4

Input : 9->9->9->4->6->9
        9->9->8->4->9
Output : 9->9->7->9->5->9->8->0->1->8->1
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

void print_list(list_node *l1){
    for(;l1;l1=l1->next){
        printf("%d ",l1->data);
    }
    printf("\n");
}

list_node* to_list(int *ip, int length){
    list_node *head = NULL, *prev = NULL;
    int i = 0;
    for(;i<length;i++){
        list_node *t_node = make_list_node(ip[i]);
        if(head==NULL) head = t_node;
        else prev->next = t_node;
        prev = t_node;
    }
    return head;
}

list_node* reverse(list_node *head){
    list_node *p = head, *q = NULL, *r = NULL;
    while(p){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
    }
    return q;
}

list_node* multiple_list_by(list_node *l1, int data, list_node *from){
    list_node *head = NULL, *t_head = from;
    list_node *prev = NULL;
    int sum_carry = 0, prod_carry = 0;
    for(;l1;l1=l1->next){
        int prod = (l1->data * data) + prod_carry;
        if(t_head==NULL) t_head = make_list_node(0);
        if(head==NULL) head = t_head;
        else prev->next = t_head;
        int sum = t_head->data + (prod%10) + sum_carry;
        prod_carry = prod/10;
        sum_carry = sum/10;
        t_head->data = sum%10;
        prev = t_head;
        t_head = t_head->next;
    }
    if(sum_carry + prod_carry>0){
        prev->next = make_list_node(sum_carry+prod_carry);
    }
    return head;
}

list_node* multiply_2_list(list_node *l1, list_node *l2){
    if(!l1 || !l2) return NULL;
    list_node *r_l1 = reverse(l1);
    list_node *r_l2 = reverse(l2);
    list_node *head = NULL, *prev = NULL;
    list_node *t_head = NULL;
    for(;r_l2;r_l2=r_l2->next){
        list_node *t_result = multiple_list_by(r_l1, r_l2->data, t_head);
        if(head==NULL){
            head = t_head = t_result;
        }else{
            prev->next = t_result;
        }
        prev = t_result;
        t_head = t_head->next;
    }
    return reverse(head);
}

int main(){
    int n1[] = {9,9,9,9,9,9,9,1,0,9,0,0,0,9,9,1,1,0};
    int len1 = sizeof(n1)/sizeof(n1[0]);
    int n2[] = {9,0,0,0,0,0,9,9,9,9,9};
    int len2 = sizeof(n2)/sizeof(n2[0]);

    list_node *l1 = to_list(n1, len1);
    list_node *l2 = to_list(n2, len2);

    print_list(l1);
    print_list(l2);
    list_node *op = multiply_2_list(l1, l2);
    print_list(op);

    return 0;
}