/*
Given an input string and q number of operations that need to be performed on it.
There are three types of operations.
1 – reverse the string
2 1 a – insert the input character (here ‘a’) in the front of the current string
2 2 a – insert the input character (here ‘a’) in the back of the current string

Example:
abc -> input string( lets say ‘s’)
5 -> number of operations    

1     ->    s = abc ( front_vector {}, flag= true)  
2 2 a     ->    s = abc ( front_vector {a}, flag= true)
2 1 b     ->    s = abcb ( front_vector {a}, flag= true)
1     ->    s = abcb ( front_vector {a}, flag= false)
2 1 x     ->    s = abcb ( front_vector {x,a}, flag= false)

Front insertion string: xa
Output (Final string): xaabcb
*/

// Note - Below implementation doesn't uses list.

#include <stdio.h>
#include <malloc.h>
#include <string.h>

void print_char_arr(char *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%c",ip[i]);
    }
    printf("\n");
}

void print_int_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void reverse(char *ip, int s, int e){
    for(;s<e;s++,e--){
        char t = ip[s];
        ip[s] = ip[e];
        ip[e] = t;
    }
}

typedef struct{
    char *data;
    int top;
    int max_size;
}stack;

stack* init_stack(int max_size){
    stack *stck = (stack*)malloc(sizeof(stack));
    if(stck){
        stck->data = (char*)calloc(max_size, sizeof(char));
        stck->top = -1;
        stck->max_size = max_size;
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

void push(stack *stck, char c){
    if(is_full(stck)){
        printf("Full\n");
    }else{
        stck->data[++stck->top] = c;
    }
}

char pop(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return '\0';
    }
    return stck->data[stck->top--];
}

char* get_final_string(char *ip, int len, int *oper, int oper_len){
    stack *stck = init_stack(len);
    char *t_op = (char*)calloc(len, sizeof(char));
    int k  = 0;
    int reverse_flag = 0;
    int j = 0;
    int i = 0;
    for(;i<oper_len && j<len;i++){
        if(j!=0 && oper[i]==2){
            reverse_flag = !(reverse_flag);
        }else if(oper[i]==0){
            if(reverse_flag==0){
                push(stck, ip[j++]);
            }else{
                t_op[k++] = ip[j++];
            }
        }else if(oper[i]==1){
            if(reverse_flag==1){
                push(stck, ip[j++]);
            }else{
                t_op[k++] = ip[j++];
            }
        }
    }
    // print_char_arr(t_op,k);
    char *op = (char*)calloc(len+1, sizeof(char));
    int p = 0;
    while(!is_empty(stck)){
        op[p++] = pop(stck);
    }
    i = 0;
    while(i<k){
        op[p++] = t_op[i++];
    }
    op[p] = '\0';
    if(reverse_flag) reverse(op,0,p-1);
    return op;
}

int main(){
    char *ip = "abcxyfzmklqpmno";
    int len = strlen(ip);
    // Reverse = 2, add front = 0, add rear = 1
    int oper[] = {1,1,1,1,0,2,1,1,2,0,1,1,2,0,0,0,1,1};
    int oper_len = sizeof(oper)/sizeof(oper[0]);
    printf("Ip=>%s\n",ip);
    printf("oper=>");
    print_int_arr(oper,oper_len);
    char *op = get_final_string(ip, len, oper, oper_len);
    printf("Op=>%s\n",op);
    return 0;
}