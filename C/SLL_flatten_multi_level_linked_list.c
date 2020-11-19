// https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
/*
Given a linked list where in addition to the next pointer, each node has a child
 pointer, which may or may not point to a separate list. These child lists may 
 have one or more children of their own, and so on, to produce a multilevel data
  structure, as shown in below figure.You are given the head of the first level 
  of the list. Flatten the list so that all the nodes appear in a single-level 
  linked list. You need to flatten the list in way that all nodes at first level 
  should come first, then nodes of second level, and so on.

Each node is a C struct with the following definition.
struct List 
{ 
    int data; 
    struct List *next; 
    struct List *child; 
}; 

10->5->12->7->11
 |         |
 V         V
 4->20->13 17->6
     |   |  |
     V   V  V
     2   16 9->8 
         |  |
         V  V
         3  19->15

OP >> 10->5->12->7->11->4->20->13->17->6->2->16->9->8->3->19->15
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct SLL_Node{
    int data;
    struct SLL_Node *next, *child;
}list_node;

list_node* make_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = node->child = NULL;
    }
    return node;
}

list_node* connect_next_node(int *ip, int length){
    list_node *head = NULL;
    list_node *prev = NULL;
    int i = 0;
    for(;i<length && ip[i]!=-1;i++){
        list_node *node = make_list_node(ip[i]);
        if(!head) head = node;
        else prev->next = node;
        prev = node;
    }
    return head;
}

void print_multi_level_list(list_node *head){
    for(;head;head=head->next){
        printf("%d -> ",head->data);
        print_multi_level_list(head->child);
        printf("\n");
    }
}

void print_list(list_node *head){
    for(;head;head=head->next)
        printf("%d ",head->data);
    printf("\n");
}

list_node* get_last_node(list_node *head){
    for(;head && head->next;head=head->next);
    return head;
}

list_node* get_next_node_with_child(list_node *head){
    for(;head && head->child==NULL;head=head->next);
    return head;
}

list_node* flatten_multilevel_list(list_node *head){
    list_node *p = head, *q = head;
    while(p){
        p = get_last_node(p);
        q = get_next_node_with_child(q);
        if(q){
            p->next = q->child;
            q->child = NULL;
        }
        p = p->next;
    }
    return head;
}

int main(){

    int ip[50][50] = {{10, 5, 12, 7, 11,-1},
                        {4, 20, 13,-1},
                        {17, 6,-1},
                        {2,-1},
                        {16,-1},
                        {9, 8,-1},
                        {3,-1},
                        {19, 15,-1}
                       }; 
  
    int row = 8;
    int col = 10;
    list_node **arr = (list_node**)calloc(row, sizeof(list_node*));
    int i = 0;
    for(;i<row;i++)
        arr[i] = connect_next_node(ip[i],col);

    /* modify child pointers to create the list shown above */
    arr[0]->child = arr[1]; 
    arr[0]->next->next->next->child = arr[2]; 
    arr[1]->next->child = arr[3];
    arr[1]->next->next->child = arr[4];
    arr[2]->child = arr[5]; 
    arr[4]->child = arr[6]; 
    arr[5]->child = arr[7];

    list_node *head = arr[0];
    print_multi_level_list(head);
    printf("*****************************************************\n");

    head = flatten_multilevel_list(head);
    print_list(head);

    return 0;
}