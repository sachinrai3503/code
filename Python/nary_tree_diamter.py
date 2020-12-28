# https://www.geeksforgeeks.org/diameter-n-ary-tree/
# https://www.interviewbit.com/problems/largest-distance-between-nodes-of-a-tree/
"""
Problem Description

Given an arbitrary unweighted rooted tree which consists of N nodes.

The goal of the problem is to find largest distance between two nodes in a tree.

Distance between two nodes is a number of edges on a path between the nodes 
 (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i 
 (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be 
 root node.

Problem Constraints
1 <= N <= 40000

Input Format
 First and only argument is an integer array A of size N.

Output Format
 Return a single integer denoting the largest distance between two nodes
 in a tree.

Example Input
Input 1:

 A = [-1, 0, 0, 0, 3]

Example Output
Output 1: 3

Example Explanation
Explanation 1:

 node 0 is the root and the whole tree looks like this: 
          0
       /  |  \
      1   2   3
               \
                4

 One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, 
 thus the answer is 3.

"""

def get_max(a, b):
    return a if a>b else b

def get_max1_2(max1, max2, val):
    if val<max2:
         return max1, max2
    elif val>max1:
        return val, max1
    else:
        return max1, val

class Solution:
    
    def get_tree(self, A):
        tree_map = dict()
        for i in range(len(A)):
            childs = tree_map.get(A[i], None)
            if not childs:
                childs = list()
                tree_map[A[i]] = childs
            childs.append(i)
        return tree_map
        
    def max_path_len(self, tree_map, root_key, path_len):
        if root_key==None: return -1
        childs = tree_map.get(root_key, None)
        if not childs:
            path_len[0] = get_max(path_len[0], 1)
            return 1
        max1, max2 = 0, 0
        for child in childs:
            height = self.max_path_len(tree_map, child, path_len)
            max1, max2 = get_max1_2(max1, max2, height)
        path_len[0] = get_max(path_len[0], max1 + max2 + 1)
        return get_max(max1, max2) + 1
            
    
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # print(A)
        tree = self.get_tree(A)
        # print('Tree',tree)
        path_len = [0]
        root_key = tree.get(-1, None)
        self.max_path_len(tree, root_key[0], path_len)
        # print('path>',path_len)
        return path_len[0] - 1
    
def main():
    sol = Solution()
    diameter = sol.solve([ -1, 0, 0, 0, 3 ])
    print('Diameter>',diameter)

if __name__ == '__main__':
    main()
