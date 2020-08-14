//  https://www.geeksforgeeks.org/implement-a-dictionary-using-trie/
/*
Implement a dictionary using Trie such that if the input is a string 
representing a word, the program prints its meaning from the prebuilt 
dictionary.

Input: str = “map”
Output: a diagrammatic representation of an area
Input: str = “language”
Output: the method of human communication
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
    char *meaning;
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
        data->meaning = NULL;
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

trie_node* insert_data(trie_node *node, char *word, int index, int length, 
    char *meaning){
    if(index==length) return node;
    if(node==NULL) node = make_trie_node();
    int char_index = to_index(word[index]);
    if(node->data[char_index]==NULL) node->data[char_index] = make_trie_data();
    if(index==length-1){
        node->data[char_index]->meaning = meaning;
    }else{
        node->data[char_index]->next = insert_data(node->data[char_index]->next,
            word,index+1,length,meaning);
    }
    return node;
}

void insert_word(trie *dict, char *word, char *meaning){
    int word_len = strlen(word);
    dict->root = insert_data(dict->root,word,0,word_len,meaning);
}

char* search_word(trie *dict, char *word){
    if(dict==NULL){
        printf("No dict maintained\n");
        return NULL;
    }
    trie_node *node = dict->root;
    int index = 0;
    int length = strlen(word);
    while(node){
        int char_index = to_index(word[index]);
        if(node->data[char_index]==NULL) break;
        if(index==length-1){
            char *meaning = node->data[char_index]->meaning;
            if(meaning) return meaning;
            else return "No meaning present of word";
        }
        index++;
        node = node->data[char_index]->next;
    }
    return NULL;
}

void print_node(trie_node *node, char *op, int index){
    if(!node) return;
    int i = 0;
    for(;i<26;i++){
        if(node->data[i]){
            op[index] = i+97;
            if(node->data[i]->meaning){
                op[index+1] = '\0';
                printf("%s means %s\n",op, node->data[i]->meaning);
            }
            print_node(node->data[i]->next,op,index+1);
        }
    }
}

void print_trie(trie *dict){
    char *op = (char*)calloc(100,sizeof(char));
    print_node(dict->root,op,0);
}

int main(){
    char *word[] = {"a","ant","andy","and","language","map","mapping"};
    char *meaning[] = {"vowel","chitti","boy","conjuction","communication",
        "ways", "process"};
    int length = sizeof(word)/sizeof(word[0]);
    char *temp_word[] = {"boy","there","andyi","an"};
    int temp_length = sizeof(temp_word)/sizeof(temp_word[0]);

    printf("words are =>");
    print_arr(word, length);
    printf("meaning are =>");
    print_arr(meaning, length);

    trie *dict = init_trie();
    int i = 0;
    for(;i<length;i++){
        insert_word(dict,word[i],meaning[i]);
    }
    printf("Trie data below\n");;
    print_trie(dict);
    printf("====================================\n");

    for(i=0;i<length;i++){
        printf("%s means %s\n",word[i],search_word(dict,word[i]));
    }

    for(i=0;i<temp_length;i++){
        printf("%s means %s\n",temp_word[i],search_word(dict,temp_word[i]));
    }

    return 0;
}