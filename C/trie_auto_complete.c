// https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
/*
We are given a Trie with a set of strings stored in it.
Now the user types in a prefix of his search query, we need to give him all
recommendations to auto-complete his query based on the strings stored in
the Trie.

We assume that the Trie stores past searches by the users.

For example if the Trie store {“abc”, “abcd”, “aa”, “abbbaba”} 
and the User types in “ab” then he must be shown {“abc”, “abcd”, “abbbaba”}.
*/


#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <string.h>

void print_arr(char *ip[], int length){
    int i=0 ;
    for(;i<length;i++){
        printf("%s ",ip[i]);
    }
    printf("\n");
}

typedef struct trie_level_node trie_node;

typedef struct{
    int is_last;
    trie_node *next;
}trie_data;

typedef struct trie_level_node{
    trie_data **data;
}trie_node;

typedef struct{
    trie_node *root;
}trie;

trie_data* make_trie_data(){
    trie_data *data = (trie_data*)malloc(sizeof(trie_data));
    if(data){
        data->is_last = 0;
        data->next = NULL;
    }
    return data;
}

trie_node* make_trie_node(){
    trie_node *node = (trie_node*)malloc(sizeof(trie_node));
    if(node){
        node->data = (trie_data**)calloc(26,sizeof(trie_data*));
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
    if(c>=65 && c<=90) return c-'A';
    if(c>=97 && c<=122) return c-'a';
    return INT_MAX;
}

trie_node* insert_data(trie_node *node, char *word, int index, int length){
    if(index==length) return node;
    if(node==NULL) node = make_trie_node();
    int char_index = to_index(word[index]);
    if(node->data[char_index]==NULL) node->data[char_index] = make_trie_data();
    trie_data *data = node->data[char_index];
    if(index==length-1){
        data->is_last = 1;
    }else{
        data->next = insert_data(data->next,word,index+1,length);
    }
    return node;
}

void insert_word(trie *dict, char *word){
    int word_len = strlen(word);
    dict->root = insert_data(dict->root,word,0,word_len);
}

void print_node(trie_node *node, char *op, int index){
    if(!node) return;
    int i = 0;
    for(;i<26;i++){
        if(node->data[i]){
            op[index] = i+97;
            if(node->data[i]->is_last){
                op[index+1] = '\0';
                printf("%s ",op);
            }
            print_node(node->data[i]->next,op,index+1);
        }
    }
}

void search_recommeded(trie *dict, char *word){
    if(dict==NULL){
        printf("No dict maintained\n");
        return;
    }
    trie_node *node = dict->root;
    int index = 0;
    int length = strlen(word);
    char *op = (char*)calloc(100,sizeof(char));
    while(node){
        int char_index = to_index(word[index]);
        if(node->data[char_index]==NULL) break;
        op[index] = word[index];
        if(index==length-1){
            if(node->data[char_index]->is_last) {
                op[index+1] = '\0';
                printf("%s ",op);
            }
            print_node(node->data[char_index]->next,op,index+1);
            break;
        }
        index++;
        node = node->data[char_index]->next;
    }
}

void print_trie(trie *dict){
    char *op = (char*)calloc(100,sizeof(char));
    print_node(dict->root,op,0);
}

int main(){
    char *word[] = {"a","ant","andy","and","language","map","mapping",
            "abc", "abcd", "aa", "abbbaba"};
    int length = sizeof(word)/sizeof(word[0]);
    char *temp_word[] = {"boy","there","andyi","an","mapp","map","ma","ab"};
    int temp_length = sizeof(temp_word)/sizeof(temp_word[0]);

    printf("words are =>");
    print_arr(word, length);

    trie *dict = init_trie();
    int i = 0;
    for(;i<length;i++){
        insert_word(dict,word[i]);
    }
    printf("Trie data below\n");;
    print_trie(dict);
    printf("\n====================================\n");

    for(i=0;i<temp_length;i++){
        printf("%s ->",temp_word[i]);
        search_recommeded(dict,temp_word[i]);
        printf("\n");
    }

    return 0;
}