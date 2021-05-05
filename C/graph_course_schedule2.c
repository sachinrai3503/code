// https://leetcode.com/problems/course-schedule-ii/
/*
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi]
 this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs,
 return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish
 all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should
 have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should
 have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
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

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findOrder(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize, int* returnSize){
    adj_list_graph *graph = get_graph(numCourses, prerequisites, prerequisitesSize);
    queue *que = init_queue(numCourses);
    // printf("%d %d %d %d\n",que->data, que->front, que->rear, que->max_size);
    // printf("%d %d \n",graph->data, graph->max_size);
    int *op = (int*)calloc(numCourses, sizeof(int));
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
        op[completed_course_count++] = temp;
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
    *returnSize = completed_course_count;
    if(completed_course_count==numCourses) return op;
    *returnSize = 0;
    return NULL;
}