// https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
/*
Given a Linked List and a number n, write a function that returns 
the value at the n’th node from the end of the Linked List.
*/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *next;
}list_node;

list_node* make_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

list_node* make_list(list_node *head, int data){
    list_node *node = make_node(data);
    node->next = head;
    return node;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

list_node* get_kth_node(list_node *head, int k){
    list_node *prev = NULL;
    int i = 0;
    for(;i<k && head;head=head->next,i++){
        prev = head;
    }
    if(i!=k) return NULL;
    return prev;
}

list_node* get_kth_node_from_last(list_node *head, int k){
    list_node *kth_node_from_head = get_kth_node(head,k);
    if(kth_node_from_head==NULL){
        printf("Invalid K given.\n");
        return NULL;
    }
    list_node *tail =  head;
    while(kth_node_from_head->next){
        tail = tail->next;
        kth_node_from_head = kth_node_from_head->next;
    }
    return tail;
}

int main(){
    int ip[] = {1,2,3};
    int length = sizeof(ip)/sizeof(ip[0]);

    list_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);

    int k = 0;
    for(;k<=length+1;k++){
        printf("k=%d ",k);
        list_node *kth_last_node = get_kth_node_from_last(head,k);
        if(kth_last_node){
            printf("%d\n",kth_last_node->data);
        }
    }
    return 0;
}