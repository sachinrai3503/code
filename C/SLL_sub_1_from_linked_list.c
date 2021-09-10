// https://www.geeksforgeeks.org/subtract-1-from-a-number-represented-as-linked-list/
/*
Given the head of the linked list representing a positive integer,
 the task is to print the updated linked list after subtracting 1 from it.

Examples:
Input: LL = 1 -> 2 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 3

Input: LL = 1 -> 2
Output: 1 -> 1
*/

#include <stdio.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *next;
}list;

list* init_list_node(int data){
    list *node = (list*)malloc(sizeof(int));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

list* to_list(int *ip, int length){
    list *head = NULL;
    list *prev = NULL;
    int i = 0;
    for(;i<length;i++){
        list *temp = init_list_node(ip[i]);
        if(head==NULL) head = temp;
        else prev->next = temp;
        prev = temp;
    }
    return head;
}

void print_list(list *head){
    for(;head;head=head->next){
        printf("%d ", head->data);
    }
    printf("\n");
}

void add_1_till(list *from, list *till){
    for(;from && from!=till;from=from->next){
        if(from->data==9){
            from->data = 0;
        }else from->data = from->data + 1;
    }
}

void minus_1(list *node){
    if(node){
        if(node->data==0) node->data = 9;
        else node->data = node->data-1;
    }
}

list* subtract_1(list *head){
    list *p = head;
    list *start = NULL;
    while(p){
        if(p->next==NULL){
            minus_1(p);
        }else if(p->next->data==0){
            if(start==NULL) start = p;
            minus_1(p);
        }else if(p->next->data>0){
            add_1_till(start, p);
            start = NULL;
        }
        p = p->next;
    }
    return head;
}

int main(){

    int ip[] = {9,9,9,9};
    int length = sizeof(ip)/sizeof(ip[0]);

    list *head = to_list(ip, length);
    print_list(head);

    subtract_1(head);
    print_list(head);

    return 0;
}