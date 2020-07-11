// https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
/*
Given an array of words, print all anagrams together. 

For example, if the given array is 
{“cat”, “dog”, “tac”, “god”, “act”}, then output may be 
“cat tac act dog god”.
*/

// Here solution with sort is done.
// For map based solution see dict_group_anagrams.py.

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <string.h>

void print_arr_of_string(char *ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%s ",ip[i]);
    }
    printf("\n");
}

typedef struct{
    char **words;
    int *index;
}word_arr;

/*
Returns a word_arr node which has all the string in given ip arr
and there index.
*/
word_arr* make_word_arr(char *ip[], int length){
    void init_word_arr(word_arr*,char**,int);
    word_arr *nw = (word_arr*)malloc(sizeof(word_arr));
    if(nw){
        nw->words = (char**)calloc(length,sizeof(char*));
        nw->index = (int*)calloc(length,sizeof(int));
        init_word_arr(nw,ip,length);
    }
    return nw;
}

char* copy_string(char *ip, int length){
    char *op = (char*)calloc(length+1,sizeof(char));
    int i = 0;
    for(;i<length;i++){
        op[i] = ip[i];
    }
    op[i] = '\0';
    return op;
}

/*
Initializes the word_arr node with the arr of string given
and there index in the given string.
*/
void init_word_arr(word_arr *arr, char **from, int length){
    int i = 0;
    for(;i<length;i++){
        arr->words[i] = copy_string(from[i],strlen(from[i]));
        arr->index[i] = i;
    }
}

void swap_letter(char *a, char *b){
    char temp = *a;
    *a = *b;
    *b = temp;
}

/*
Sort a given string

For simplicity using normal sort.
Better is using heap/merge.
*/
void sort_word(char *ip, int length){
    int i = 0;
    for(;i<length;i++){
        int min_index = i;
        int j = i+1;
        for(;j<length;j++){
            if(ip[min_index]>ip[j]){
                min_index = j;
            }
        }
        swap_letter(ip+i,ip+min_index);
    }
}

/*
sort each string in the arr
*/
void sort_string_arr(char *ip[], int length){
    int i = 0;
    for(;i<length;i++){
        sort_word(ip[i],strlen(ip[i]));
    }
}

/*
Returns 1 if str1 is <= str2
        else 2
*/
int compare_two_word(char *word1, char *word2){
    int word1_len = strlen(word1);
    int word2_len = strlen(word2);
    int i = 0, j = 0;
    for(;i<word1_len && j<word2_len;i++,j++){
        if(word1[i]>word2[j]) return 2;
        else if(word1[i]<word2[j]) return 1;
    }
    if(i==word1_len) return 1;
    return 2;
}

void swap_word(char **a, char **b){
    char *temp = *a;
    *a = *b;
    *b = temp;
}

void swap_index(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

/*
Sorts the sorted words in the word_arr and 
also take care of there index while sorting.
*/
void sort_word_arr(word_arr *arr, int length){
    int i = 0;
    for(;i<length;i++){
        int min_index = i;
        int j = i+1;
        for(;j<length;j++){
            if(compare_two_word(arr->words[min_index],arr->words[j])==2){
                min_index = j;
            }
        }
        swap_word(arr->words+i,arr->words+min_index);
        swap_index(arr->index+i,arr->index+min_index);
    }
}

void print_all_anagrams_together(char *ip[], int length){
    word_arr *arr = make_word_arr(ip,length);
    sort_string_arr(arr->words,length);
    sort_word_arr(arr,length);
    int i = 0;
    for(;i<length;i++){
        printf("%s ",ip[arr->index[i]]);
    }
}

int main(){
    char *ip[] = {"cat", "dog", "tac", "god", "act","doggy","ggdoy"};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr_of_string(ip,length);
    print_all_anagrams_together(ip,length);

    return 0;
}