// https://www.geeksforgeeks.org/find-all-possible-trees-with-given-inorder-traversal/
/*
Given an array that represents Inorder Traversal, find all possible Binary Trees with the given Inorder traversal and print their preorder traversals.

Examples:

Input:   in[] = {3, 2};
Output:  Preorder traversals of different possible Binary Trees are:
         3 2
         2 3
Below are different possible binary trees
    3        2
     \      /
      2    3

Input:   in[] = {4, 5, 7};
Output:  Preorder traversals of different possible Binary Trees are:
          4 5 7 
          4 7 5 
          5 4 7 
          7 4 5 
          7 5 4 
Below are different possible binary trees
  4         4           5         7       7
   \          \       /   \      /       /
    5          7     4     7    4       5
     \        /                  \     /
      7      5                    5   4 
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct List1{
      int data;
      struct List1 *next;
}list1;

list1* init_list1_node(int data){
      list1 *node = (list1*)malloc(sizeof(list1));
      if(node){
            node->data = data;
            node->next = node;
      }
      return node;
}

list1* add_to_list1(list1 *last1, list1 *last2){
      if(!last2) return last1;
      if(!last1) return last2;
      list1 *t_first = last1->next;
      last1->next = last2->next;
      last2->next = t_first;
      return last2;
}

list1* clone_list1(list1 *last){
      if(!last) return NULL;
      list1 *new_list = NULL;
      list1 *first = last->next;
      for(;first!=last;first=first->next){
            new_list = add_to_list1(new_list, init_list1_node(first->data));
      }
      new_list = add_to_list1(new_list, init_list1_node(first->data));
      return new_list;
}

void print_list1(list1 *last){
      if(!last) return;
      list1 *first = last->next;
      for(;first!=last;first=first->next){
            printf("%d ", first->data);
      }
      printf("%d\n", first->data);
}

typedef struct List2{
      list1 *last;
      struct List2 *next;
}list2;

list2* init_list2_node(list1 *last){
      list2 *node = (list2*)malloc(sizeof(list2));
      if(node){
            node->last = last;
            node->next = node;
      }
      return node;
}

list2* add_to_list2(list2 *last1, list2 *last2){
      if(!last1) return last2;
      if(!last2) return last1;
      list2 *t_first = last1->next;
      last1->next = last2->next;
      last2->next = t_first;
      return last2;
}

void print_list2(list2 *last){
      if(!last) return;
      list2 *first = last->next;
      for(;first!=last;first=first->next){
            print_list1(first->last);
      }
      print_list1(first->last);
}

list2* combine(int root, list2 *left_last, list2 *right_last){
      list2 *last = NULL;
      if(!left_last && !right_last){
            last = add_to_list2(last, init_list2_node(init_list1_node(root)));
      }else if(right_last==NULL){
            list2 *first = left_last->next;
            for(;first!=left_last;first=first->next){
                  list2 *t_list = init_list2_node(add_to_list1(init_list1_node(root),first->last));
                  last = add_to_list2(last, t_list);
            }
            list2 *t_list = init_list2_node(add_to_list1(init_list1_node(root),first->last));
            last = add_to_list2(last, t_list);
      }else if(left_last==NULL){
            list2 *first = right_last->next;
            for(;first!=right_last;first=first->next){
                  list2 *t_list = init_list2_node(add_to_list1(init_list1_node(root),first->last));
                  last = add_to_list2(last, t_list);
            }
            list2 *t_list = init_list2_node(add_to_list1(init_list1_node(root),first->last));
            last = add_to_list2(last, t_list);
      }else{
            list2 *left_first = left_last->next;
            left_last->next = NULL;
            list2 *right_first = right_last->next;
            right_last->next = NULL;
            list2 *t_left = left_first;
            for(;t_left;t_left=t_left->next){
                  list2 *t_right = right_first;
                  for(;t_right;t_right=t_right->next){
                        list1 *t_list1 = add_to_list1(clone_list1(t_left->last),
                                                      clone_list1(t_right->last));
                        t_list1 = add_to_list1(init_list1_node(root), t_list1);
                        last = add_to_list2(last, init_list2_node(t_list1));
                  }
            }
      }
      return last;
}

list2* get_all_preorder_trees(int *ip, int s, int e){
      list2 *last = NULL;
      int i = s;
      for(;i<=e;i++){
            last = add_to_list2(last, 
                                combine(ip[i], 
                                        get_all_preorder_trees(ip,s,i-1),
                                        get_all_preorder_trees(ip,i+1,e)));
      }
      return last;
}

int main(){
      int ip[] = {1,2,3,4,5,6,7};
      int length = sizeof(ip)/sizeof(ip[0]);

      list2 *last = get_all_preorder_trees(ip,0,length-1);
      print_list2(last);

      return 0;
}