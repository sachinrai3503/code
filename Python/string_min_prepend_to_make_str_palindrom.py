
# https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/
"""
Given a string str we need to tell 
 minimum characters to be added at front of string
 to make string palindrome.

Examples:
Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.
"""

def get_reversed(text):
    reversed_text = list()
    for i in range(len(text)-1,-1,-1):
        reversed_text.append(text[i])
    return ''.join(reversed_text)

def get_lps(text):
    """
    Returns the length of longest proper 
    prefix which is also suffix.
    """
    lps_list = [None]*len(text)
    for i in range(len(text)):
        j = i-1
        while j>0 and text[lps_list[j]]!=text[i]:
            j = lps_list[j]-1
        if j==-1:
            lps_list[i] = 0
        elif text[lps_list[j]]==text[i]:
            lps_list[i] = lps_list[j]+1
        else:
            lps_list[i] = 0
    print('lps',lps_list)
    return lps_list[len(lps_list)-1]

def get_min_prepend_to_make_palindrom(text):
    new_text = text + '$' + get_reversed(text)
    print('new text>',new_text)
    longest_palindrom_substr_from_index0 = get_lps(new_text)
    return len(text) - longest_palindrom_substr_from_index0

def main():
    text = "aabcbaaa"
    print('ip>',text)
    print('min count =',get_min_prepend_to_make_palindrom(text))

if __name__ == '__main__':
    main()