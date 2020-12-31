// https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/
/*
How to implement a stack which will support following operations in O(1) time 
 complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.

The important question is, whether to use a linked list or array for
 implementation of stack?
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *next, *prev;
}stack_node;

typedef struct {
    stack_node *top;
    stack_node *middle;
    int count;
    int max_size;
}stack;

stack_node* init_node(int data){
    stack_node *node = (stack_node*)malloc(sizeof(stack_node));
    if(node){
        node->data = data;
        node->prev = node->next = NULL;
    }
    return node;
}

stack* init_stack(int max_size){
    stack *_stck = (stack*)malloc(sizeof(stack));
    if(_stck){
        _stck->top = NULL;
        _stck->middle = NULL;
        _stck->count = 0;
        _stck->max_size = max_size;
    }
    return _stck;
}

int is_full(stack *stck){
    if(stck->count==stck->max_size) return 1;
    return 0;
}

int is_empty(stack *stck){
    if(stck->top==NULL) return 1;
    return 0;
}

stack_node* get_middle(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return NULL;
    }
    return stck->middle;
}

void print_stack(stack *stck){
    if(is_empty(stck)){
        printf("Stack Empty\n");
        return;
    }
    stack_node *temp = stck->top;
    while(temp){
        printf("%d ",temp->data);
        temp = temp->prev;
    }
    printf("\n");
}

void push(stack *stck, int data){
    if(is_full(stck)){
        printf("Full\n");
    }else{
        stack_node *node = init_node(data);
        if(stck->top){
            stck->top->next = node;
            node->prev = stck->top;
        }
        stck->top = node;
        stck->count++;
        if(stck->count%2){
            if(stck->count==1) stck->middle = stck->top;
            else stck->middle = stck->middle->next;
        }
    }
}

stack_node* pop(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return NULL;
    }else{
        stack_node *temp = stck->top;
        stck->top = stck->top->prev;
        if(stck->top) stck->top->next = NULL;
        if(stck->count%2) stck->middle = stck->middle->prev;
        stck->count--;
        temp->prev = temp->next = NULL;
        return temp;
    }
}

stack_node* delete_middle(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return NULL;
    }else{
        stack_node *temp = stck->middle;
        if(stck->middle==stck->top){
            stck->middle = stck->top = NULL;
        }else{
            stack_node *left = temp->prev;
            stack_node *right = temp->next;
            if(left) left->next = right;
            if(right) right->prev = left;
            if(stck->count%2) stck->middle = left;
            else stck->middle = right;
        }
        stck->count--;
        return temp;
    }
}

int main(){
    int ip[] = {1,2,3,4,5,6,7,8,9,10};
    int ip_len = sizeof(ip)/sizeof(ip[0]);
    // 1 - push && 0 - pop && anything else delete middle
    int ops[] = {1,0,1,2,1,1,2,1,0,1,1,1,2,2};
    int ops_len = sizeof(ops)/sizeof(ops[0]);

    stack *stck = init_stack(ip_len);
    int i = 0;
    int j = 0;
    for(;i<ops_len && j<ip_len;i++){
        if(ops[i]==1) push(stck, ip[j++]);
        else if(ops[i]==0) {
            stack_node *temp = pop(stck);
            printf("poped = %d\n",temp->data);
        }else{
            stack_node *temp = delete_middle(stck);
            printf("Deleted middle = %d\n",temp->data);
        }
        printf("Stack(printed from top)->>");
        print_stack(stck);
    }
    return 0;
}