# https://leetcode.com/problems/the-score-of-students-solving-math-expression
"""
You are given a string s that contains digits 0-9, addition symbols '+', and 
 multiplication symbols '*' only, representing a valid math expression of single 
 digit numbers (e.g., 3+5*2). This expression was given to n elementary school
 students. The students were instructed to get the answer of the expression by 
 following this order of operations:

- Compute multiplication, reading from left to right; Then,
- Compute addition, reading from left to right.

You are given an integer array answers of length n, which are the submitted 
 answers of the students in no particular order. You are asked to grade the 
 answers, by following these rules:

If an answer equals the correct answer of the expression, this student will be rewarded 5 points;
Otherwise, if the answer could be interpreted as if the student applied the 
 operators in the wrong order but had correct arithmetic, this student will be rewarded 2 points;
Otherwise, this student will be rewarded 0 points.

Return the sum of the points of the students.

Example 1:
Input: s = "7+3*1*2", answers = [20,13,42]
Output: 7
Explanation: As illustrated above, the correct answer of the expression is 13, therefore one student is rewarded 5 points: [20,13,42]
A student might have applied the operators in this wrong order: ((7+3)*1)*2 = 20. Therefore one student is rewarded 2 points: [20,13,42]
The points for the students are: [2,5,0]. The sum of the points is 2+5+0=7.

Example 2:
Input: s = "3+5*2", answers = [13,0,10,13,13,16,16]
Output: 19
Explanation: The correct answer of the expression is 13, therefore three students are rewarded 5 points each: [13,0,10,13,13,16,16]
A student might have applied the operators in this wrong order: ((3+5)*2 = 16. Therefore two students are rewarded 2 points: [13,0,10,13,13,16,16]
The points for the students are: [5,0,0,5,5,2,2]. The sum of the points is 5+0+0+5+5+2+2=19.

Example 3:
Input: s = "6+0*1", answers = [12,9,6,4,8,6]
Output: 10
Explanation: The correct answer of the expression is 6.
If a student had incorrectly done (6+0)*1, the answer would also be 6.
By the rules of grading, the students will still be rewarded 5 points (as they got the correct answer), not 2 points.
The points for the students are: [0,0,5,0,0,5]. The sum of the points is 10.

Constraints:
3 <= s.length <= 31
s represents a valid expression that contains only digits 0-9, '+', and '*' only.
All the integer operands in the expression are in the inclusive range [0, 9].
1 <= The count of all operators ('+' and '*') in the math expression <= 15
Test data are generated such that the correct answer of the expression is in the range of [0, 1000].
n == answers.length
1 <= n <= 104
0 <= answers[i] <= 1000
"""

# NOTE - Related to https://leetcode.com/problems/24-game

from functools import cache
from typing import List, Set

class Solution:

    def __init__(self):
        self.char_to_int = {chr(48+i):i for i in range(10)}

    def solve(self, a, b, oper):
        if oper=='+': return a+b
        if oper=='*': return a*b

    def get_correct_score(self, s, s_len):
        op1 = 0 # first * then +
        t_op1 = self.char_to_int[s[0]]
        i = 1
        while i<s_len:
            next_int = self.char_to_int[s[i+1]]
            if s[i]=='*':
                t_op1*=next_int # first * then +
            else:
                op1+=t_op1 # first * then +
                t_op1 = next_int
            i+=2
        op1+=t_op1
        # print(f'{op1=}')
        return op1

    @cache
    def get_all_possible_op(self, i, j) -> Set:
        # print(f'{i=} {j=}')
        if i>j: return None
        if i==j: return {self.char_to_int[self.s[i]],}
        op = set()
        for k in range(i+1, j, 2):
            left_possible_ops = self.get_all_possible_op(i, k-1)
            right_possible_ops = self.get_all_possible_op(k+1, j)
            if (0 in left_possible_ops or 0 in right_possible_ops) and self.s[k]=='*': # handle s="9+8*0", anss=[0]
                op.add(0)
            for left_possible_op in left_possible_ops:
                for right_possible_op in right_possible_ops:
                    ans = self.solve(left_possible_op, right_possible_op, self.s[k])
                    if ans<=self.max_ans:
                        op.add(ans)
                    # print(f'{i=} {j=} {k=} {left_possible_ops=} {right_possible_ops=} {ans=} {self.max_ans=} {op=}')
        # print(f'-'*50)
        return op

    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        op = 0
        self.s = s
        self.max_ans = max(answers)
        s_len = len(self.s)
        correct_op = self.get_correct_score(self.s, s_len)
        all_possible_op = self.get_all_possible_op(0, s_len-1)
        # print(f'{correct_op=} {all_possible_op=}')
        for ans in answers:
            if ans == correct_op:
                op+=5
            elif ans in all_possible_op:
                op+=2
        return op