// https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
/*
Find the distance between two keys in a binary tree, no parent pointers are given.
 Distance between two nodes is the minimum number of edges to be traversed 
 to reach one node from other.
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_tree_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return make_tree_node(data);
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

int find_given_child_dist(tree_node *node, int cur_dist, int data){
    if(node==NULL) return -1;
    if(node->data == data) return cur_dist;
    int left = find_given_child_dist(node->left,cur_dist+1,data);
    if(left!=-1) return left;
    return find_given_child_dist(node->right,cur_dist+1,data);
}

int find_dist_bet_2_node(tree_node *root, int data1, int data2, int *to_find,
    int *found_flag){
    if(root==NULL) return INT_MAX;
    if(root->data==data1 || root->data==data2){
        *found_flag = 1;
        if(root->data==data1) *to_find = data2;
        else *to_find = data1;
        int dist = find_given_child_dist(root,0,*to_find);
        if(dist!=-1){
            *found_flag = 2;
            return dist;
        }return 1;
    }
    int left = find_dist_bet_2_node(root->left,data1,data2,to_find,found_flag);
    if(*found_flag==2) return left;
    if(*found_flag==1){
        int dist = find_given_child_dist(root->right,left+1,*to_find);
        if(dist==-1) return left+1;
        *found_flag = 2;
        return dist;
    }
    if(*found_flag==0){
        int right = find_dist_bet_2_node(root->right,data1,data2,to_find,
                found_flag);
        if(*found_flag==2) return right;
        if(*found_flag==1) return right+1;
        if(*found_flag==0) return INT_MAX;
    }
}

int main(){
    int ip[] = {10,5,1,8,15,13,12,17};
    int length = sizeof(ip)/sizeof(ip[0]);
    int data1 = 12;
    int data2 = 8;

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");
    printf("Data1 = %d Data2 = %d\n",data1,data2);

    int to_find = INT_MIN;
    int found_flag = 0;
    int dist = find_dist_bet_2_node(root,data1,data2,&to_find,&found_flag);
    if(found_flag==2) printf("Dist = %d\n",dist);
    else if(found_flag==1) printf("Not found %d\n",to_find);
    else printf("Didn't find any node\n");

    return 0;
}