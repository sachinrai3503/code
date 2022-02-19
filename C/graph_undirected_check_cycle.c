// https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
// https://www.geeksforgeeks.org/detect-cycle-in-an-undirected-graph-using-bfs/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include "graph_util.h"

/*
Checks cycle in connected component using DFS.
*/
int has_cycle_dfs(vertex *current_vertex, vertex *parent_vertex, int *visited){
    if(is_visted(current_vertex,visited)){
        return 1;
    }
    mark_visited(current_vertex,visited);
    edge *_edge = current_vertex->edge_list;
    for(;_edge;_edge=_edge->next){
        if(is_visted(_edge->to_vertex,visited)==0){
            int cycle_flag = has_cycle_dfs(_edge->to_vertex,current_vertex,visited);
            if(cycle_flag) return 1;
        }else if(_edge->to_vertex!=parent_vertex){
            return 1;
        }
    }
    return 0;
}

/*
Checks cycle in each connected component.
*/
int check_cycle_DFS(graph *_graph){
    int *visted = (int*)calloc(_graph->vertex_count,sizeof(int));
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        if(!is_visted(_graph->vertex_list[i],visted)){
            int cycle_flag = has_cycle_dfs(_graph->vertex_list[i],NULL,visted);
            if(cycle_flag) return 1;
        }
    }
    return 0;
}

/*
Check cycle in connected component using BFS.
*/
int has_cycle_bfs(vertex *current_vertex, int *visited){
    if(is_visted(current_vertex,visited)){
        return 1;
    }
    queue *que = init_queue(20);
    vertex *null_vertex = init_vertex(INT_MIN,NULL);
    vertex *parent_vertex = init_vertex(INT_MAX,NULL);
    insert_queue(que,parent_vertex);
    insert_queue(que,current_vertex);
    mark_visited(current_vertex,visited);
    insert_queue(que,null_vertex);
    while(!is_empty(que) && que->data[que->front]!=null_vertex){
        parent_vertex = delete_queue(que);
        while(!is_empty(que) && que->data[que->front]!=null_vertex){
            vertex *temp = delete_queue(que);
            insert_queue(que,temp); // Inserting as parent
            edge *_edge = temp->edge_list;
            for(;_edge;_edge=_edge->next){
                if(is_visted(_edge->to_vertex,visited)==0){
                    mark_visited(_edge->to_vertex,visited);
                    insert_queue(que,_edge->to_vertex);
                }else if(_edge->to_vertex!=parent_vertex){
                    return 1;
                }
            }
            insert_queue(que,null_vertex);
        }
        if(!is_empty(que))
            delete_queue(que);
    }
    return 0;
}

/*
Checks cycle in each connected component.
*/
int check_cycle_BFS(graph *_graph){
    int *visted = (int*)calloc(_graph->vertex_count,sizeof(int));
    int i = 0;
    for(;i<_graph->vertex_count;i++){
        if(!is_visted(_graph->vertex_list[i],visted)){
            int cycle_flag = has_cycle_bfs(_graph->vertex_list[i],visted);
            if(cycle_flag) return 1;
        }
    }
    return 0;
}

int main(){
    int graph_mat[50][50] ={{0,1,0,0,0,0,0,0,0},
                            {1,0,1,0,0,0,0,0,0},
                            {0,1,0,1,0,0,0,0,0},
                            {0,0,1,0,1,0,0,0,1},
                            {0,0,0,1,0,1,0,0,0},
                            {0,0,0,0,1,0,1,0,0},
                            {0,0,0,0,0,1,0,0,0},
                            {0,0,0,0,0,0,0,0,1},
                            {0,0,0,1,0,0,0,1,1}
                            };
    int vertex_count = 9;

    graph *_graph = init_graph(graph_mat,vertex_count);
    print_graph(_graph);

    printf("Is cycle present(DFS) = %d\n",check_cycle_DFS(_graph));
    printf("Is cycle present(BFS) = %d\n",check_cycle_BFS(_graph));

    return 0;
}