// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// https://www.geeksforgeeks.org/lca-in-a-tree-using-binary-lifting-technique/
/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
 in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
 is defined between two nodes p and q as the lowest node in T that has both
 p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,INT_MIN,INT_MIN,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,INT_MIN,INT_MIN,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
 of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
*/

#include <stdio.h>
#include <malloc.h>
#include <math.h>
#include <limits.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_2D(int **ip, int row, int col){
    int i = 0;
    for(;i<row;i++){
        print_arr(ip[i],col);
    }
}

int** init_2D_arr(int row, int col){
    int **arr = (int**)calloc(row, sizeof(int*));
    int i = 0;
    for(;i<row;i++){
        arr[i] = (int*)malloc(col*sizeof(int));
    }
    return arr;
}

void set_ancestors(int *tree, int node_count, int **ancestors, int col, 
                   int *level, int index, int parent_index, int cur_level){
    if(index>=node_count) return;
    if(tree[index]==INT_MIN) return;
    level[index] = cur_level;
    ancestors[index][0] = parent_index;
    int i = 1;
    for(;i<col;i++){
        int temp = ancestors[index][i-1];
        if(temp==-1) ancestors[index][i] = -1;
        else ancestors[index][i] = ancestors[temp][i-1];
    }
    set_ancestors(tree, node_count, ancestors, col, level, index*2+1, index,
                  cur_level+1);
    set_ancestors(tree, node_count, ancestors, col, level, index*2+2, index,
                  cur_level+1);
}

int get_kth_ancestor(int **ancestors, int node_count, int col, int node_index,
                     int k){
    while(node_index!=-1 && k>0){
        int j = log2(k);
        int n = pow(2, j);
        node_index = ancestors[node_index][j];
        k = k-n;
    }
    return node_index;
}

int find_lca(int **ancestor, int node_count, int col, int *level, int p, int q){
    // Getting the nodes at same level.
    if(level[p]>level[q]){
        p = get_kth_ancestor(ancestor, node_count, col, p, level[p]-level[q]);
    }else if(level[q]>level[p]){
        q = get_kth_ancestor(ancestor, node_count, col, q, level[q]-level[p]);
    }
    if(p==q) return p;
    // Getting this level as it is must that root will be the common ancestor, 
    // if no other nodes are common ancestor to p & q.
    int common_level = level[q];
    // Also, anything above the 2^i will definetly be a common ancestor, so will 
    // search with decreasing i values.
    // See this - https://www.youtube.com/watch?v=02zM-QoKoPg
    int i = log2(common_level);
    for(;i>=0;i--){
        if(ancestor[p][i]!=ancestor[q][i]){
            p = ancestor[p][i];
            q = ancestor[q][i];
        }
    }
    return ancestor[p][0];
}

int main(){
    int tree[] = {20,8,22,4,12,INT_MIN,INT_MIN,INT_MIN,INT_MIN,10,14};
    // Note - Below are index of the tree elements
    int p = 10;
    int q = 2;
    int node_count = sizeof(tree)/sizeof(tree[0]);
    print_arr(tree, node_count);
    int col = log2(node_count) + 1;
    int **ancestors = init_2D_arr(node_count, col);
    int *level = (int*)malloc(sizeof(int)*node_count);
    set_ancestors(tree, node_count, ancestors, col, level, 0, -1, 0);
    print_2D(ancestors, node_count, col);
    print_arr(level, node_count);
    int lca_index = find_lca(ancestors, node_count, col, level, p, q);
    if(lca_index==-1){
        printf("No lca found for %d and %d\n",p,q);
    }else{
        printf("LCA = %d\n",tree[lca_index]);
    }
    return 0;
}