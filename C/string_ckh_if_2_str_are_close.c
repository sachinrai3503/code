// https://leetcode.com/problems/determine-if-two-strings-are-close/
/*
Two strings are considered close if you can attain one from the other using the
 following operations:

Operation 1: Swap any two existing characters.
 For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another
 existing character, and do the same with the other character.
 For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, 
 and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, 
             in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Example 4:
Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa,
             in any amount of operations.
 
Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
*/

#include <stdio.h>
#include <malloc.h>
#define false 0
#define true 1

typedef int bool;

int get_max(int a, int b)
{
    return (a > b) ? a : b;
}

int *get_freq(char *ip, int length)
{
    int *freq = (int *)calloc(26, sizeof(int));
    int i = 0;
    for (; i < length; i++)
    {
        freq[ip[i] - 97]++;
    }
    return freq;
}

bool has_same_char(int *freq1, int *freq2)
{
    int i = 0;
    for (; i < 26; i++)
    {
        if (!((freq1[i] != 0 && freq2[i] != 0) ||
              (freq1[i] == 0 && freq2[i] == 0)))
            return false;
    }
    return true;
}

int *get_freq_char_map(int *freq1, int *freq2, int length)
{
    int *map = (int *)calloc(length, sizeof(int));
    int i = 0;
    for (; i < 26; i++)
    {
        if (freq1[i] > 0)
            map[freq1[i]]++;
        if (freq2[i] > 0)
            map[freq2[i]]++;
    }
    return map;
}

bool closeStrings(char *word1, char *word2)
{
    int l1 = strlen(word1);
    int l2 = strlen(word2);
    int *freq1 = get_freq(word1, l1);
    int *freq2 = get_freq(word2, l2);
    if (has_same_char(freq1, freq2) == false)
        return false;
    int *freq_char_map = get_freq_char_map(freq1, freq2, get_max(l1, l2) + 1);
    int i = 0;
    for (; i < l1 + 1; i++)
    {
        if (freq_char_map[i] % 2 == 1)
            return false;
    }
    return true;
}