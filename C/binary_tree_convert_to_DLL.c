// https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
// https://www.geeksforgeeks.org/convert-a-given-binary-tree-to-doubly-linked-list-set-2/
// https://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/
/*
Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). 
The left and right pointers in nodes are to be used as previous and next
 pointers respectively in converted DLL. 
 
The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
The first node of Inorder traversal (left most node in BT) must be
 head node of the DLL.
*/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }   
    return node;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return make_node(data);
    else if(root->data>data) root->left = make_tree(root->left,data);
    else if(root->data<data) root->right = make_tree(root->right,data);
    return root;
}

void pre(tree_node *root){
    if(root){
        printf("%d ",root->data);
        pre(root->left);
        pre(root->right);
    }
}

void print_list(tree_node *head){
    for(;head;head=head->right){
        printf("%d ",head->data);
    }
    printf("\n");
}

tree_node* join(tree_node *list1_last, tree_node *list2_last){
     if(list1_last==NULL) return list2_last;
     if(list2_last==NULL) return list1_last;
     tree_node *head2 = list2_last->right;
     list2_last->right = list1_last->right;
     list1_last->right = head2;
     head2->left = list1_last;
     return list2_last;
}

tree_node* to_DLL(tree_node *root){
    if(root==NULL) return NULL;
    tree_node *left_last = to_DLL(root->left);
    tree_node *right_last = to_DLL(root->right);
    root->left = root->right = NULL;
    root->right = root;
    return (join(join(left_last,root),right_last));
}

tree_node* convert_tree_to_DLL(tree_node *root){
    tree_node *last = to_DLL(root);
    if(!last) return last;
    tree_node *first = last->right;
    last->right = NULL;
    return first;
}

int main(){
    int ip[] = {100,80,50,10,70,60,75,72,82,90,85,150,200,202,175,170};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int  i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");

    tree_node *head = convert_tree_to_DLL(root);
    print_list(head);

    return 0;
}

// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
/*
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer
 points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
*/

//  Definition for a binary tree node.
 typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 }treeNode;

treeNode* flattenTree(treeNode *root){
    if(root==NULL) return NULL;
    treeNode *left = flattenTree(root->left);
    treeNode *right = flattenTree(root->right);
    root->left = root->right = NULL;
    root->right = root;
    treeNode *last = root;
    if(left){
        last->right = left->right;
        left->right = root;
        last = left;
    }
    if(right){
        last->right = right->right;
        right->right = root;
        last = right;
    }
    return last;
}

void flatten(struct TreeNode* root){
    treeNode *last = flattenTree(root);
    if(last) last->right = NULL;
}