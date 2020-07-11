#include <stdio.h>
#include <malloc.h>
#include <limits.h>

// To maintain the graph
struct vertex_node;

typedef struct edge_node{
    int data;
    struct vertex_node *to_vertex;
    struct edge_node *next;
}edge;

typedef struct vertex_node{
    int data;
    edge *edge_list;
}vertex;

typedef struct{
    vertex **vertex_list;
    int vertex_count;
}graph;

edge* init_edge(int data, vertex *to_vertex){
    edge *new_edge = (edge*)malloc(sizeof(edge));
    if(new_edge){
        new_edge->data = data;
        new_edge->to_vertex = to_vertex;
        new_edge->next = NULL;
    }
    return new_edge;
}

vertex* init_vertex(int data, edge *edge_list){
    vertex *new_vertex = (vertex*)malloc(sizeof(vertex));
    if(new_vertex){
        new_vertex->data = data;
        new_vertex->edge_list = edge_list;
    }
    return new_vertex;
}

void set_graph(graph *_graph, int (*graph_mat)[50], int vertex_count){
    int i = 0;
    for(;i<vertex_count;i++){
        _graph->vertex_list[i] = init_vertex(i,NULL);
    }
    for(i=0;i<vertex_count;i++){
        edge *edge_list = NULL;
        edge *prev = NULL;
        int j = 0;
        for(;j<vertex_count;j++){
            if(graph_mat[i][j]==1){
                edge *nw = init_edge(j,_graph->vertex_list[j]);
                if(edge_list==NULL){
                    edge_list = nw;
                }else{
                    prev->next = nw;
                }
                prev = nw;
            }
        }
        _graph->vertex_list[i]->edge_list = edge_list;
    }
}

graph* init_graph(int (*graph_mat)[50], int vertex_count){
    graph *new_graph = (graph*)malloc(sizeof(graph));
    if(new_graph){
        new_graph->vertex_list = (vertex**)calloc(vertex_count,sizeof(vertex*));
        new_graph->vertex_count = vertex_count;
        set_graph(new_graph,graph_mat,vertex_count);
    }
    return new_graph;
}

void print_edge_list(edge *edge_list){
    for(;edge_list;edge_list=edge_list->next){
        printf("%d ",edge_list->data);
    }
    printf("\n");
}

void print_graph(graph *_graph){
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        printf("Vertex = %d >",_graph->vertex_list[i]->data);
        print_edge_list(_graph->vertex_list[i]->edge_list);
    }
}

// To maintain the visited vertex
int is_visted(vertex *_vertex, int *visited){
    if(visited[_vertex->data]==1)return 1;
    return 0;
}

void mark_visited(vertex *_vertex, int *visited){
    visited[_vertex->data] = 1;
}

// To maintain queue used in BFS
typedef struct{
    vertex **data;
    int front, rear;
    int max_size;
}queue;

queue* init_queue(int max_size){
    queue *que = (queue*)malloc(sizeof(que));
    if(que){
        que->data = (vertex**)calloc(max_size,sizeof(vertex*));
        que->front = que->rear = -1;
        que->max_size = max_size;
    }
    return que;
}

int is_full(queue *que){
    if((que->front==0 && que->rear==que->max_size-1) || (que->rear==que->front-1)) return 1;
    return 0;
}

int is_empty(queue *que){
    if(que->front==-1) return 1;
    return 0;
}

void insert_queue(queue *que, vertex *data){
    if(is_full(que)){
        printf("Full\n");
    }else{
        if(que->rear==que->max_size-1) que->rear = 0;
        else que->rear++;
        if(que->front==-1) que->front = 0;
        que->data[que->rear] = data;
    }
}

vertex* delete_queue(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return NULL;
    }else{
        vertex *temp = que->data[que->front];
        if(que->front==que->rear) que->front = que->rear = -1;
        else if(que->front==que->max_size-1) que->front = 0;
        else que->front++;
        return temp;
    }
}

void print_queue(queue *que){
    int i = que->front;
    if(i>que->rear){
        while(i<que->max_size-1){
            printf("%d ",que->data[i]->data);
            i++;
        }
        i = 0;
    }
    while(i<=que->rear){
        printf("%d ",que->data[i]->data);
        i++;
    }
    printf("\n");
}