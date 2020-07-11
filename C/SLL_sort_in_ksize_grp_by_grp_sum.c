/*
You are given a linked list and a number k. 
You have to sort the linked list in groups of size k by the 
    sum value of each individual chunk in decreasing order. 
The elements within a chunk will not change.

Example:
Linked List: 1->3->0->5->1->7->0->2->4->3
k=2

Output: 1->7->4->3->0->5->1->3->0->2

Explanation:
1->3=4
0->5=5
1->7=8
0->2=2
4->3=7
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

list_node* make_list(list_node *head, int data){
    list_node *nw = make_node(data);
    nw->next = head;
    return nw;
}

int get_list_sum(list_node *head){
    int sum = 0;
    for(;head;head=head->next){
        sum+=head->data;
    }
    return sum;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

list_node* copy_list(list_node *head){
    list_node *new_head = NULL;
    list_node *prev = NULL;
    for(;head;head=head->next){
        if(new_head==NULL){
            new_head = make_node(head->data);
            prev = new_head;
        }else{
            prev->next = make_node(head->data);
            prev = prev->next;
        }
    }
    return new_head;
}

/*
Merge to circular list into 1 and return the last node.
*/
list_node* merge_list(list_node *list1, list_node *list2){
    if(list1==NULL) return list2;
    if(list2==NULL) return list1;
    list_node *temp = list2->next;
    list2->next = list1->next;
    list1->next = temp;
    return list2;
}

/*
This returns the head of next group.

It converts the current group to circular list and set the last node of list
    and sum in the given arguments.
*/
list_node* find_k_size_grp_sum(list_node *head, int k, list_node **last, int *sum){
    int t_sum = 0;
    list_node *prev = NULL;
    list_node *t_head = head;
    int i = 0;
    while(t_head && i<k){
        t_sum+=t_head->data;
        prev = t_head;
        t_head = t_head->next;
        i++;
    }
    if(prev){
        prev->next = head;
    }
    *last = prev;
    *sum = t_sum;
    return t_head;
}

list_node* sort_list_in_k_size_grp_by_grp_sum(list_node *head, int k){
    if(k<=0){
        printf("Invalid\n");
        return head;
    }
    int list_sum = get_list_sum(head);
    list_node** list_sum_map = (list_node**)calloc(list_sum+1,sizeof(list_node*));
    list_node *new_head = NULL;
    while(head){
        list_node *last_node = NULL;
        int sum = 0;
        head = find_k_size_grp_sum(head,k,&last_node,&sum);
        list_sum_map[sum] = merge_list(list_sum_map[sum],last_node);    
    }
    list_node *new_list_last_node = NULL;
    int i = list_sum;
    for(;i>=0;i--){
        new_list_last_node = merge_list(new_list_last_node,list_sum_map[i]);
    }
    if(new_list_last_node){
        new_head = new_list_last_node->next;
        new_list_last_node->next = NULL;
    }
    return new_head;
}

int main(){
    int ip[] = { 1,3,0,5,1,7,0,2,4,3};
    int length = sizeof(ip)/sizeof(ip[0]);

    list_node *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = make_list(head,ip[i]);
    }
    print_list(head);

    int k = 0;
    for(;k<=length+1;k++){
        list_node *t_head = copy_list(head);
        printf("K = %d > ",k);
        list_node *new_list_head = sort_list_in_k_size_grp_by_grp_sum(t_head,k);
        print_list(new_list_head);
    }

    return 0;
}