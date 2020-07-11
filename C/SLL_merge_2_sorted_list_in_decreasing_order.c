// https://www.geeksforgeeks.org/merge-two-sorted-linked-lists-such-that-merged-list-is-in-reverse-order/
/*
Given two linked lists sorted in increasing order.
 Merge them such a way that the result list is in decreasing order (reverse order).

Examples:

Input:  a: 5->10->15->40
        b: 2->3->20 
Output: res: 40->20->15->10->5->3->2
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

list_node* make_list(list_node *head, list_node *data){
    if(data==NULL) return head;
    data->next = head;
    return data;
}

list_node* merge_decreasing_order(list_node *head1, list_node *head2){
    list_node *new_head = NULL;
    while(head1 && head2){
        list_node *min_node = NULL;
        if(head1->data<head2->data){
            min_node = head1;
            head1 = head1->next;
        }else{
            min_node = head2;
            head2 = head2->next;
        }
        min_node->next = NULL;
        new_head = make_list(new_head,min_node);
    }
    while(head1){
        list_node *min_node = head1;
        head1 = head1->next;
        min_node->next = NULL;
        new_head = make_list(new_head,min_node);
    }
    while(head2){
        list_node *min_node = head2;
        head2 = head2->next;
        min_node->next = NULL;
        new_head = make_list(new_head,min_node);
    }
    return new_head;
}

int main(){
    int ip1[] = {5,10,15,20,40};
    int ip2[] = {2,3,20};
    int len1 = sizeof(ip1)/sizeof(ip1[0]);
    int len2 = sizeof(ip2)/sizeof(ip2[0]);

    list_node *head1 = NULL, *head2 = NULL;
    head1 = to_list(ip1,len1);
    head2 = to_list(ip2,len2);

    print_list(head1);
    print_list(head2);
    print_list(merge_decreasing_order(head1,head2));

    return 0;
}