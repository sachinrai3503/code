// https://www.geeksforgeeks.org/merge-two-sorted-lists-place/
/*
Given two sorted lists, merge them so as to produce 
 a combined sorted list (without using extra space).

Examples:

Input : head1: 5->7->9
        head2: 4->6->8 
Output : 4->5->6->7->8->9
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *next;
}list_node;

list_node* make_node(int data){
    list_node *nw = (list_node*)malloc(sizeof(list_node));
    if(nw){
        nw->data = data;
        nw->next = NULL;
    }
    return nw;
}

void print_list(list_node *head){
    for(;head;head=head->next)
        printf("%d ",head->data);
    printf("\n");
}

list_node* insert_in_list(list_node *list, int data){
    list_node *nw = make_node(data);
    list_node *prev = NULL;
    list_node *head = list;
    for(;head;head=head->next)
        prev = head;
    if(prev==NULL)
        return nw;
    else
        prev->next = nw;
    return list;
}

list_node* to_list(int ip[], int length){
    list_node *head = NULL;
    int i = 0;
    for(;i<length;i++){
        head = insert_in_list(head,ip[i]);
    }
    return head;
}

list_node* get_last_smaller_node(list_node *list, int data){
    list_node *prev = NULL;
    for(;list && list->data<=data;list=list->next)
        prev = list;
    return prev;
}

list_node* merge_2_list(list_node *list1, list_node *list2){
    if(list1==NULL) return list2;
    if(list2==NULL) return list1;
    list_node *new_list = NULL;
    list_node *prev = NULL;
    while(list1 && list2){
        list_node *last_smaller_node = get_last_smaller_node(list2,list1->data);
        if(new_list==NULL){
            if(last_smaller_node==NULL) new_list = list1;
            else new_list = list2;
        }else{
            if(last_smaller_node==NULL) prev->next = list1;
            else prev->next = list2;
        }
        if(last_smaller_node){
            list2 = last_smaller_node->next;
            last_smaller_node->next = list1;
        }
        prev = list1;
        list1 = list1->next;
    }
    if(list2){
        prev->next = list2;
    }
    return new_list;
}

int main(){
    int ip1[] = {10,30,50,70,90,110};
    int ip2[] = {200,400,600,800};
    int len1 = sizeof(ip1)/sizeof(ip1[0]);
    int len2 = sizeof(ip2)/sizeof(ip2[0]);

    list_node *head1 = NULL, *head2 = NULL;
    head1 = to_list(ip1,len1);
    head2 = to_list(ip2,len2);

    print_list(head1);
    print_list(head2);
    print_list(merge_2_list(head1,head2));

    return 0;
}