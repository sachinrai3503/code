// https://www.geeksforgeeks.org/flattening-a-linked-list/
/*
Given a LL where every node represents a LL and contains 2 pointers of its type:
(i) Pointer to next node in the main list (we call it ‘right’ pointer)
(ii) Pointer to a LL where this node is head (we call it ‘down’ pointer).
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
Write a function flatten() to flatten the lists into a single linked list. 
The flattened linked list should also be sorted. 

For example, for the above input list, output list should be 
5->7->8->10->19->20->22->28->30->35->40->45->50.
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct SLL_Node{
    int data;
    struct SLL_Node *next, *child;
}list_node;

list_node* make_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = node->child = NULL;
    }
    return node;
}

list_node* connect_child_node(int *ip, int length){
    list_node *head = NULL;
    list_node *prev = NULL;
    int i = 0;
    for(;i<length && ip[i]!=-1;i++){
        list_node *node = make_list_node(ip[i]);
        if(!head) head = node;
        else prev->child = node;
        prev = node;
    }
    return head;
}

list_node* connect_next_node(list_node **ip, int length){
    list_node *head = NULL;
    list_node *prev = NULL;
    int i = 0;
    for(;i<length;i++){
        if(ip[i]==NULL) continue;
        if(!head) head = ip[i];
        else prev->next = ip[i];
        prev = ip[i];
    }
    return head;
}

void print_child(list_node *head){
    for(;head;head=head->child)
        printf("%d ",head->data);
    printf("\n");
}

void print_list(list_node *head){
    for(;head;head=head->next)
        print_child(head);
}

void print_list2(list_node *head){
    for(;head;head=head->next){
        printf("%d ==>",head->data);
        if(head->child) print_child(head);
        else printf("NULL\n");
    }
}

typedef struct {
    list_node **data;
    int current_size, max_size;
}heap;

heap* init_heap(int max_size){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = (list_node**)calloc(max_size,sizeof(list_node*));
        _heap->current_size = 0;
        _heap->max_size = max_size;
    }
    return _heap;
}

int is_full(heap *_heap){
    if(_heap && _heap->current_size==_heap->max_size) return 1;
    return 0;
}

int is_empty(heap *_heap){
    if(_heap && _heap->current_size==0) return 1;
    return 0;
}

void swap(list_node **a, list_node **b){
    list_node *temp = *a;
    *a = *b;
    *b = temp;
}

void min_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int min_index = index;
    if(left<_heap->current_size && 
       _heap->data[left]->data < _heap->data[min_index]->data)
        min_index = left;
    if(right<_heap->current_size && 
       _heap->data[right]->data < _heap->data[min_index]->data)
        min_index = right;
    if(min_index!=index){
        swap(_heap->data+index, _heap->data+min_index);
        min_heapify(_heap, min_index);
    }
}

void insert_heap(heap *_heap, list_node *data){
    if(_heap && is_full(_heap)){
        printf("Full\n");
    }
    else if(_heap && data){
        _heap->data[_heap->current_size++] = data;
        int parent_index = (_heap->current_size-2)/2;
        for(;parent_index>0;parent_index = (parent_index-1)/2){
            min_heapify(_heap, parent_index);
        }
        if(parent_index==0){
            min_heapify(_heap, parent_index);
        }
    }
}

list_node* delete_top(heap *_heap){
    if(is_empty(_heap)){
        printf("Empty\n");
        return NULL;
    }
    list_node *temp = _heap->data[0];
    _heap->data[0] = _heap->data[--_heap->current_size];
    min_heapify(_heap,0);
    return temp;
}

list_node* flatten_lists(list_node *head, int list_count){
    list_node *prev = NULL, *new_head = NULL;
    heap *_heap = init_heap(list_count);
    for(;head;head=head->next){
        insert_heap(_heap, head);
    }
    while(!is_empty(_heap)){
        list_node *temp = delete_top(_heap);
        if(!new_head) new_head = temp;
        else prev->next = temp;
        if(temp->child){
            insert_heap(_heap, temp->child);
            temp->child = NULL;
        }
        prev = temp;
    }
    return new_head;
}

int main(){

    // Child are represented in cols where -1 means end of list.
    // New row is next list.
    int ip[50][50] = {  {5,7,8,30,-1},
                        {10,-1,-1},
                        {19,22,50,-1},
                        {28,-1}
                    };
    int row = 4;
    int col = 10;

    list_node **heads = (list_node**)calloc(row,sizeof(list_node*));
    int i = 0;
    for(;i<row;i++){
        heads[i] = connect_child_node(ip[i],col);
    }
    list_node *head = connect_next_node(heads, row);
    print_list(head);
    printf("============================\n");
    
    // NOTE : In the flattened list nodes are connected via 'NEXT' pointer.
    list_node *flatten_head = flatten_lists(head, row);
    print_list2(flatten_head);

    return 0;
}