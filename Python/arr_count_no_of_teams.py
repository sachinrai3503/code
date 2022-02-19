# https://leetcode.com/problems/count-number-of-teams/
# https://www.geeksforgeeks.org/find-number-of-triplets-in-array-such-that-aiajak-and-ijk/
"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
    where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions.
    (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
"""

class BIT:
    def __init__(self, length):
        self.length = length
        self.data = [0 for i in range(length)]

    def query(self, index):
        count = 0
        while index>0:
            count+=self.data[index]
            index-=(index&-index)
        return count

    def update(self, index, value = 1):
        while index<self.length:
            self.data[index]+=value
            index+=(index&-index)    
        
class Solution:
    def numTeams(self, rating: list[int]) -> int:
        count = 0
        length = len(rating)
        greater_count = [[0 for j in range(length)] for i in range(2)]
        t_arr = [i for i in range(length, 0, -1)]
        t_arr.sort(key = lambda x :  rating[length-x])
        # print(rating)
        # print(t_arr)
        bit = BIT(length+1)
        for i in range(length-1, -1, -1):
            greater_count[0][i] = bit.query(t_arr[i])
            bit.update(t_arr[i])
            greater_count[1][i] = (length-1) - i - greater_count[0][i] 
        # print(greater_count)
        bit = BIT(length+1)
        for i in range(length):
            smaller_ele_count_to_right = bit.query(t_arr[i])
            bit.update(t_arr[i])
            smaller_ele_count_to_left = i - smaller_ele_count_to_right
            count+=((smaller_ele_count_to_left*greater_count[0][i])+
                    (smaller_ele_count_to_right*greater_count[1][i]))
        return count