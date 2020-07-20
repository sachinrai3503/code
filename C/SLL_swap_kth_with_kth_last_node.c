// https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/
/*
Given a singly linked list, swap kth node from beginning with kth node from end.
 Swapping of data is not allowed, only pointers should be changed

Input: 1 -> 2 -> 3 -> 4 -> 5, K = 2
Output: 1 -> 4 -> 3 -> 2 -> 5 

Input: 1 -> 2 -> 3 -> 4 -> 5, K = 5
Output: 5 -> 2 -> 3 -> 4 -> 1 
*/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *next;
}list_node;

list_node* make_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

list_node* make_list(list_node *head, int data){
    list_node *node = make_node(data);
    node->next = head;
    return node;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

void print_node(list_node *node){
    if(node){
        printf("%d ",node->data);
    }else{
        printf("NULL ");
    }
}

void swap(list_node **p , list_node **q){
    list_node *temp = *p;
    *p = *q;
    *q = temp;
}

/*
 p & q are kth node from first and last respectively.
 p1 & q1 are prev of p and q.
 qn is q->next
*/
void set_required_node(list_node *head, list_node **p1, list_node **p,
            list_node **q1, list_node **q, list_node **qn, int k){
    *p1 = *p = *q1 = *q = *qn =  NULL;
    if(head==NULL) return;
    list_node *t_head = head;
    int i = 0;
    for(;i<k && t_head;i++,t_head=t_head->next){
        *p1 = *p;
        *p = t_head;
    }
    if(k==0 || i<k){
        printf("Invalid value for k given\n");
        *p1 = *p = NULL;
        return;
    }
    // This is set when the kth last node is after kth node in the list.
    // Used to swap the pointers if kth last node is in 1st half of the list 
    // and kth node in the 2nd half.
    int p_crossed_flag = 0;
    list_node *tp = *p;
    *q = head;
    while(tp && tp->next){
        if(*q==*p){
            p_crossed_flag = 1;
        }
        *q1 = *q;
        *q = (*q)->next;
        tp = tp->next;
    }
    if(p && p_crossed_flag==0){
        swap(q,p);
        swap(q1,p1);
    }
    if(*q)
        *qn = (*q)->next;
}

list_node* swap_kth_with_kth_last_node(list_node *head, int k){
    // p & q are kth node from first and last respectively.
    list_node *p = NULL, *q = NULL; 
    // p1 & q1 are prev of p and q.
    list_node *p1 = NULL, *q1 = NULL;
    // qn = q->next
    list_node *qn = NULL;
    if(k<=0) return head;
    set_required_node(head,&p1,&p,&q1,&q,&qn,k);
    // printf("p1=");print_node(p1);
    // printf("p=");print_node(p);
    // printf("q1=");print_node(q1);
    // printf("q=");print_node(q);
    // printf("qn=");print_node(qn);
    // printf("\n");
    if(p1==NULL){
        head = q;
    }else{
        p1->next = q;
    }
    if(q1 && q1!=p){
        q1->next = p;
    }
    if(q1 && q1!=p){
        q->next = p->next;
    }else if(q1){
        q->next = p;
    }
    if(p)
        p->next = qn;
    return head;
}

int main(){
    int ip[] = {4,5,6,7,8,9,10};
    int length = sizeof(ip)/sizeof(ip[0]);

    list_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);

    int k = 0;
    for(;k<=length+1;k++){
        printf("K=%d ==",k);
        head = swap_kth_with_kth_last_node(head,k);
        print_list(head);
    }

    return 0;
}