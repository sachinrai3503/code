// https://leetcode.com/problems/possible-bipartition/
/*
Given a set of N people (numbered 1, 2, ..., N), we would like to split
 everyone into two groups of any size.

Each person may dislike some other people, and they should not go
 into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people
 numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups
 in this way.

Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 
Constraints:
1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
*/

#include <limits.h>
#include <stdio.h>
#include <malloc.h>
#define false 0
#define true 1

typedef int bool;

typedef struct node{
    int data;
    struct node *next;
}list_node;

list_node* init_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = node;
    }
    return node;
}

list_node* append(list_node *last, int data){
    list_node *node = init_list_node(data);
    if(last){
        node->next = last->next;
        last->next = node;
    }
    return node;
}

void print_list(list_node *last){
    if(!last){
        printf("\n");
        return;
    }
    list_node *first = last->next;
    list_node *temp = first;
    for(;temp->next!=first;temp=temp->next){
        printf("%d ",temp->data);
    }
    if(temp){
        printf("%d\n",temp->data);
    }
}

typedef struct{
    list_node **data;
    int node_count;
}graph;

graph* init_graph(int node_count){
    graph *_graph = (graph*)malloc(sizeof(graph));
    if(_graph){
        _graph->data = (list_node**)calloc(node_count+1,sizeof(list_node*));
        _graph->node_count = node_count;
    }
    return _graph;
}

void add_undirected_edge(graph *_graph, int v1, int v2){
    if(_graph && v1<=_graph->node_count && v2<=_graph->node_count){
        _graph->data[v1] = append(_graph->data[v1], v2);
        _graph->data[v2] = append(_graph->data[v2], v1);
    }
}

void print_graph(graph *_graph){
    int i = 1;
    for(;i<=_graph->node_count;i++){
        printf("%d>",i);
        print_list(_graph->data[i]);
    }
}

typedef struct{
    int *data;
    int front, rear;
    int max_size;
}queue;

queue* init_que(int max_size){
    queue *que = (queue*)malloc(sizeof(queue));
    if(que){
        que->data = (int*)calloc(max_size, sizeof(int));
        que->front = que->rear = -1;
        que->max_size = max_size;
    }
    return que;
}

bool is_empty(queue *que){
    if(que && que->front==-1) return true;
    return false;
}

bool is_full(queue *que){
    if((que->front==0 && que->rear==que->max_size) || (que->rear==que->front-1))
        return true;
    return false;
}

void insert_queue(queue *que, int data){
    if(is_full(que)){
        printf("Full\n");
        return;
    }else{
        if(que->rear==que->max_size-1) que->rear=0;
        else que->rear++;
        if(que->front==-1) que->front = 0;
        que->data[que->rear] = data;
    }
}

int delete_queue(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = que->data[que->front];
        if(que->front==que->rear) que->front = que->rear = -1;
        else if(que->front==que->max_size-1) que->front = 0;
        else que->front++;
        return temp;
    }
}

bool isComponentBipartite(graph *_graph, char *set, int node){
    if(set[node]!='\0'){
        printf("Vertex %d already visited.\n",node);
        return true;
    }
    queue *que = init_que(_graph->node_count+1);
    insert_queue(que, node);
    set[node] = 'A';
    while(!is_empty(que)){
        int temp = delete_queue(que);
        list_node *adj_list_last = _graph->data[temp];
        if(!adj_list_last) continue;
        list_node *head = adj_list_last->next;
        while(true){
            int adj = head->data;
            if(set[adj]!='\0' && set[adj]==set[temp]) return false;
            else if(set[adj]=='\0'){
                insert_queue(que, adj);
                set[adj] = (set[temp]=='A')?'B':'A';
            }
            if(head==adj_list_last) break;
            else head=head->next;
        }
    }
    return true;
}

graph* get_graph(int N, int** dislikes, int dislikesSize, int* dislikesColSize){
    graph *_graph = init_graph(N);
    int i = 0;
    for(;i<dislikesSize;i++){
        add_undirected_edge(_graph, dislikes[i][0], dislikes[i][1]);
    }
    return _graph;
}

bool possibleBipartition(int N, int** dislikes, int dislikesSize, int* 
                         dislikesColSize){
    graph *_graph = get_graph(N, dislikes, dislikesSize, dislikesColSize);
    // print_graph(_graph);
    char *set = (char*)calloc(N+1, sizeof(char));
    int i = 1;
    for(;i<=_graph->node_count;i++){
        if(set[i]=='\0'){
            bool status = isComponentBipartite(_graph, set, i);
            if(!status) return false; 
        }
    }
    return true;
}