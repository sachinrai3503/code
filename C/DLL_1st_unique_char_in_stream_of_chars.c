// https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/
/*
Given a stream of characters, find the first non-repeating character from stream.
You need to tell the first non-repeating character in O(1) time at any moment.
*/

// For Queue based approach see - Queue1stUniqueCharInStreamOfChars.java

#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef struct node{
    char data;
    struct node *next, *prev;
}dll_node;

typedef struct{
    dll_node *first, *last;
}DLL;

dll_node* init_dll_node(char data){
    dll_node *node = (dll_node*)malloc(sizeof(dll_node));
    if(node){
        node->data = data;
        node->next = node->prev = NULL;
    }
    return node;
}

DLL* init_DLL(){
    DLL *dll = (DLL*)malloc(sizeof(DLL));
    if(dll){
        dll->first = dll->last = NULL;
    }
    return dll;
}

dll_node* insert_at_last(DLL *dll, char data){
    dll_node *new_node = init_dll_node(data);
    if(dll->last==NULL){
        dll->last = dll->first = new_node;
    }else{
        new_node->prev = dll->last;
        dll->last->next = new_node;
        dll->last = new_node;
    }
    return new_node;
}

dll_node* delete_node(DLL *dll, dll_node *node){
    if(dll->last==NULL){
        printf("Empty\n");
        return NULL;
    }else{
        dll_node *prev = node->prev;
        dll_node *next = node->next;
        if(prev==NULL){
            dll->first = dll->first->next;
        }else{
            prev->next = next;
        }
        if(next==NULL){
            dll->last = dll->last->prev;
        }else{
            next->prev = prev;
        }
    }
    node->next = node->prev = NULL;
    return node;
}

void print_1st_unique_char(char *s, int length){
    DLL *dll = init_DLL();
    dll_node *null_node = init_dll_node('\0');
    dll_node **dll_map = (dll_node**)calloc(26, sizeof(dll_node*));
    int i = 0;
    for(;i<length;i++){
        int t_index = s[i]-97;
        if(dll_map[t_index]==NULL){
            dll_map[t_index] = insert_at_last(dll, s[i]);
        }else if(dll_map[t_index]!=null_node){
            delete_node(dll, dll_map[t_index]);
            dll_map[t_index] = null_node;
        }
        printf("Unique char till now = %c\n", dll->first->data);
    }
}

int main(){
    char ip[] = "geekforgeekandgeeksandquizfor";
    int length = strlen(ip);

    printf("ip=%s\n",ip);
    print_1st_unique_char(ip, length);
    return 0;
}