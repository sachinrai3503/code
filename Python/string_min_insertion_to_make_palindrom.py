# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
"""
Given a string str, the task is to find the minimum number
 of characters to be inserted to convert it to palindrome.
Before we go further, let us understand with few examples:

ab: Number of insertions required is 1 i.e. bab
aa: Number of insertions required is 0 i.e. aa
abcd: Number of insertions required is 3 i.e. dcbabcd
"""

def get_min(a, b):
    if a>b:
        return a
    else:
        return b

def get_longest_palindrom_subseq_len(text):
    text_len = len(text)
    if text_len==0:
        return 0
    op = [[0]*text_len,[0]*text_len]
    for i in range(text_len-1,-1,-1):
        cur_row = i%2
        prev_row = 1 if cur_row==0 else 0
        for j in range(i,text_len,1):
            if i==j:
                op[cur_row][j] = 1
            elif text[i]==text[j]:
                if i==j-1:
                    op[cur_row][j] = 2
                else:
                    op[cur_row][j] = 2 + op[prev_row][j-1]
            else:
                op[cur_row][j] = get_min(op[cur_row][j-1],op[prev_row][j])
        # print(op)
    print(op)
    return op[0][text_len-1]

def get_min_insertion_to_make_palindrom(text):
    longest_palin_subseq_len = get_longest_palindrom_subseq_len(text)
    return len(text) - longest_palin_subseq_len

def main():
    text = "GEEKSFORGEEKS"
    print('ip>',text)
    print('min insertion=',get_min_insertion_to_make_palindrom(text))

if __name__=='__main__':
    main()