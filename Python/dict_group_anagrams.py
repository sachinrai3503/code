# https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
# https://leetcode.com/problems/group-anagrams/
"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

# Here solution uses sort and dict.
# For Sorting based solution see - string_print_all_anagram_together.c
# For O(N*M) time based solution see StringPrintAllAnagramTogether.java.

def to_list(ip_dict):
    ip_list = list()
    for value in ip_dict.values():
        ip_list.append(value)
    return ip_list

def get_new_list_with_each_string_sorted(ip_list):
    new_list = list()
    for string in ip_list:
        new_list.append(''.join(sorted(string)))
    return new_list

def group_all_anagrams(ip_list):
    anagram_dict = dict()
    ip_list_with_sorted_strings = get_new_list_with_each_string_sorted(ip_list)
    print('Sorted =>',ip_list_with_sorted_strings)
    for i in range(len(ip_list_with_sorted_strings)):
        sorted_string = ip_list_with_sorted_strings[i]
        if sorted_string in anagram_dict.keys():
            anagram_dict[sorted_string].append(ip_list[i])
        else:
            anagram_dict[sorted_string] = [ip_list[i]]
    return to_list(anagram_dict)

def main():
    ip_list = ["cat", "dog", "tac", "god", "act","doggy","ggdoy"]
    print('ip=>', ip_list)
    anagram_dict = group_all_anagrams(ip_list)
    print(anagram_dict)

if __name__ == '__main__':
    main()