// geeksforgeeks.org/merge-sort-for-linked-list/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *next;
}list_node;

list_node* make_list_node(int data){
    list_node *nw = (list_node*)malloc(sizeof(list_node));
    if(nw){
        nw->data = data;
        nw->next = NULL;
    }
    return nw;
}

list_node* make_list(list_node *head, int data){
    list_node *nw = make_list_node(data);
    nw->next = head;
    return nw;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

list_node* get_middle_node(list_node *head){
    list_node *slow = head, *fast = head;
    while(fast && fast->next){
        fast=fast->next;
        if(fast->next){
            fast=fast->next;
            slow=slow->next;
        }
    }
    return slow;
}

list_node* get_last_smaller_node(list_node *list1, int data){
    list_node *prev = NULL;
    for(;list1 && list1->data<=data;list1=list1->next) prev = list1;
    return prev;
}

list_node* merge_2_sorted_list(list_node *list1, list_node *list2){
    if(list1==NULL) return list2;
    if(list2==NULL) return list1;
    list_node *new_head = NULL, *prev = NULL;
    while(list1 && list2){
        list_node *last_smaller_node = get_last_smaller_node(list2,list1->data);
        if(new_head==NULL){
            if(last_smaller_node) new_head = list2;
            else new_head = list1;
        }else{
            if(last_smaller_node) prev->next = list2;
            else prev->next = list1;
        }
        if(last_smaller_node){
            list2 = last_smaller_node->next;
            last_smaller_node->next = list1;
        }
        prev = list1;
        list1 = list1->next;
    }
    if(list1==NULL){
        prev->next = list2;
    }
    return new_head;
}

list_node* merge_sort_list(list_node *head){
    if(head==NULL) return NULL;
    if(head->next==NULL) return head;
    list_node *middle_node = get_middle_node(head);
    // printf("middle = %d\n",middle_node->data);
    list_node *_1st_half = head;
    list_node *_2nd_half = middle_node->next;
    middle_node->next = NULL;
    list_node *list1 = merge_sort_list(_1st_half);
    list_node *list2 = merge_sort_list(_2nd_half);
    return merge_2_sorted_list(list1,list2);
}

int main(){

    int ip[] = {40,20,60,10,50,30};
    int length = sizeof(ip)/sizeof(ip[0]);

    list_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);

    print_list(merge_sort_list(head));

    return 0;
}