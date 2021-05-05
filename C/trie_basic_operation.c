// https://leetcode.com/problems/implement-trie-prefix-tree/
// https://www.geeksforgeeks.org/trie-insert-and-search/
// https://www.geeksforgeeks.org/trie-delete/
// https://www.geeksforgeeks.org/trie-display-content/
#include <string.h>
#define true 1
#define false 0

typedef int bool;
typedef struct trienode trie_node;

typedef struct{
    char c;
    int eow;
    trie_node *next;
}trie_data;

typedef struct trienode{
    trie_data **data;
    int sibbling_count;
}trie_node;


typedef struct {
    trie_node *root;
} Trie;

trie_data* init_trie_data(char c, int eow){
    trie_data *data = (trie_data*)malloc(sizeof(trie_data));
    if(data){
        data->c = c;
        data->eow = eow;
        data->next = NULL;
    }
    return data;
}

trie_node* init_trie_node(int size){
    trie_node* node = (trie_node*)malloc(sizeof(trie_node));
    if(node){
        node->data = (trie_data**)calloc(size, sizeof(trie_data*));
        node->sibbling_count = 0;
    }
    return node;
}

/** Initialize your data structure here. */

Trie* trieCreate() {
    Trie *trie = (Trie*)malloc(sizeof(Trie));
    if(trie){
        trie->root = NULL;
    }
    return trie;
}

int to_index(char c){
    return c-97;
}

trie_node* insert_in_trie(trie_node *root, char *word, int i, int length){
    if(*word=='\0' || i==length) return root;
    char c = word[i];
    int index = to_index(c);
    if(root==NULL) root = init_trie_node(26);
    if(root->data[index]==NULL) {
        root->data[index] = init_trie_data(c, i==length-1);
        root->sibbling_count++;
    }
    else if(i==length-1) root->data[index]->eow = 1;
    root->data[index]->next = insert_in_trie(root->data[index]->next, word, i+1, length);
    return root;
}

/** Inserts a word into the trie. */
void trieInsert(Trie* obj, char * word) {
    obj->root = insert_in_trie(obj->root, word, 0, strlen(word));  
}

bool search_in_trie(trie_node *root, char *word, int i, int length){
    if(root==NULL) return false;
    int index = to_index(word[i]);
    if(root->data[index]==NULL) return false;
    if(i==length-1) return root->data[index]->eow; 
    return search_in_trie(root->data[index]->next, word, i+1, length);
}


/** Returns if the word is in the trie. */
bool trieSearch(Trie* obj, char * word) {
    return search_in_trie(obj->root, word, 0, strlen(word));    
}

bool starts_with_in_trie(trie_node *root, char *word, int i, int length){
    if(i==length) return true;
    if(root==NULL) return false;
    int index = to_index(word[i]);
    if(root->data[index]==NULL) return false;
    return starts_with_in_trie(root->data[index]->next, word, i+1, length);
}

/** Returns if there is any word in the trie that starts with the given prefix. */
bool trieStartsWith(Trie* obj, char * prefix) {
   return starts_with_in_trie(obj->root, prefix, 0, strlen(prefix));
}

void print_trie(trie_node *root, char *op, int index){
    if(root==NULL) return;
    int i = 0;
    for(;i<26;i++){
        if(root->data[i]){
            op[index] = root->data[i]->c;
            if(root->data[i]->eow){
                op[index+1] = '\0';
                printf("%s\n",op);
            }
            print_trie(root->data[i]->next, op, index+1);
        }
    }
}

void display_trie(Trie *obj){
    char *op = (char*)calloc(100,sizeof(char));
    print_trie(obj->root, op, 0);
}

int delete_in_trie(trie_node *root, char *word, int i, int length){
    if(root==NULL) return 0;
    int index = to_index(word[i]);
    if(root->data[index]==NULL) return 0;
    if(i==length-1){
        if(!root->data[index]->eow) return 0;
        root->data[index]->eow = 0;
        if(root->data[index]->next) return 0;
        free(root->data[index]);
        root->data[index] = NULL;
        root->sibbling_count--;
        return 1;
    }
    if(delete_in_trie(root->data[index]->next, word, i+1, length)){
        if(root->data[index]->next->sibbling_count==0){
            free(root->data[index]);
            root->data[index] = NULL;
            root->sibbling_count--;
            return 1;
        }else{
            return 0;
        }
    }
    return 0;
}


/** deletes the word if it is in the trie. */
bool trieDelete(Trie* obj, char * word) {
    return delete_in_trie(obj->root, word, 0, strlen(word));    
}

void trieFree(Trie* obj) {
    free(obj->root);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/