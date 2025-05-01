# https://leetcode.com/problems/guess-the-word
"""
You are given an array of unique strings words where words[i] is six letters long. One word of words was
 chosen as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string,
 and it must be from words. Master.guess(word) returns:

-1 if word is not from words, or
an integer representing the number of exact matches (value and position) of your guess to the secret word.
There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can
 call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed
 guesses. You will get:

"Either you took too many guesses, or you did not find the secret word." if you called Master.guess 
 more than allowedGuesses times or if you did not call Master.guess with the secret word, or
"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of 
 calls to Master.guess less than or equal to allowedGuesses.
The test cases are generated such that you can guess the secret word with a reasonable strategy (other than
 using the bruteforce method).

Example 1:
Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.

Example 2:
Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation: Since there are two words, you can guess both.

Constraints:
1 <= words.length <= 100
words[i].length == 6
words[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in words.
10 <= allowedGuesses <= 30
"""

from collections import defaultdict
from typing import List

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass

class Solution:

    def count_matching_char(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i]==word2[i]:
                count+=1
        return count

    def get_word_dict_by_letter_pos(self, words):
        # key = [0-5]
        # for each key 0<=i<=5 in the dict, values will be a dict 
        # value_dict = {'a': [list of word with 'a' in i position], 'b':[word with 'b' in i pos]}
        word_dict = {i:defaultdict(set) for i in range(6)}
        for word in words:
            for i in range(6):
                word_dict[i][word[i]].add(word)
        # print(f'{word_dict=}')
        return word_dict

    # Will not work for below
    # "cmgfju"
    # ["mvlbvs","dxjnxh","tjipwc","uaqwgm","iunakv","lcdzdl","kkhxsx","zfzyrb","adcmbk",
    #  "rlbojq","rzaspp","cmgfju"]
    # 10
    def findSecretWord1(self, words: List[str], master: 'Master') -> None:
        words_len = len(words)
        ignored_words = set()
        word_dict = self.get_word_dict_by_letter_pos(words)
        for i in range(words_len):
            word_i = words[i]
            if word_i in ignored_words: continue
            guess_count = master.guess(word_i)
            print(f'{i=} {word_i=} {guess_count=}')
            if guess_count==0:
                for k in range(6):
                    # print(f'{word_i=} {k=} {word_dict[k][word_i[k]]=}')
                    ignored_words.update(word_dict[k][word_i[k]])
            elif guess_count<6:
                ignored_words.add(word_i)
                for j in range(i+1, words_len):
                    word_j = words[j]
                    if word_j in ignored_words: continue
                    if self.count_matching_char(word_i, word_j)!=guess_count:
                        ignored_words.add(word_j)
            else:
                break
        print(f'{ignored_words=}')
        return
    
    # https://leetcode.com/problems/guess-the-word/solutions/556075/how-to-explain-to-interviewer-843-guess-the-word
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        words_len = len(words)
        words_set = set(words)
        word_dict = self.get_word_dict_by_letter_pos(words)
        # print(f'{word_dict=}')
        ignored_words = set()
        new_words_set = set()
        while words_set:
            # print(f'{len(words_set)=} {words_set=}')
            word_i = words_set.pop()
            guess_count = master.guess(word_i)
            # print(f'{word_i=} {guess_count=}')
            if guess_count==0:
                for k in range(6):
                    # print(f'{word_i=} {k=} {word_dict[k][word_i[k]]=}')
                    ignored_words.update(word_dict[k][word_i[k]])
                words_set.difference_update(ignored_words)
                ignored_words.clear()
            elif guess_count<6:
                # print(f'- {len(words_set)=} {words_set=}')
                while words_set:
                    t_word = words_set.pop()
                    if self.count_matching_char(word_i, t_word)==guess_count:
                        new_words_set.add(t_word)
                # print(f'- {len(new_words_set)=} {new_words_set=}')
                words_set.update(new_words_set)
                new_words_set.clear()
            else:
                break
        # print(f'{ignored_words=}')
        return