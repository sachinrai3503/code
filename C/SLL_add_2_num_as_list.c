#include <stdio.h>
#include <limits.h>
#include <malloc.h>

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

list_node* insert_at_end(list_node *head, list_node *data){
    list_node *prev = NULL;
    list_node *temp = head;
    for(;temp;temp=temp->next){
        prev = temp;
    }
    if(prev==NULL) return data;
    else prev->next = data;
    return head;
}

list_node* insert_at_front(list_node *head, list_node *data){
    if(data==NULL) return head;
    data->next = head;
    return data;
}

list_node* to_list(int ip[], int length){
    list_node *head = NULL;
    int i = 0;
    for(;i<length;i++){
        head = insert_at_end(head,make_node(ip[i]));
    }
    return head;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

int get_data(list_node *node){
    if(node) return node->data;
    return 0;
}

int get_length(list_node *node){
    int len = 0;
    for(;node;node=node->next) len++;
    return len;
}

// https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
/*
Input:
List1: 5->6->3 // represents number 365
List2: 8->4->2 // represents number 248
Output:
Resultant list: 3->1->6 // represents number 613
Explanation: 365 + 248 = 613
*/
list_node* add_list(list_node *head1, list_node *head2){
    list_node *new_head = NULL;
    list_node *prev = NULL;
    int carry = 0, sum = 0;
    while(head1 || head2){
        int a = get_data(head1);
        int b = get_data(head2);
        sum = a + b + carry;
        list_node *nw = make_node(sum%10);
        carry = sum/10;
        if(new_head==NULL) new_head = nw;
        else prev->next = nw;
        prev = nw;
        if(head1) head1 = head1->next;
        if(head2) head2 = head2->next;
    }
    if(carry && prev){
        prev->next = make_node(carry);
    }
    return new_head;
}

// https://www.geeksforgeeks.org/sum-of-two-linked-lists/
/*
Input:
  First List: 5->6->3  // represents number 563
  Second List: 8->4->2 //  represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405
*/
list_node* add_list2_rec(list_node *list1, int list1_len, list_node *list2, int list2_len, int *carry){
    if(list1==NULL && list2==NULL){
        *carry = 0;
        return NULL;
    }
    int a = 0, b = 0, sum = 0;
    list_node *temp = NULL;
    if(list1_len==list2_len){
        temp = add_list2_rec(list1->next,list1_len-1,list2->next,list2_len-1,carry);
        a = get_data(list1);
        b = get_data(list2);
    }else if(list1_len>list2_len){
        temp = add_list2_rec(list1->next,list1_len-1,list2,list2_len,carry);
        a = get_data(list1);
        b = 0;
    }else{
        temp = add_list2_rec(list1,list1_len,list2->next,list2_len-1,carry);
        a = 0;
        b = get_data(list2);
    }
    sum = a + b + *carry;
    *carry = sum/10;
    list_node *nw = make_node(sum%10);
    nw->next = temp;
    return nw;
}

list_node* add_list2(list_node *list1, list_node *list2){
    int carry = 0;
    list_node *new_list = add_list2_rec(list1,get_length(list1),list2,get_length(list2),&carry);
    if(carry!=0){
        new_list = insert_at_front(new_list,make_node(carry));
    }
    return new_list;
}

int main(){
    int ip1[] = {9,9,3,9};
    int ip2[] = {2,6};
    int len1 = sizeof(ip1)/sizeof(ip1[0]);
    int len2 = sizeof(ip2)/sizeof(ip2[0]);

    list_node *list1 = to_list(ip1,len1);
    list_node *list2 = to_list(ip2,len2);

    printf("list1 =>");
    print_list(list1);
    printf("list2 =>");
    print_list(list2);

    printf("sum(msd at last) =>");
    print_list(add_list(list1,list2));
    printf("sum(msd at first) =>");
    print_list(add_list2(list1,list2));

    return 0;
}