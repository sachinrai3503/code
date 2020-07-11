# https://www.geeksforgeeks.org/minimum-number-appends-needed-make-string-palindrome/
"""
Given a string s we need to tell minimum characters
 to be appended (insertion at end) to make a string palindrome.

Examples:
Input : s = "abede"
Output : 2
We can make string palindrome as "abedeba"
by adding ba at the end of the string.
"""

from string_min_prepend_to_make_str_palindrom import get_lps
from string_min_prepend_to_make_str_palindrom import get_reversed

def get_min_append_to_make_palindrom(text):
    new_text = get_reversed(text) + '$' + text
    print('new text>',new_text)
    longest_palindrom_substr_from_index0 = get_lps(new_text)
    return len(text) - longest_palindrom_substr_from_index0

def main():
    text = "aabb"
    print('ip>',text)
    print('min count =',get_min_append_to_make_palindrom(text))

if __name__ == '__main__':
    main()