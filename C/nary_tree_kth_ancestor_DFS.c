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

// Note - Below DFS approch won't work when tree has 50000 nodes.
// See nary_tree_kth_ancestor_DP_Binary_lifting.c for a better sol.

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct child_node_holder child_node;

typedef struct node {
     int data;
     child_node *childs;
} TreeAncestor;

typedef struct child_node_holder{
    TreeAncestor *child;
    struct child_node_holder *next;
}child_node;

child_node* init_child_node_holder(TreeAncestor *child){
    child_node *node = (child_node*)malloc(sizeof(child_node));
    if(node){
        node->child = child;
        node->next = node;
    }
    return node;
}

TreeAncestor* init_tree_node(int data){
    TreeAncestor *node = (TreeAncestor*)malloc(sizeof(TreeAncestor));
    if(node){
        node->data = data;
        node->childs = NULL;
    }
    return node;
}

void add_child(TreeAncestor *root, TreeAncestor *child){
    if(root->childs==NULL){
        root->childs = init_child_node_holder(child);
    }else{
        child_node *child_holder = init_child_node_holder(child);
        child_holder->next = root->childs->next;
        root->childs->next = child_holder;
        root->childs = child_holder;
    }
}

TreeAncestor* treeAncestorCreate(int n, int* parent, int parentSize) {
    TreeAncestor **tree = (TreeAncestor**)calloc(n, sizeof(TreeAncestor*));
    int i = 0;
    for(;i<parentSize;i++){
        TreeAncestor *node = init_tree_node(i);
        tree[i] = node;
        if(parent[i]!=-1){
            add_child(tree[parent[i]], node);
            // printf("child=%d parent=%d  <>",node->data, parent[i]);
        }
    }
    return tree[0];
}

void print_tree(TreeAncestor *root){
    if(root==NULL) return;
    printf("%d ",root->data);
    child_node *last = root->childs;
    if(last==NULL){
        printf("NULL ");
        return;
    }
    child_node *temp = last->next;
    while(temp!=last){
        print_tree(temp->child);
        temp = temp->next;
    }
    print_tree(temp->child);
}

int find_kth_ancestor(TreeAncestor *root, int node, int k, int *s, int *op){
    if(root==NULL) return k;
    // printf("root=%d op=%d k=%d s=%d\n",root->data,*op,k,*s);
    if(root->data==node){
        *s = 1;
        if(k==0){
            *op = root->data;
        }
        return k-1;
    }
    child_node *last = root->childs;
    if(last==NULL) return k;
    child_node *temp = last->next;
    while(temp!=last){
        // printf("-child - node=%d\n",temp->child->data);
        int dist = find_kth_ancestor(temp->child, node, k, s, op);
        // printf("Dist = %d\n",dist);
        if(*s==1){
            if(dist==0){
                *op = root->data;
            }
            return dist-1;
        }
        temp = temp->next;
    }
    if(temp==last){
        // printf("child - node=%d\n",temp->child->data);
        int dist = find_kth_ancestor(temp->child, node, k, s, op);
        // printf("Dist = %d\n",dist);
        if(*s==1){
            if(dist==0){
                *op = root->data;
            }
            return dist-1;
        }
    }
    return k;
}
    
int treeAncestorGetKthAncestor(TreeAncestor* obj, int node, int k) {
    // print_tree(obj);
    int s = 0;
    int op = -1;
    find_kth_ancestor(obj, node, k, &s, &op);
    return op;
}

void treeAncestorFree(TreeAncestor* obj) {
    
}

/**
 * Your TreeAncestor struct will be instantiated and called as such:
 * TreeAncestor* obj = treeAncestorCreate(n, parent, parentSize);
 * int param_1 = treeAncestorGetKthAncestor(obj, node, k);
 
 * treeAncestorFree(obj);
*/