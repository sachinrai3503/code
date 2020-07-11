# https://www.geeksforgeeks.org/find-number-times-string-occurs-given-string/
"""
Given two strings, 
find the number of times the second string occurs in the first string,
 whether continuous or discontinuous.

Examples:

Input:  
string a = "GeeksforGeeks"
string b = "Gks"

Output: 4

"""

def count_occurences_rec(text, text_index, pat, pat_index):
    if len(text)<=0 or len(pat)<=0:
        print('In valid inputs')
        return 0
    if pat_index==len(pat):
        return 1
    if text_index==len(text):
        return 0
    count = 0
    from_index = text_index
    for i in range(from_index,len(text),1):
        if text[i] == pat[pat_index]:
            count+=count_occurences_rec(text,i+1,pat,pat_index+1)
    return count

def count_occurences_dp(text,pat):
    text_len = len(text)
    pat_len = len(pat)
    if text_len<=0 or pat_len<=0:
        print('In valid inputs')
        return 0
    op = [[0]*text_len,[0]*text_len]
    # print(op)
    for i in range(pat_len-1,-1,-1):
        cur_row = i%2
        prev_row = 1 if cur_row == 0 else 0
        prev = 0
        for j in range(text_len-1,-1,-1):
            if text[j]!=pat[i]:
                op[cur_row][j] = prev
            else:
                remaining_occ = 0
                if i==(pat_len-1):
                    remaining_occ = 1
                elif j==(text_len-1):
                    remaining_occ = 0
                else:
                    remaining_occ = op[prev_row][j+1]
                op[cur_row][j] = prev + remaining_occ
            prev = op[cur_row][j]
    # print(op)
    return op[0][0]

def main():
    text = 'GEEKSFORGEEKS'
    pat = 'EEK'
    print('text =>',text)
    print('pat =>',pat)
    print('Count(REC)=',count_occurences_rec(text,0,pat,0))
    print('Count(DP)=',count_occurences_dp(text,pat))

if __name__ == '__main__':
    main()