// https://www.dailycodingproblem.com/blog/lockable-binary-trees/
// https://www.geeksforgeeks.org/locking-and-unlocking-of-resources-in-the-form-of-n-ary-tree/

/*
Given an binary tree of resources arranged hierarchically such that height of 
tree is O(Log N) where N is total number of nodes (or resources). 

A process needs to lock a resource node in order to use it. But a node can't 
be locked if any of its descendant or ancestor is locked.

Following operations are required for a given resource node:

islock()- returns true if a given node is locked and false if it is not. 
          A node is locked if lock() has successfully executed for the node.
Lock()- locks the given node if possible and updates lock information. 
        Lock is possible only if ancestors and descendants of current node are not locked.
unLock()- unlocks the node and updates information.

How design resource nodes and implement above operations such that following
 time complexities are achieved.

    islock()  O(1)
    Lock()    O(log N)
    unLock()  O(log N)
*/

// NOTE - In below sol. assuming the tree constructed is balanced for simplicity.
//        Can use AVL tree for balancing.

// Note - If we check for all the decendants before locking then time complexity
//   will be O(n) where n is nodes count. This can occur with root node.

#include <stdio.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *left, *right;
    int is_locked;
    int no_of_child_locked;
    struct node *parent;
}tree_node;

tree_node* make_tree_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
        node->is_locked = 0;
        node->no_of_child_locked = 0;
        node->parent = NULL;
    }
    return node;
}

tree_node* make_tree(tree_node *root, tree_node *parent, int data){
    if(root==NULL){
        tree_node *node = make_tree_node(data);
        node->parent = parent;
        return node;
    }
    if(root->data>data) root->left = make_tree(root->left, root, data);
    else if(root->data<data) root->right = make_tree(root->right, root, data);
    return root;
}

void pre(tree_node *root){
    if(root){
        printf("%d:%d:%d - ",root->data,root->is_locked,root->no_of_child_locked);
        pre(root->left);
        pre(root->right);
    }
}

tree_node* get_node(tree_node *root, int data){
    while(root){
        if(root->data==data) return root;
        else if(root->data>data) root = root->left;
        else if(root->data<data) root = root->right;
    }
    return NULL;
}

int is_locked(tree_node *node){
    if(node && node->is_locked) return 1;
    return 0;
}

int unlock(tree_node *node){
    if(!node || !is_locked(node)) return 0;
    tree_node *parent = node->parent;
    while(parent){
        parent->no_of_child_locked--;
        parent = parent->parent;
    }
    node->is_locked = 0;
    return 1;
}

int lock(tree_node *node){
    if(!node || is_locked(node)) return 0;
    if(node->no_of_child_locked!=0) return 0;
    tree_node *parent = node->parent;
    while(parent){
        if(is_locked(parent)) return 0;
        parent = parent->parent;
    }
    parent = node->parent;
    while(parent){
        parent->no_of_child_locked++;
        parent = parent->parent;
    }
    node->is_locked = 1;
    return 1;
}

int main(){

    int ip[] = {100,50,40,30,35,60,55,59,58,57,120,125,122,130,126,128,127,129};
    int to_lock[] = {59,60,50,40,35,126,122,125,129};
    int to_unlock[] = {100,50,35,122};
    
    int ip_len = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<ip_len;i++){
        root = make_tree(root, NULL, ip[i]);
    }
    pre(root);
    printf("\n*************************************\n");

    int lock_len = sizeof(to_lock)/sizeof(to_lock[0]);
    int unlock_len = sizeof(to_unlock)/sizeof(to_unlock[0]);

    for(i=0;i<lock_len;i++){
        printf("Locking %d >>",to_lock[i]);
        printf("is locked = %d\n",lock(get_node(root,to_lock[i])));
    }
    pre(root);
    printf("\n");

    for(i=0;i<unlock_len;i++){
        printf("Unlocking %d >>",to_unlock[i]);
        printf("is unlocked = %d\n",unlock(get_node(root,to_unlock[i])));
    }
    pre(root);

    return 0;
}