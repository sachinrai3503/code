// https://leetcode.com/problems/course-schedule/
/*
There are a total of numCourses courses you have to take, labeled from 0 to
 numCourses - 1. You are given an array prerequisites where
 prerequisites[i] = [ai, bi] indicates that you must take course bi first
 if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you
 should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
*/

#include <stdio.h>
#include <limits.h>
#define true 1
#define false 0

typedef int bool;

typedef struct list_node{
    int data;
    struct list_node *next;
}adj_list_node;

adj_list_node* init_node(int data){
    adj_list_node *node = (adj_list_node*)malloc(sizeof(adj_list_node));
    if(node){
        node->data = data;
        node->next = node;
    }
    return node;
}

adj_list_node* add_to_adj_list(adj_list_node *last, int data){
    adj_list_node *node = init_node(data);
    if(last==NULL) return node;
    node->next = last->next;
    last->next = node;
    return node;
}

typedef struct {
    adj_list_node **data;
    int max_size;
    int *in_degree;
}adj_list_graph;

adj_list_graph* init_graph(int max_size){
    adj_list_graph *graph = (adj_list_graph*)malloc(sizeof(adj_list_graph));
    if(graph){
        graph->data = (adj_list_node**)calloc(max_size, sizeof(adj_list_node*));
        graph->max_size = max_size;
        graph->in_degree = (int*)calloc(max_size, sizeof(int));
    }
    return graph;
}

adj_list_graph* get_graph(int vertex_count, int **edges, int edges_len){
    adj_list_graph *graph = init_graph(vertex_count);
    int i = 0;
    for(;i<edges_len;i++){
        int a = edges[i][1];
        int b = edges[i][0];
        graph->data[a] = add_to_adj_list(graph->data[a], b);
        graph->in_degree[b]++;
    }
    return graph;
}

typedef struct{
    int *data;
    int front, rear;
    int max_size;
}queue;

queue* init_queue(int max_size){
    queue *que = (queue*)malloc(sizeof(queue));
    if(que){
        que->data = (int*)calloc(max_size, sizeof(int));
        que->front = que->rear = -1;
        que->max_size = max_size;
    }
    return que;
}

bool is_full(queue *que){
    if((que->front==0 && que->rear==que->max_size-1) || (que->rear==que->front-1)){
        return true;
    }
    return false;
}

bool is_empty(queue *que){
    if(que->front==-1) return true;
    return false;
}

int get_front(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return INT_MIN;
    }
    return que->data[que->front];
}

void insert_queue(queue *que, int data){
    if(is_full(que)){
        printf("Full\n");
        return;
    }else{
        if(que->rear==que->max_size-1) que->rear=0;
        else que->rear++;
        if(que->front==-1) que->front=0;
        que->data[que->rear] = data;
    }
}

int delete_front(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = que->data[que->front];
        if(que->rear==que->front) que->rear=que->front=-1;
        else if(que->front==que->max_size-1) que->front=0;
        else que->front++;
        return temp;
    }
}

bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize){
    // if(prerequisitesSize==0) return true;
    adj_list_graph *graph = get_graph(numCourses, prerequisites, prerequisitesSize);
    queue *que = init_queue(numCourses);
    // printf("%d %d %d %d\n",que->data, que->front, que->rear, que->max_size);
    // printf("%d %d \n",graph->data, graph->max_size);
    int completed_course_count = 0;
    int i = 0;
    for(;i<numCourses;i++){
        if(graph->in_degree[i]==0){
            // printf("HERE\n");
            insert_queue(que, i);
        }
    }
    while(!is_empty(que)){
        int temp = delete_front(que);
        completed_course_count++;
        adj_list_node *last = graph->data[temp];
        if(last){
            adj_list_node *adj_node = last->next;
            for(;adj_node!=last;adj_node=adj_node->next){
                graph->in_degree[adj_node->data]--;
                if(graph->in_degree[adj_node->data]==0) insert_queue(que, adj_node->data);
            }
            graph->in_degree[adj_node->data]--;
            if(graph->in_degree[adj_node->data]==0) insert_queue(que, adj_node->data);
        }
    }
    if(completed_course_count==numCourses) return true;
    return false;
}