# https://leetcode.com/problems/combination-sum/
# https://www.geeksforgeeks.org/combinational-sum/
"""
Given an array of distinct integers candidates and a target integer target, 
 return a list of all unique combinations of candidates where the chosen numbers
 sum to target. 

You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen 
 numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is
 less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note: 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]
 
Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""

def append(op_list, index, value):
    if op_list[index] == None:
        op_list[index] = list()
    op_list[index].append(value)

class Solution:
    
    def get_all_subset(self, op, subset, target, item_list):
        if target==0:
            # print(item_list)
            item_tuple = tuple(sorted(item_list))
            subset.add(item_tuple)
            return
        if not op[target]: return
        for item in op[target]:
            item_list.append(target-item)
            self.get_all_subset(op, subset, item, item_list)
            item_list.pop()
    
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        subset = set()
        op = [None]*(target+1)
        for i in range(len(candidates)-1,-1,-1):
            candidate = candidates[i]
            for j in range(candidate, target+1):
                if j==candidate: append(op, j, 0)
                elif op[j-candidate]: append(op, j, j-candidate)
        for item in op:
            if item: item.sort(reverse=True)
        # print(op)
        self.get_all_subset(op, subset, target, list())
        return subset
        