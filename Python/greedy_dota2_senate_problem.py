# https://leetcode.com/problems/dota2-senate
"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants
 to decide on a change in the Dota2 game. The voting for this change is a round-based
 procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in 
 this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to 
 vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character
 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n 
  senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the
 given order. This procedure will last until the end of voting. All the senators who
 have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party.
 Predict which party will finally announce the victory and change the Dota2 game. 
 The output should be "Radiant" or "Dire".

Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:
Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Constraints:
n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.
"""

class Solution:

    def count_member(self, s, s_len):
        r_count, d_count = 0, 0
        for char in s:
            if char=='R': r_count+=1
            else: d_count+=1
        return r_count, d_count

    def predictPartyVictory(self, senate: str) -> str:
        senate_len = len(senate)
        senate_list = list(senate)
        r_count, d_count = self.count_member(senate, senate_len)
        r_blocked_count, d_blocked_count = 0, 0
        r_to_block_count, d_to_block_count = 0, 0
        while True:
            for i in range(senate_len):
                if senate_list[i]=='N': continue
                if senate_list[i]=='R':
                    if r_to_block_count>0:
                        senate_list[i] = 'N'
                        r_blocked_count+=1
                        r_to_block_count-=1
                    else:
                        d_to_block_count+=1
                else:
                    if d_to_block_count>0:
                        senate_list[i] = 'N'
                        d_blocked_count+=1
                        d_to_block_count-=1
                    else:
                        r_to_block_count+=1
                if (d_blocked_count+d_to_block_count)>=d_count: return 'Radiant'
                if (r_blocked_count+r_to_block_count)>=r_count: return 'Dire'
            # print(f'{senate_list=}')
        return None