// https://www.geeksforgeeks.org/find-all-shortest-unique-prefixes-to-represent-each-word-in-a-given-list/
// https://www.interviewbit.com/problems/shortest-unique-prefix/
/*
Given an array of words, find all shortest unique 
prefixes to represent each word in the given array. 
Assume that no word is prefix of another.

Examples:
Input: arr[] = {"zebra", "dog", "duck", "dove"}
Output: dog, dov, du, z

Input: arr[] =  {"geeksgeeks", "geeksquiz", "geeksforgeeks"};
Output: geeksf, geeksg, geeksq}
*/

// Sorting based solution in java :: String_shortest_key_for_each_str.java

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <string.h>

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
    char c;
    int frequency;
    struct node *child;
}trie_data;

typedef struct node{
    trie_data **data;
    int data_count; // count of data cells in one group.
}trie_node;

typedef struct{
    trie_node *root;
}trie;

trie_data* init_data(char c){
    trie_data *data = (trie_data*)malloc(sizeof(trie_data));
    if(data){
        data->c = c;
        data->frequency = 1;
        data->child = NULL;
    }
    return data;
}

trie_node* init_node(int data_count){
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

int to_index(char c){
    if(c>=65 && c<=90) return c-65;
    if(c>=97 && c<=122) return c-97;
    printf("[ERROR] : Non char given\n");
    return -1;
}

void print_trie_node(trie_node *node, char *op, int index){
    if(node==NULL){
        return;
    }
    int i = 0;
    for(;i<node->data_count;i++){
        if(node->data[i]){
            op[index] = node->data[i]->c;
            if(node->data[i]->frequency == 1){
                op[index+1] = '\0';
                printf("%s - ",op);
            }else{
                print_trie_node(node->data[i]->child,op,index+1);
            }
        }
    }
}

void print_trie(trie *_trie){
    char *op = (char*)calloc(100,sizeof(char));
    print_trie_node(_trie->root,op,0);
}

trie_node* insert_in_node(trie_node *node, char *ip_str, int ip_len, int ip_index){
    if(ip_len<=0 || ip_index==ip_len){
        return node;
    }
    if(node==NULL){
        node = init_node(NODE_DATA_COUNT);
    }
    int char_index = to_index(ip_str[ip_index]);
    trie_data *data = node->data[char_index];
    if(!data){
        data = init_data(ip_str[ip_index]);
        node->data[char_index] = data;
    }else{
        data->frequency++;
    }
    data->child = insert_in_node(data->child,ip_str,ip_len,ip_index+1);
    return node;
}

void insert_in_trie(trie *_trie, char *ip){
    if(_trie==NULL){
        printf("Empty trie given\n");
        return;
    }
    _trie->root = insert_in_node(_trie->root,ip,strlen(ip),0);
}

int main(){
    char *ip[] = {"geeksgeeks", "geeksquiz", "geeksforgeeks"};
    int length = sizeof(ip)/sizeof(ip[0]);

    trie *_trie = init_trie();
    print_char_arr(ip,length);
    int i = 0;
    for(;i<length;i++){
        insert_in_trie(_trie,ip[i]);
    }
    print_trie(_trie);

    return 0;
}