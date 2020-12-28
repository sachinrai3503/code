# https://leetcode.com/problems/text-justification/
"""
Given an array of words and a width maxWidth, format the text such that each 
line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words
 as you can in each line. Pad extra spaces ' ' when necessary so that each line 
 has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the 
 number of spaces on a line do not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
 inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 
Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."],
       maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
 because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to",
        "explain","to","a","computer.","Art","is","everything","else","we","do"], 
       maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""


def print_words_in_line(words_in_line):
    length = len(words_in_line)
    i = 0
    k = 1
    while i < length and words_in_line[i] != -1:
        print('Line', k, 'word from', i+1, 'to', words_in_line[i])
        i = words_in_line[i]
        k += 1


class Solution:

    def wrap_word(self, words, width, x):
        op = list()
        length = len(words)
        i = 0
        while i < length:
            word_len = len(words[i])
            word_count = 1
            j = i+1
            while j < length:
                word_len = word_len + 1 + len(words[j])
                if word_len > width:
                    break
                word_count += 1
                j += 1
            if j != length:
                word_len -= (len(words[j])+1)
            extra_space = width-word_len
            op_word = words[i]
            if word_count > 1:
                if j != length:
                    quo, rem = extra_space//(word_count -
                                             1), extra_space % (word_count-1)
                else:
                    quo, rem = 0, 0
                # print(word_len, extra_space, word_count, quo, rem)
                for k in range(i+1, j):
                    op_word = op_word + ' ' + ' '*quo + \
                        ' '*(1 if rem > 0 else 0) + words[k]
                    rem -= 1
                if j == length:
                    op_word = op_word + ' '*extra_space
            else:
                quo, rem = extra_space, 0
                # print(word_len, extra_space, word_count, quo, rem,'--')
                op_word = op_word + ' '*quo + ' '*rem
            op.append(op_word)
            i = j
        return op

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        return self.wrap_word(words, maxWidth, 2)
