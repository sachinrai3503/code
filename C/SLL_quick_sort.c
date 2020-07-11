// https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/

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

list_node* get_last_node(list_node *head){
    for(;head && head->next;head=head->next);
    return head;
}

void find_pivot(list_node *head, list_node **pivot, list_node **smaller_than_pivot, list_node **greater_than_pivot){
    *pivot = *smaller_than_pivot = *greater_than_pivot = NULL;
    list_node *cur = NULL;
    for(;head;){
        cur = head;
        head=head->next;
        if(!*pivot){
            *pivot = cur;
            (*pivot)->next = NULL;
        }else if(cur->data<=(*pivot)->data){
            cur->next = *smaller_than_pivot;
            *smaller_than_pivot = cur;
        }else{
            cur->next = *greater_than_pivot;
            *greater_than_pivot = cur;
        }
    }
}

list_node* quick_sort_SLL(list_node *head){
    if(!head) return NULL;
    if(head->next==NULL)  return head;
    list_node *pivot = NULL;
    list_node *smaller_than_pivot = NULL;
    list_node *greater_than_pivot = NULL;
    find_pivot(head,&pivot,&smaller_than_pivot,&greater_than_pivot);
    // printf("pivot = %d ",pivot->data);
    // printf("smaller => "); print_list(smaller_than_pivot);
    // printf("greater => "); print_list(greater_than_pivot);
    list_node *l1 = quick_sort_SLL(smaller_than_pivot);
    list_node *l2 = quick_sort_SLL(greater_than_pivot);
    list_node *new_head = NULL;
    if(l1){
        new_head=l1;
        get_last_node(l1)->next = pivot;
    }else{
        new_head=pivot;
    }
    pivot->next = l2;
    return new_head;
}

int main(){

    int ip[] = {40,30,20,60,10,50,50,30};
    int length = sizeof(ip)/sizeof(ip[0]);

    list_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);

    print_list(quick_sort_SLL(head));

    return 0;
}