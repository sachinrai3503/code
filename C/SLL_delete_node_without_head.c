#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *next;
}my_node;

my_node* make_node(int data){
    my_node *nw = (my_node*)malloc(sizeof(my_node));
    if(nw){
        nw->data = data;
        nw->next = NULL;
    }
    return nw;
}

my_node* make_list(my_node *head, int data){
    my_node *nw = make_node(data);
    nw->next = head;
    return nw;
}

void print_list(my_node *head){
    while(head){
        printf("%d ",head->data);
        head = head->next;
    }
    printf("\n");
}

my_node* get_node(my_node *head, int data){
    for(;head && head->data!=data;head=head->next);
    return head;
}

// https://www.geeksforgeeks.org/delete-a-node-from-linked-list-without-head-pointer/
void delete_given_node(my_node *node){
    if(node==NULL){
        printf("Null node given\n");
    }else if(node->next==NULL){
        printf("Deleting last node. Requires head\n");
    }else{
        my_node *next = node->next;
        node->data = next->data;
        node->next = next->next;
        next->next = NULL;
        free(next);
    }
}

//https://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/
/**
1) It must accept a pointer to the start node as the first parameter 
    and node to be deleted as the second parameter i.e., a pointer to head node is not global.
2) It should not return a pointer to the head node.
3) It should not accept pointer to pointer to the head node.

You may assume that the Linked List never becomes empty.
**/
void delete_given_node_with_constraints(my_node *head, my_node *node){
    if(head==NULL || node==NULL){
        printf("Null node given\n");
    }else if(head==node && head->next==NULL){
        printf("Deleting the only node in the list. Set the head to NULL manually.");
        free(node);
    }else if(node->next==NULL){
        my_node *temp = head;
        for(;temp->next!=node;temp=temp->next);
        temp->next = node->next;
        free(node);
    }else{
        delete_given_node(node);
    }
}

int main(){
    int ip[] = {1,2,3,4,5,6,7};
    int length = sizeof(ip)/sizeof(ip[0]);
    int del_data_1 = 1;
    int del_data_2 = 7;

    my_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);
    
    my_node *del_node_1 = get_node(head,del_data_1);
    my_node *del_node_2 = get_node(head,del_data_2);

    delete_given_node(del_node_1);
    print_list(head);
    printf("======================================\n");
    delete_given_node_with_constraints(head,del_node_2);
    print_list(head);

    return 0;
}