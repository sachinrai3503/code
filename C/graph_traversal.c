// https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
// https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include "graph_util.h"

/*
Traverses a connected component using DFS.
*/
void traverse_adjacent_edge_dfs(vertex *_vertex, int *visited){
    if(is_visted(_vertex,visited)){
        return;
    }
    printf("%d ",_vertex->data);
    mark_visited(_vertex,visited);
    edge *_edge = _vertex->edge_list;
    for(;_edge;_edge=_edge->next){
        traverse_adjacent_edge_dfs(_edge->to_vertex,visited);
    }
}

void graph_traversal_DFS(graph *_graph){
    int *visited = (int*)calloc(_graph->vertex_count,sizeof(int));
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        traverse_adjacent_edge_dfs(_graph->vertex_list[i],visited);
    }
    printf("\n");
}

/*
Traverses a connected component using BFS.
*/
void traverse_adjacent_edge_bfs(vertex *_vertex, int *visited){
    if(is_visted(_vertex,visited)){
        return;
    }
    queue *que = init_queue(20);
    insert_queue(que,_vertex);
    visited[_vertex->data] = 1;
    while(!is_empty(que)){
        vertex *temp = delete_queue(que);
        printf("%d ",temp->data);
        edge *_edge = temp->edge_list;
        for(;_edge;_edge=_edge->next){
            if(visited[_edge->data]==0){
                insert_queue(que,_edge->to_vertex);
                visited[_edge->to_vertex->data] = 1;
            }
        }
    }
}

void graph_traversal_BFS(graph *_graph){
    int *visited = (int*)calloc(_graph->vertex_count,sizeof(int));
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        traverse_adjacent_edge_bfs(_graph->vertex_list[i],visited);
    }
    printf("\n");
}

int main(){
    int graph_mat[50][50] = { {0,1,1,1,1,1},
                              {0,0,1,1,0,0},
                              {1,0,0,0,0,0},
                              {0,0,0,1,0,0},
                              {0,0,0,0,0,1},
                              {0,0,0,0,1,0}
                            };
    int vertex_count = 6;

    graph *_graph = init_graph(graph_mat,vertex_count);
    print_graph(_graph);

    printf("DFS => ");
    graph_traversal_DFS(_graph);
    printf("BFS => ");
    graph_traversal_BFS(_graph);

    return 0;
}