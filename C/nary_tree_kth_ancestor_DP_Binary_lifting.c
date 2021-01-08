// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
// https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/
// https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree-set-2/
/*
You are given a tree with n nodes numbered from 0 to n-1 in the form of a
 parent array where parent[i] is the parent of node i.

The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th
 ancestor of the given node. If there is no such ancestor, return -1.

Note - The k-th ancestor of a tree node is the k-th node in the path
       from that node to the root.

Example:

                    0
                  /   \
                1       2
               / \     / \
              3   4   5   6

Input:
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

Output:
[null,1,0,-1]

Explanation:
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
 

Constraints:
1 <= k <= n <= 5*10^4
parent[0] == -1 indicating that 0 is the root node.
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5*10^4 queries.
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <math.h>

// Used the technique for binary lifting

void printArr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print2D(int **ip, int row, int col){
    int i = 0;
    for(;i<row;i++){
        printArr(ip[i],col);
    }
}

typedef struct {
    int node_count;
    int *parent;
    int parentSize;
    int **ancestor;
} TreeAncestor;

int* init_arr(int size){
    int *ip = (int*)calloc(size, sizeof(int));
    return ip;
}

int** get_ancestors(TreeAncestor *tree){
    int **ancestor = (int**)calloc(tree->node_count, sizeof(int*));
    // Adding 1 because we need to store data for that size also.
    // Eg. if log2(50000) = 15 then we need size = 16 to store the data for 15.
    int size = log2(tree->node_count) + 1;
    int i = 0;
    for(;i<tree->node_count;i++){
        ancestor[i] = init_arr(size);
        int j = 0;
        for(;j<size;j++){
            if(j==0) ancestor[i][j] = tree->parent[i];
            else if(i==0) ancestor[i][j] = -1;
            else{
                int temp = ancestor[i][j-1];
                if(temp==-1) ancestor[i][j] = -1;
                else ancestor[i][j] = ancestor[temp][j-1];
            }
        }
    }
    // print2D(ancestor, tree->node_count, size);
    return ancestor;
}

TreeAncestor* treeAncestorCreate(int n, int* parent, int parentSize) {
    TreeAncestor *tree = (TreeAncestor*)malloc(sizeof(TreeAncestor));
    if(tree){
        tree->node_count = n;
        tree->parent = parent;
        tree->parentSize = parentSize;
        tree->ancestor = get_ancestors(tree);
    }
    return tree;
}

    
int treeAncestorGetKthAncestor(TreeAncestor* obj, int node, int k) {
    if(node==-1) return -1;
    if(k==0) return node;
    int j = log2(k);
    int n = pow(2, j);
    return treeAncestorGetKthAncestor(obj, obj->ancestor[node][j], k-n);
}

void treeAncestorFree(TreeAncestor* obj) {
    
}

/**
 * Your TreeAncestor struct will be instantiated and called as such:
 * TreeAncestor* obj = treeAncestorCreate(n, parent, parentSize);
 * int param_1 = treeAncestorGetKthAncestor(obj, node, k);
 
 * treeAncestorFree(obj);
*/