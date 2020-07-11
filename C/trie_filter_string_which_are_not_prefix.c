// https://www.geeksforgeeks.org/strings-from-an-array-which-are-not-prefix-of-any-other-string/
/*
Given an array arr[] of strings, 
the task is to print the strings from the array 
which are not prefix of any other string from the same array.

Examples:
Input: arr[] = {“apple”, “app”, “there”, “the”, “like”}
Output: apple,like,there

Input: arr[] = {“a”, “aa”, “aaa”, “aaaa”}
Output: aaaa
*/

#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <malloc.h>

const int NODE_DATA_COUNT = 26;

void print_char_arr(char *ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%s - ",ip[i]);
    }
    printf("\n");
}

struct node;

typedef struct{
    char data;
    struct node *child;
}trie_data;

typedef struct node{
    trie_data **data;
    int data_count; // count of data cells in one group.
}trie_node;

typedef struct{
    trie_node *root;
}trie;

trie_data* init_trie_data(char data){
    trie_data *_trie_data = (trie_data*)malloc(sizeof(trie_data));
    if(_trie_data){
        _trie_data->data = data;
        _trie_data->child = NULL;
    }
    return _trie_data;
}

trie_node* init_trie_node(int data_count){
    trie_node *node = (trie_node*)malloc(sizeof(trie_node));
    if(node){
        node->data = (trie_data**)calloc(data_count,sizeof(trie_data*));
        node->data_count = data_count;
    }
    return node;
}

trie* init_trie(){
    trie *_trie = (trie*)malloc(sizeof(trie));
    if(_trie){
        _trie->root = NULL;
    }
    return _trie;
}

void print_trie_node(trie_node *node, char *op, int op_index){
    if(!node){
        if(op_index>0){
            op[op_index] = '\0';
            printf("%s - ",op);
        }
        return;
    }
    int i = 0;
    for(;i<node->data_count;i++){
        if(node->data[i]){
            op[op_index] = node->data[i]->data;
            print_trie_node(node->data[i]->child,op,op_index+1);
        }
    }
}

void print_trie(trie *_trie){
    char *op = (char*)calloc(100,sizeof(char));
    print_trie_node(_trie->root,op,0);
    printf("\n");
}

int to_index(char c){
    if(c>=65 && c<=90) return c-65;
    if(c>=97 && c<=122) return c-97;
    printf("[FATAL]: %c is not a valid char\n",c);
    return -1;
}

trie_node* insert_in_node(trie_node *node, char *ip, int ip_len, int ip_index){
    if(ip_len<=0 || ip_index==ip_len){
        return node;
    }
    if(node==NULL){
        node = init_trie_node(NODE_DATA_COUNT);
    }
    char c = ip[ip_index];
    int data_index = to_index(c);
    trie_data *data = node->data[data_index];
    if(data==NULL){
        data = init_trie_data(c);
        node->data[data_index] = data;
    }
    data->child = insert_in_node(data->child,ip,ip_len,ip_index+1);
    return node;
}

void insert_in_trie(trie *_trie, char *data){
    if(_trie==NULL){
        printf("No trie provided\n");
        return;
    }
    _trie->root = insert_in_node(_trie->root,data,strlen(data),0);
}

void filter_char(char *ip[], int length){
    trie *_trie = init_trie();
    int i = 0;
    for(;i<length;i++){
       insert_in_trie(_trie,ip[i]);
    }
    print_trie(_trie);
}

int main(){
    char *ip[] = {"a", "aa", "aaa", "aaaa", "aae"};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_char_arr(ip,length);
    filter_char(ip,length);

    return 0;
}