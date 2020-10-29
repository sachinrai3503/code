// https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/?ref=lbp
/*
Given a pointer to a node to be deleted, delete the node. Note that we don’t 
have pointer to head node.
*/

// Tried to handle the deletion of last node.

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct SLL{
    int data;
    struct SLL *next;
}list_node;

list_node* init_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

typedef struct{
    list_node *head;
    list_node *last_node; // Only set when the last node is deleted
}list;

list* init_list(){
    list *_list = (list*)malloc(sizeof(list));
    if(_list){
        _list->head = _list->last_node = NULL;
    }
    return _list;
}

int is_empty(list *_list){
    if(_list->head==_list->last_node) return 1;
    return 0;
}

list_node* get_node(list *_list, int data){
    if(is_empty(_list)){
        printf("Empty\n");
        return NULL;
    }
    list_node *head = _list->head;
    for(;head!=_list->last_node;head=head->next){
        if(head->data==data) return head;
    }
    return NULL;
}

void print_list(list *_list){
    list_node *head = _list->head;
    for(;head!=_list->last_node;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

list* to_list(int ip[], int length){
    list *_list = init_list();
    list_node *prev = NULL;
    int i = 0;
    for(;i<length;i++){
        list_node *node = init_node(ip[i]);
        if(!prev) _list->head = node;
        else prev->next = node;
        prev = node;
    }
    return _list;
}

list_node* delete(list *_list, list_node *node){
    if(is_empty(_list)){
        printf("Ëmpty\n");
        return NULL;
    }
   if(node->next==_list->last_node){
       _list->last_node = node;
       _list->last_node->next = NULL;
       return node;
   }
   int temp = node->data;
   list_node *next = node->next;
   node->data = next->data;
   node->next = next->next;
   next->next = NULL;
   next->data = temp;
   return next;
}

int main(){
    int ip[] = {1,2,3,4,5,6,7,8,9,10};
    int length = sizeof(ip)/sizeof(ip[0]);

    list *_list = to_list(ip,length);
    print_list(_list);

    int x[] = {1,5,9,10,8,3,2,6,7,4};
    int xlen = sizeof(x)/sizeof(x[0]);
    int i = 0;
    for(;i<xlen;i++){
        list_node *node = delete(_list, get_node(_list,x[i]));
        printf("Deleted = %d :: List>>",node->data);
        print_list(_list);
    }

}