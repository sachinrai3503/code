// https://www.geeksforgeeks.org/find-the-string-formed-by-joining-k-consecutive-nodes-of-linked-list/
/*
Given an integer K and a linked list in which each node stores a character. 
The task is to join K consecutive nodes of the linked list to form a word. 
Finally, print the string obtained by joining these words (space separated).

Input: List = ‘a’ -> ‘b’ -> ‘c’ ->’d’ -> ‘e’ -> NULL, k = 3
Output: abc de

Input: List = ‘a’ -> ‘b’ -> ‘c’ -> ‘d’ -> ‘e’ -> ‘f’ -> NULL, k = 2
Output: ab cd ef
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <string.h>

typedef struct node{
    char data;
    struct node *next;
}SLL;

SLL* make_SLL_node(char data){
    SLL* node = (SLL*)malloc(sizeof(SLL));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

SLL* make_SLL(SLL *head, char data){
    SLL *node = make_SLL_node(data);
    node->next = head;
    return node;
}

void print_SLL(SLL *head){
    for(;head;head=head->next)
        printf("%d ",head->data);
    printf("\n");
}

typedef struct char_list{
    char *data;
    int size;
    struct char_list *next;
}list_node;

list_node* make_list_node(int size){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = (char*)calloc(size+1,sizeof(char));
        node->size = size;
        node->next = NULL;
    }
    return node;
}

void print_list(list_node *head){
    for(;head;head=head->next)
        printf("%s ",head->data);
    printf("\n");
}

list_node* join_k_consquetive_node(SLL *head, int k){
    if(k<=0){
        printf("Invalid K passed\n");
        return NULL;
    }
    list_node *new_head = make_list_node(k);
    list_node *cur_node = new_head;
    list_node *prev = NULL;
    int index = 0;
    int i = 0;
    for(;head;head=head->next,i++){
        cur_node->data[index++] = head->data;
        if((i%k)==(k-1)){
            cur_node->data[index] = '\0';
            list_node *next = make_list_node(k);
            cur_node->next = next;
            prev = cur_node;
            cur_node = cur_node->next;
            index = 0;
        }
    }
    if(index!=0){
        cur_node->data[index] = '\0';
    }
    return new_head;
}

int main(){
    char *ip = "abcdefghi";
    int length = strlen(ip);

    SLL *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_SLL(head,ip[i]);
    }
    print_SLL(head);

    int k = 0;
    for(;k<=length+1;k++){
        printf("K=%d>>",k);
        list_node *list =join_k_consquetive_node(head,k);
        print_list(list);
    }

    return 0;
}