# https://www.lintcode.com/problem/3638
# https://leetcode.com/problems/single-row-keyboard
"""
A custom string keyboard keyboard of fixed length 26, consisting of 26 lowercase letters all aligned on one line.

The custom keyboard has index subscripts from 0 to 25. Initially, your finger is at index subscript 0, and each time you 
 type a character, you need to move your finger to the index of the corresponding character in the keyboard keyboard, and
 the number of moves required to move from index i to index j is |i - j|.

Now given a word string word, calculate how many times you need to move it to type the word.

Constraints:
keyboard.length == 26
keyboard contains each English lowercase letter exactly once in some order.
1 <= word.length <= 10^4
word[i] is an English lowercase letter.
"""

class Solution:
    """
    @param keyboard: Customized keyboard strings
    @param word: A string
    @return: Total number of moves
    """
    def calculate_time(self, keyboard: str, word: str) -> int:
        d1 = {keyboard[i]:i for i in range(26)}
        op, prev = 0, 0
        for char in word:
            op = op + abs(prev-d1[char])
            prev = d1[char]
        return op