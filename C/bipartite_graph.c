// https://leetcode.com/problems/is-graph-bipartite/
// https://www.geeksforgeeks.org/bipartite-graph/
// Note - GFG sol "From the property of graphs we can infer that , A graph
//  containing odd number of cycles or Self loop  is Not Bipartite." is not
//  correct. ip = [[1,3],[0,2],[1,3],[0,2,4],[3]]

/*
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two 
 independent subsets A and B, such that every edge in the graph has one
 node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j
 for which the edge between nodes i and j exists.  Each node is an integer 
 between 0 and graph.length - 1.  

There are no self edges or parallel edges: graph[i] does not contain i, 
 and it doesn't contain any element twice.

Example 1:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to divide the set of nodes into 2 independent
 subsets.

 

Constraints:
1 <= graph.length <= 100
0 <= graph[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected. 
*/

#include <limits.h>
#include <stdio.h>
#include <malloc.h>
#define false 0
#define true 1

typedef int bool;

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

bool isComponentBipartite(int **graph, int graphSize, int *graphColSize, 
                          bool *visited, char *set, int index){
    if(visited[index]){
        printf("Vertex %d already visited.\n",index);
        return true;
    }
    queue *que = init_que(graphSize);
    insert_queue(que, index);
    visited[index] = true;
    set[index] = 'A';
    while(!is_empty(que)){
        int temp = delete_queue(que);
        int i = 0;
        for(;i<graphColSize[temp];i++){
            int adj = graph[temp][i];
            if(visited[adj] && set[adj]==set[temp]) return false;
            else if(!visited[adj]){
                insert_queue(que, adj);
                visited[adj] = true;
                set[adj] = (set[temp]=='A')?'B':'A';
            }
        }
    }
    return true;
}

bool isBipartite(int** graph, int graphSize, int* graphColSize){
    bool *visited = (bool*)calloc(graphSize, sizeof(bool));
    char *set = (char*)calloc(graphSize, sizeof(char));
    int i = 0;
    for(;i<graphSize;i++){
        if(!visited[i]){
            bool status = isComponentBipartite(graph, graphSize, graphColSize, 
                                               visited, set, i);
            if(!status) return false; 
        }
    }
    return true;
}