// https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
// https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph-using-bfs/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include "graph_util.h"

/*
Checks if the graph component has cycle.
*/
int has_cycle_dfs(vertex *current_vertex, int *visited, int *rec_stack_hash){
    if(is_visted(current_vertex,visited) && rec_stack_hash[current_vertex->data]==1){
        return 1;
    }else if(is_visted(current_vertex,visited)){
        return 0;
    }
    mark_visited(current_vertex,visited);
    rec_stack_hash[current_vertex->data] = 1;
    edge *_edge = current_vertex->edge_list;
    for(;_edge;_edge=_edge->next){
        int cycle_flag = has_cycle_dfs(_edge->to_vertex,visited,rec_stack_hash);
        if(cycle_flag) return 1;
    }
    rec_stack_hash[current_vertex->data] = 0;
    return 0;
}

/*
Checks cycle in each connected component.
*/
int check_cycle_DFS(graph *_graph){
    int *visted = (int*)calloc(_graph->vertex_count,sizeof(int));
    int *rec_stack_hash = (int*)calloc(_graph->vertex_count,sizeof(int));
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        if(!is_visted(_graph->vertex_list[i],visted)){
            int cycle_flag = has_cycle_dfs(_graph->vertex_list[i],visted,rec_stack_hash);
            if(cycle_flag) return 1;
        }
    }
    return 0;
}

/*
Computes no. of incoming edges for each of the vertex in the graph.
*/
int* get_in_degree(graph *_graph){
    int *in_degree = (int*)calloc(_graph->vertex_count,sizeof(int));
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        edge *_edge = _graph->vertex_list[i]->edge_list;
        for(;_edge;_edge=_edge->next){
            in_degree[_edge->to_vertex->data]++;
        }
    }
    return in_degree;
}

int check_cycle_BFS(graph *_graph){
    int *in_degree = get_in_degree(_graph);
    queue *que = init_queue(_graph->vertex_count);
    int visited_vertex_count = 0;
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        if(in_degree[i]==0){
            insert_queue(que,_graph->vertex_list[i]);
        }
    }
    while(!is_empty(que)){
        vertex *temp = delete_queue(que);
        visited_vertex_count++;
        edge *_edge = temp->edge_list;
        for(;_edge;_edge=_edge->next){
            in_degree[_edge->to_vertex->data]--;
            if(in_degree[_edge->to_vertex->data]==0){
                insert_queue(que,_edge->to_vertex);
            }
        }
    }
    if(visited_vertex_count==_graph->vertex_count) return 0;
    return 1;
}

int main(){
    int graph_mat[50][50] = {{0,1,0,1,0},
                             {0,0,1,0,0},
                             {0,0,0,1,1},
                             {0,0,0,0,0},
                             {0,0,0,0,0}
                            };
    int vertex_count = 5;

    graph *_graph = init_graph(graph_mat,vertex_count);
    print_graph(_graph);

    printf("Is cycle present(DFS) = %d\n",check_cycle_DFS(_graph));
    printf("Is cycle present(BFS) = %d\n",check_cycle_BFS(_graph));

    return 0;
}