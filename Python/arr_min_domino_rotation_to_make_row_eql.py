# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row
"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile 
 with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 
Constraints:
2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""

from sys import maxsize
from typing import List

class Solution:

    def compare_map1to2(self, count_map1, count_map2, expected_count):
        for num, act_count in count_map1.items():
            if count_map2.get(num, 0)>=(expected_count-act_count):
                return expected_count-act_count
        return maxsize

    def minDominoRotations_1(self, tops: List[int], bottoms: List[int]) -> int:
        min_rotations = maxsize
        dice_count = len(tops)
        tops_count = dict()
        bottoms_count = dict()
        dice_with_same_top_bottom = dict()
        for i in range(dice_count):
            top, bottom = tops[i], bottoms[i]
            if top==bottom:
                count = dice_with_same_top_bottom.get(top, 0)
                dice_with_same_top_bottom[top] = count+1
                continue
            top_count = tops_count.get(top, 0)
            bottom_count = bottoms_count.get(bottom, 0)
            tops_count[top] = top_count+1
            bottoms_count[bottom] = bottom_count+1
        # print(f'{dice_count=} {tops_count=} {bottoms_count=} {dice_with_same_top_bottom=}')
        
        dice_count_with_same_top_bottom = len(dice_with_same_top_bottom)
        if dice_count_with_same_top_bottom>1: return -1
        elif dice_count_with_same_top_bottom==1:
            common_dice, common_dice_count = list(dice_with_same_top_bottom.items())[0]
            dice_count-=common_dice_count
            top_rotations = (dice_count-tops_count.get(common_dice, 0))
            bottom_rotations = (dice_count-bottoms_count.get(common_dice, 0))
            if bottoms_count.get(common_dice, 0)>=top_rotations: min_rotations = min(min_rotations, top_rotations)
            if tops_count.get(common_dice, 0)>=bottom_rotations: min_rotations = min(min_rotations, bottom_rotations)
        else:
            top_rotations = self.compare_map1to2(tops_count, bottoms_count, dice_count)
            min_rotations = min(min_rotations, top_rotations)
            bottom_rotations = self.compare_map1to2(bottoms_count, tops_count, dice_count)
            min_rotations = min(min_rotations, bottom_rotations)
        return min_rotations if min_rotations!=maxsize else -1
    
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dice_count = len(tops)
        for i in range(1,7):
            common_i = True
            i_top_count, i_bottom_count = 0, 0
            for j in range(dice_count):
                if tops[j]!=i and bottoms[j]!=i:
                    common_i = False
                    break
                if tops[j]==i:
                    i_top_count+=1
                if bottoms[j]==i:
                    i_bottom_count+=1
            if common_i: # no other i will be possible
                return dice_count - max(i_top_count, i_bottom_count)
        return -1