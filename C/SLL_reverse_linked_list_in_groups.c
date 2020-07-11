//https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
//https://www.geeksforgeeks.org/reverse-linked-list-groups-given-size-set-2/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *next;
}my_node;

my_node* make_node(int data){
    my_node *nw = (my_node*)malloc(sizeof(my_node));
    if(nw){
        nw->data = data;
        nw->next = NULL;
    }
    return nw;
}

my_node* make_list(my_node *head, int data){
    my_node *nw = make_node(data);
    nw->next = head;
    return nw;
}

void print_list(my_node *head){
    while(head){
        printf("%d ",head->data);
        head = head->next;
    }
    printf("\n");
}

my_node* reverse_list_till_size(my_node *head, int k){
    my_node *p = head, *q = NULL, *r = NULL;
    int i = 0;
    while(p && i<k){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
        i++;
    }
    if(k>0){
        head->next = p;
    }else return head;
    return q;
}

my_node* reverse_list_in_groups_size(my_node *head, int size){
    my_node *prev = NULL;
    my_node *new_head = NULL;
    while(head){
        my_node *reversed_node = reverse_list_till_size(head,size);
        if(new_head==NULL){
            new_head = reversed_node;
        }else{
            prev->next = reversed_node;
        }
        prev = head;
        head = head->next;
    }
    return new_head;
}

int main(){
    int ip[] = {1,2,3,4,5,6,7};
    int length = sizeof(ip)/sizeof(ip[0]);
    
    my_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);

    i = 0;
    for(;i<=length+1;i++){
        head = reverse_list_in_groups_size(head,i);
        printf("size = %d >",i);
        print_list(head);
    }

    return 0;
}