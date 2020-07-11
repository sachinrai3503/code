# https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/?ref=lbp
"""
Given a string of size ‘n’. The task is to remove or delete 
minimum number of characters from the string so
 that the resultant string is palindrome.

Note: The order of characters should be maintained.

Examples :

Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string
"""

from string_min_insertion_to_make_palindrom import get_min
from string_min_insertion_to_make_palindrom import get_longest_palindrom_subseq_len

def get_min_del_to_make_palindrom(text):
    longest_palin_subseq_len = get_longest_palindrom_subseq_len(text)
    return len(text) - longest_palin_subseq_len

def main():
    text = "geeksforgeeks"
    print('ip>',text)
    print('min insertion=',get_min_del_to_make_palindrom(text))

if __name__=='__main__':
    main()