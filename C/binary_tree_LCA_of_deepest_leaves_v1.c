// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
/*
Given the root of a binary tree, return the lowest common ancestor of its 
 deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth
 of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest
 depth such that every node in S is in the subtree with root A.

Note: This question is the same as 865: 
 https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, 
 but the depth of nodes 7 and 4 is 3.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, & it's the lca of itself.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
 
Constraints:
The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 1000
The values of the nodes in the tree are unique.
*/

// Note - Below sol. is not O(n) and also has mutiple traversal.
// Time complexity = 2^d * O(n) where d is the depth of deepest node.
// At depth d count of nodes is 2^d.
// See binary_tree_LCA_of_deepest_leaves_v2.c for O(n) & 1 traversal sol.

#include <stdio.h>

//  * Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode tree_node;

typedef struct SCL{
    tree_node *data;
    struct SCL *next;
}list_node;

list_node* init_list_node(tree_node *data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = node;
    }
    return node;
}

list_node* add_to_list(list_node *last, tree_node *data){
    list_node *node = init_list_node(data);
    if(last){
        node->next = last->next;
        last->next = node;
    }
    return node;
}

void free_list(list_node *last){
    if(last){
        list_node *first = last->next;
        last->next = NULL;
        free(first);
    }
}

void print_list(list_node *last){
    if(last){
        list_node *temp = last->next;
        for(;temp!=last;temp=temp->next){
            printf("%d ", temp->data->val);
        }
        printf("%d ", temp->data->val);
    }
    printf("\n");
}

void get_node_at_deepest_level(tree_node *root, int cur_level, int *max_level, 
                               list_node **last){
    if(root==NULL) return;
    if(cur_level>*max_level){
        free_list(*last);
        *max_level = cur_level;
        *last = add_to_list(NULL, root);
    }else if(cur_level==*max_level){
        *last = add_to_list(*last, root);
    }
    get_node_at_deepest_level(root->left, cur_level+1, max_level, last);
    get_node_at_deepest_level(root->right, cur_level+1, max_level, last);
}

int is_present_in_tree(tree_node *root, int data){
    if(root==NULL) return 0;
    if(root->val==data) return 1;
    return (is_present_in_tree(root->left, data) || 
           is_present_in_tree(root->right, data));
}

tree_node* get_LCA(tree_node *root, tree_node *p, tree_node *q, int *s,
                   tree_node **other){
    if(root==NULL) return NULL;
    if(root->val==p->val || root->val==q->val){
        *other = (root->val==p->val)?q:p;
        *s = 1;
        if(is_present_in_tree(root, (*other)->val)){
            *s = 2;
            return root;
        }
        return NULL;
    }
    tree_node *left = get_LCA(root->left, p, q, s, other);
    if(*s==2) return left;
    if(*s==1){
        if(is_present_in_tree(root, (*other)->val)){
            *s = 2;
            return root;
        }
        return NULL;
    }
    tree_node *right = get_LCA(root->right, p, q, s, other);
    if(*s==2) return right;
    if(*s==1){
        if(is_present_in_tree(root, (*other)->val)){
            *s = 2;
            return root;
        }
        return NULL;
    }
    return NULL;
}

tree_node* lowestCommonAncestor(tree_node* root, tree_node* p, tree_node* q) {
    int s = 0;
    tree_node *other = NULL;
    return get_LCA(root, p, q, &s, &other);
}

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root){
    tree_node *lca = NULL;
    if(root==NULL) return NULL;
    int level = -1;
    list_node *last = NULL;
    get_node_at_deepest_level(root, 0, &level, &last);
    // print_list(last);
    list_node *temp = last->next;
    last->next = NULL;
    lca = temp->data;
    temp = temp->next;
    for(;temp;temp=temp->next){
        lca = lowestCommonAncestor(root, lca, temp->data);
        if(lca==root) return lca;
    }
    return lca;
}