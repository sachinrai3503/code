# https://www.geeksforgeeks.org/check-if-two-strings-after-processing-backspace-character-are-equal-or-not/
"""
Given two strings s1 and s2, let us assume that while typing the strings
 there were some backspaces encountered which are represented by #.
 
The task is to determine whether the resultant strings after processing 
the backspace character would be equal or not.

Examples:

Input: s1= geee#e#ks, s2 = gee##eeks 
Output: True 

Input: s1 = equ#ual, s2 = ee#quaal#
Output:  False
"""

def next_valid_index(string, i):
    count = 0
    while i>=0:
        if string[i]=='#':
            count+=1
            i-=1
        elif count>0:
            count-=1
            i-=1
        else:
            break
    return i
        

def is_equal(str1, str2):
    i, j = len(str1)-1, len(str2)-1
    while i>=0 and j>=0:
        i = next_valid_index(str1,i)
        j = next_valid_index(str2,j)
        if i!=-1 and j!=-1:
            if str1[i]==str2[j]:
                i-=1
                j-=1
            else:
                return False
    i = next_valid_index(str1,i)
    j = next_valid_index(str2,j)
    if i==-1 and j==-1:
        return True
    else:
        return False

def main():
    str1 = 'AA##BCAS#'
    str2 = 'B#BCA'
    print('str1=>',str1)
    print('str2=>',str2)
    print('are equal =>',is_equal(str1,str2))

if __name__ == '__main__':
    main()