// https://www.geeksforgeeks.org/delete-middle-element-stack/
/*
Given a stack with push(), pop(), empty() operations, delete middle of it
 without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]
Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]
Output : Stack[] = [1, 2, 4, 5, 6]
*/

#include <stdio.h>
#include <malloc.h>


void print_int_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct{
    int *data;
    int top;
    int max_size;
}stack;

stack* init_stack(int *ip, int length){
    stack *stck = (stack*)malloc(sizeof(stack));
    if(stck){
        stck->data = ip;
        stck->top = length-1;
        stck->max_size = length;
    }
    return stck;
}

int is_full(stack *stck){
    if(stck->top==stck->max_size-1){
        return 1;
    }
    return 0;
}

int is_empty(stack *stck){
    if(stck->top==-1) return 1;
    return 0;
}

void push(stack *stck, int data){
    if(is_full(stck)){
        printf("Full\n");
    }else{
        stck->data[++stck->top] = data;
    }
}

int pop(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return '\0';
    }
    return stck->data[stck->top--];
}

void delete_middle_element(stack *stck, int mid_index){
    if(stck->top==-1) return;
    if(mid_index==stck->top){
        pop(stck);
        return;
    }
    int temp = pop(stck);
    delete_middle_element(stck, mid_index);
    push(stck, temp);
}

int main(){
    int ip[] = {1,2,3,4,5,6,7,8,9,10};
    int length = sizeof(ip)/sizeof(ip[0]);
    stack *stck = init_stack(ip, length);
    print_int_arr(stck->data,stck->top+1);
    delete_middle_element(stck, stck->top/2);
    print_int_arr(stck->data,stck->top+1);
    return 0;
}