// https://www.geeksforgeeks.org/remove-invalid-parentheses/
/*
An expression will be given which can contain open and close parentheses 
and optionally some characters, No other operator will be there in string. 
We need to remove minimum number of parentheses to make the input string valid. 

If more than one valid output are possible removing same number of parentheses 
then print all such output.

Examples:
Input  : str = “()())()” -
Output : ()()() (())()

Input  : str = (v)())()
Output : (v)()()  (v())()
*/

// Python based sol using que @remove_invalid_paranthesis.py
// Below sol. can print same valid exp. more than once. In python this is 
// avoided using set.

#include <stdio.h>
#include <limits.h>
#include <malloc.h>
#include <string.h>

char* copy_arr(char *ip, int length){
    char *op = (char*)calloc(length+1,sizeof(char));
    int i = 0;
    for(;i<length;i++){
        op[i] = ip[i];
    }
    op[i] = '\0';
    return op;
}

typedef struct node{
    char *data;
    int length;
    struct node *next;
}list_node;

list_node* make_node(char *data, int length){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = copy_arr(data,length);
        node->length = length;
        node->next = node;
    }
    return node;
}

list_node* append_node(list_node *last, list_node *data){
    if(data==NULL){
        return last;
    }else{
        if(last){
            data->next = last->next;
            last->next = data;
        }
        return data;
    }
}

void print_list(list_node *last){
    if(last){
        list_node *first = last->next;
        for(;first!=last;first=first->next){
            printf("%s ",first->data);
        }
        printf("%s\n",first->data);
    }
}

typedef struct {
    int min_bracket_removed;
    list_node *last;
}valid_list;

valid_list* init_valid_list(){
    valid_list *list = (valid_list*)malloc(sizeof(valid_list));
    if(list){
        list->min_bracket_removed = INT_MAX;
        list->last = NULL;
    }
    return list;
}

int is_paranthesis(char c){
    if(c=='(' || c==')') return 1;
    return 0;
}

int is_valid_exp(char *ip, int length){
    int count = 0;
    int i = 0;
    for(;i<length;i++){
        if(ip[i]=='(') count++;
        else if(ip[i]==')') count--;
        if(count<0) return 0;
    }
    if(count>0) return 0;
    return 1;
}

void print_valid_expression(char *ip, int length, int index, 
    int bracket_removed_count, char *op, int k, valid_list *list){
        if(length<0 || index <0 || k<0) return;
        if(index==length){
            if(is_valid_exp(op,k) && 
                bracket_removed_count<=list->min_bracket_removed){
                    if( list->last && 
                        bracket_removed_count<list->min_bracket_removed){
                        free(list->last->next);
                        list->last = NULL;
                        list->min_bracket_removed = INT_MAX;
                    }
                    list->last = append_node(list->last,make_node(op,k));
                    list->min_bracket_removed = bracket_removed_count;
                }
            return;
        }
        op[k] = ip[index];
        print_valid_expression(ip,length,index+1,bracket_removed_count,op,k+1,
            list);
        if(is_paranthesis(ip[index]) && 
            bracket_removed_count<list->min_bracket_removed){
            print_valid_expression(ip,length,index+1,bracket_removed_count+1,op,
                k,list);
        }
}

int main(){
    char *ip = "(v)(((v)";
    int length = strlen(ip);

    printf("Ip=>%s\n",ip);

    char *op = (char*)calloc(length+1,sizeof(char));
    valid_list *list = init_valid_list();
    print_valid_expression(ip,length,0,0,op,0,list);
    printf("Min. bracet removed = %d\n",list->min_bracket_removed);
    print_list(list->last);

    return 0;
}