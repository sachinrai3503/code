// https://leetcode.com/problems/intersection-of-two-linked-lists
// https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists
/*
Given the heads of two singly linked-lists headA and headB, return the node at which the
 two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked
 structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there
 is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to
        the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to
        the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads,
 headA and headB to your program. If you correctly return the intersected node, then your
 solution will be accepted.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
 There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected
 node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
 There are 3 nodes before the intersected node in A; There are 1 node before the intersected
 node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 
Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
*/

#include <stdio.h>
#include <malloc.h>

//   Definition for singly-linked list.
  struct ListNode {
      int val;
      struct ListNode *next;
  };
 

typedef struct ListNode list_node;

list_node* make_cycle_and_get_length(list_node *head, int *length){
    list_node *t_head = head;
    list_node *prev = NULL;
    for(;head;head=head->next){
        (*length)+=1;
        prev = head;
    }
    if(prev) prev->next = t_head;
    return prev;
}

list_node* get_node_after_k_pos(list_node *head, int k){
    int i = 0;
    for(;i<k && head; i++, head=head->next);
    return head;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(!headA || !headB) return NULL;
    int lengthA = 0;
    list_node *last_node_A = make_cycle_and_get_length(headA, &lengthA);
    list_node *k_pos_node = get_node_after_k_pos(headB, lengthA); 
    while(k_pos_node && headB!=k_pos_node){
        headB = headB->next;
        k_pos_node = k_pos_node->next;
    }
    last_node_A->next = NULL;
    if(!k_pos_node) return NULL; // No intersection case
    return headB;
}