# https://leetcode.com/problems/groups-of-strings/
"""
You are given a 0-indexed array of strings words. Each string consists of lowercase
 English letters only. No letter occurs more than once in any string of words.

Two strings s1 and s2 are said to be connected if the set of letters of s2 can be
 obtained from the set of letters of s1 by any one of the following operations:

Adding exactly one letter to the set of the letters of s1.
Deleting exactly one letter from the set of the letters of s1.
Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.

The array words can be divided into one or more non-intersecting groups. A string 
 belongs to a group if any one of the following is true:
    It is connected to at least one other string of the group.
    It is the only string present in the group.

Note that the strings in words should be grouped in such a manner that a string
 belonging to a group cannot be connected to a string present in any other group.
 It can be proved that such an arrangement is always unique.

Return an array ans of size 2 where:
    ans[0] is the maximum number of groups words can be divided into, and
    ans[1] is the size of the largest group.
 
Example 1:
Input: words = ["a","b","ab","cde"]
Output: [2,3]
Explanation:
- words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].
- words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].
- words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1].
- words[3] is not connected to any string in words.
Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.  

Example 2:
Input: words = ["a","ab","abc"]
Output: [1,3]
Explanation:
- words[0] is connected to words[1].
- words[1] is connected to words[0] and words[2].
- words[2] is connected to words[1].
Since all strings are connected to each other, they should be grouped together.
Thus, the size of the largest group is 3.
 
Constraints:
1 <= words.length <= 2 * 104
1 <= words[i].length <= 26
words[i] consists of lowercase English letters only.
No letter occurs more than once in words[i].
"""

# Both of below solution gets timed out.

from typing import List

class DJ_Set:
    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.rank = [1 for i in range(length)]
        self.length = length
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        parent_i = self.find_parent(i)
        parent_j = self.find_parent(j)
        rank_pi = self.rank[parent_i]
        rank_pj = self.rank[parent_j]
        if parent_i==parent_j: return
        if rank_pi>=rank_pj:
            self.parent[parent_j] = parent_i
            self.rank[parent_i]+=self.rank[parent_j]
        else:
            self.parent[parent_i] = parent_j
            self.rank[parent_j]+=self.rank[parent_i]
    
class Solution:
    
    def set_bit_for_char_present(self, word):
        bit_tag = 0
        for char in word:
            bit_tag|=(1<<(ord(char)-97))
        # print(f'{word=} {bit_tag=}')
        return bit_tag

    def count_set_bit(self, num):
        count = 0
        while num>0:
            count+=1
            num-=(num&-num)
        # print(f'{num=} {count=}')
        return count
    
    def is_connected(self, word1, word1_len, word1_tag, word2, word2_len, word2_tag):
        diff_len = abs(word1_len-word2_len)        
        words_xor = word1_tag^word2_tag
        if diff_len==1: return self.count_set_bit(words_xor)==1
        if words_xor==0: return True
        return self.count_set_bit(words_xor)==2
    
    # This gets time out
    def groupStrings1(self, words: List[str]) -> List[int]:
        words_len = len(words)
        group_count, max_size_of_group = 0, 0
        dj_set = DJ_Set(words_len)
        words_bit_tag = list()
        word_len_list = list()
        index_list = list()
        i = 0
        for word in words:
            words_bit_tag.append(self.set_bit_for_char_present(word))
            word_len_list.append(len(word))
            index_list.append(i)
            i+=1
        index_list.sort(key = lambda x : word_len_list[x])
        # print(f"{index_list=}")
        for i in range(words_len):
            for j in range(i+1, words_len):
                ai, aj = index_list[i], index_list[j] # word_actual_index
                if abs(word_len_list[ai]-word_len_list[aj])>1: break
                if self.is_connected(words[ai], word_len_list[ai], words_bit_tag[ai], words[aj], word_len_list[aj], words_bit_tag[aj]):
                    dj_set.union(ai, aj)
        for i in range(words_len):
            if dj_set.find_parent(i)==i:
                group_count+=1
                max_size_of_group = max(max_size_of_group, dj_set.rank[i])
        return [group_count, max_size_of_group]
    
    def get_connected_word_indexs(self, word_bit_mask, bitmask_index_map):
        index_list = []
        # Checking connection of ab->a or ab->abc 
        for i in range(26):
            if word_bit_mask&(1<<i):
                t_mask = word_bit_mask^(1<<i)
            else:
                t_mask = word_bit_mask|(1<<i)
            if t_mask in bitmask_index_map:
                # index_list.append(bitmask_index_map[t_mask])
                yield bitmask_index_map[t_mask]
        # Checking connected of ab->eb
        for i in range(26):
            if word_bit_mask&(1<<i):
                t_mask = word_bit_mask^(1<<i)
                for j in range(26):
                    if j!=i and not (t_mask&(1<<j)):
                        new_t_mask = t_mask|(1<<j)
                        if new_t_mask in bitmask_index_map:
                            # index_list.append(bitmask_index_map[new_t_mask])
                            yield bitmask_index_map[new_t_mask]
        # Checking if same word is present more that once
        if word_bit_mask in bitmask_index_map:
            # index_list.append(bitmask_index_map[word_bit_mask])
            yield bitmask_index_map[word_bit_mask]
        # return index_list

    # Space=O(n) Time=O(n*26*26)
    def groupStrings(self, words: List[str]) -> List[int]:
        words_len = len(words)
        group_count, max_size_of_group = 0, 0
        dj_set = DJ_Set(words_len)
        bitmask_index_map = dict() # {bit_mask : [index_list],...}
        for i in range(words_len):
            word = words[i]
            word_bit_mask = self.set_bit_for_char_present(word)
            # connected_word_indexs = self.get_connected_word_indexs(word_bit_mask, bitmask_index_map)
            for index in self.get_connected_word_indexs(word_bit_mask, bitmask_index_map):#connected_word_indexs:
                dj_set.union(i, index)
            bitmask_index_map[word_bit_mask] = i
            # print(f'{word=} {word_bit_mask=} {connected_word_indexs=}')
        for i in range(words_len):
            if dj_set.find_parent(i)==i:
                group_count+=1
                max_size_of_group = max(max_size_of_group, dj_set.rank[i])
        return [group_count, max_size_of_group]