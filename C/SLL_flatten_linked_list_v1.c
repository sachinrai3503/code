// https://www.geeksforgeeks.org/flattening-a-linked-list/
/*
Given a LL where every node represents a LL and contains 2 pointers of its type:
(i) Pointer to next node in the main list (we call it ‘right’ pointer)
(ii) Pointer to a LL where this node is head (we call it ‘down’ pointer).
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
Write a function flatten() to flatten the lists into a single linked list. 
The flattened linked list should also be sorted. 

For example, for the above input list, output list should be 
5->7->8->10->19->20->22->28->30->35->40->45->50.
*/

// Heap based approach - SLL_flatten_linked_list_v2.c

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

list_node* connect_child_node(int *ip, int length){
    list_node *head = NULL;
    list_node *prev = NULL;
    int i = 0;
    for(;i<length && ip[i]!=-1;i++){
        list_node *node = make_list_node(ip[i]);
        if(!head) head = node;
        else prev->child = node;
        prev = node;
    }
    return head;
}

list_node* connect_next_node(list_node **ip, int length){
    list_node *head = NULL;
    list_node *prev = NULL;
    int i = 0;
    for(;i<length;i++){
        if(ip[i]==NULL) continue;
        if(!head) head = ip[i];
        else prev->next = ip[i];
        prev = ip[i];
    }
    return head;
}

void print_child(list_node *head){
    for(;head;head=head->child)
        printf("%d ",head->data);
    printf("\n");
}

void print_list(list_node *head){
    for(;head;head=head->next)
        print_child(head);
}

void print_list2(list_node *head){
    for(;head;head=head->next){
        printf("%d ==>",head->data);
        if(head->child) print_child(head);
        else printf("NULL\n");
    }
}

list_node* get_last_smaller_node(list_node *head, int k){
    list_node *prev = NULL;
    for(;head && head->data<=k;head=head->child){
        prev = head;
    }
    return prev;
}

list_node* merge_2_list(list_node *head1, list_node *head2){
    if(!head1) return head2;
    if(!head2) return head1;
    list_node *new_head = NULL;
    list_node *prev = NULL;
    while(head1 && head2){
        list_node *last_smaller_node = get_last_smaller_node(head2, head1->data);
        if(!new_head){
            if(!last_smaller_node) new_head = head1;
            else new_head = head2;
        }else{
            if(!last_smaller_node) prev->child = head1;
            else prev->child = head2;
        }
        if(last_smaller_node){
            head2 = last_smaller_node->child;
            last_smaller_node->child = head1;
        }
        prev = head1;
        head1 = head1->child;
    }
    if(head1==NULL){
        prev->child = head2;
    }
    return new_head;
}

list_node* flatten_lists(list_node *head){
    list_node *prev = NULL, *next = NULL;
    while(head){
        next = head->next;
        head->next = NULL;
        prev = merge_2_list(prev,head);
        head = next;
    }
    return prev;
}

int main(){

    // Child are represented in cols where -1 means end of list.
    // New row is next list.
    int ip[50][50] = {  {1,4,6,8,-1},
                        {2,3,7,-1},
                        {5,9,-1},
                        {10,11,12,-1}
                    };
    int row = 4;
    int col = 10;

    list_node **heads = (list_node**)calloc(row,sizeof(list_node*));
    int i = 0;
    for(;i<row;i++){
        heads[i] = connect_child_node(ip[i],col);
    }
    list_node *head = connect_next_node(heads, row);
    print_list(head);
    printf("============================\n");
    
    // NOTE : In the flattened list nodes are connected via child pointer.
    list_node *flatten_head = flatten_lists(head);
    print_list2(flatten_head);

    return 0;
}