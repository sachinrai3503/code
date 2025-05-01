# https://leetcode.com/problems/24-game
"""
You are given an integer array cards of length 4. You have four cards, each 
 containing a number in the range [1, 9]. You should arrange the numbers on 
 these cards in a mathematical expression using the operators ['+', '-', '*', '/']
 and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
    For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.

Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
    For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.

You cannot concatenate numbers together
    For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.

Return true if you can get such expression that evaluates to 24, and false otherwise.

Example 1:
Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: cards = [1,2,1,2]
Output: false

Constraints:
cards.length == 4
1 <= cards[i] <= 9
"""

# NOTE - related to  https://leetcode.com/problems/the-score-of-students-solving-math-expression

from typing import Set, List

class Solution:

    def solve(self, a, b, oper):
        op = 0
        if oper=='+': return a+b
        if oper=='*': return a*b
        if oper=='-': return a-b
        if oper=='/': return a/b if b!=0 else 0

    @cache
    def get_all_op_comb(self, cards, i, j) -> Set:
        if i>j: return None
        if i==j: return {cards[i],}
        op = set()
        for s in range(i+1, j+1):
            left_possible_ops = self.get_all_op_comb(cards, i, s-1)
            right_possible_ops = self.get_all_op_comb(cards, s, j)
            for left_possible_op in left_possible_ops:
                for right_possible_op in right_possible_ops:
                    for oper in self.operators:
                        result = self.solve(left_possible_op, right_possible_op, oper)
                        op.add(result)
                        if i==0 and j==3 and abs(24.0-result)<self.delta:
                            self.delta = abs(24.0-result)
        return op

    # def compute_for_comb(self, cards, cards_len):
    #     if tuple(cards) not in self.visited:
    #         self.visited.add(tuple(cards))
    #         t_op = self.get_all_op_comb(0, cards_len-1)
    #         # print(f'{self.visited=} {self.cards=} {t_op=}')
    #         return t_op
    #     return set()

    def compute_op_for_all_comb(self, cards, cards_len, s):
        if s>=cards_len:
            self.ops.update(self.get_all_op_comb(tuple(cards), 0, cards_len-1))
            # print(f'{cards=} {self.ops=}')
            return
        i = s
        while i<cards_len:
            cards[s], cards[i] = cards[i], cards[s]
            self.compute_op_for_all_comb(cards, cards_len, s+1)
            cards[s], cards[i] = cards[i], cards[s]
            i+=1

    def judgePoint24(self, cards: List[int]) -> bool:
        cards_len = len(cards)
        self.cards = cards
        self.operators = ['+','-','*','/']
        self.ops = set()
        self.visited = set()
        self.delta = maxsize
        self.compute_op_for_all_comb(cards, cards_len, 0)
        # print(f'{self.ops=}')
        # return 24 in self.ops
        return self.delta<=(1/10**5)