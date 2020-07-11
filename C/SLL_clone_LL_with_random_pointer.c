// https://www.geeksforgeeks.org/clone-linked-list-next-random-pointer-o1-space/
/*
Given a linked list having two pointers in each node. 
The first one points to the next node of the list, however,
 the other pointer is random and can point to any node of the list.
 Write a program that clones the given list in O(1) space,
  i.e., without any extra space.
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *next;
    struct node *random;
}list_node;

list_node* init_node(int data){
    list_node *nw = (list_node*)malloc(sizeof(list_node));
    if(nw){
        nw->data = data;
        nw->next = NULL;
        nw->random = NULL;
    }
    return nw;
}

list_node* make_list(list_node *head, int data){
    list_node *nw = init_node(data);
    nw->next = head;
    return nw;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("(%d-%d-%d) ",head->data,head->random->data,head);
    }
    printf("\n");
}

list_node* get_node(list_node *head, int data){
    for(;head;head=head->next){
        if(head->data==data) return head;
    }
    return NULL;
}

void create_new_list(list_node *head){
    list_node *p = head;
    while(p){
        list_node *nw = init_node(p->data);
        nw->next = p->next;
        p->next = nw;
        p = nw->next;
    }
}

void link_random(list_node *head){
    list_node *p = head;
    while(p){
        p->next->random = p->random->next;
        p=p->next->next;
    }
}

list_node* get_cloned_list(list_node *head){
    list_node *new_head = NULL;
    list_node *p = head;
    while(p){
        list_node *cloned_node = p->next;
        if(!new_head) new_head = cloned_node;
        p->next = cloned_node->next;
        if(cloned_node->next){
            cloned_node->next = cloned_node->next->next;
        }else{
            cloned_node->next = NULL;
        }
        p = p->next;
    }
    return new_head;
}

list_node* clone_list(list_node *head){
    create_new_list(head);
    link_random(head);
    return get_cloned_list(head);
}

int main(){
    int ip[] = {1,2,3,4,5};
    int random[] = {3,1,5,3,2};
    int length = sizeof(ip)/sizeof(ip[0]);

    list_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    list_node *p = head;
    for(i=0;p;p=p->next,i++){
        p->random = get_node(head,random[i]);
    }
    print_list(head);

    list_node *cloned_head = clone_list(head);
    print_list(cloned_head);

    return 0;
}