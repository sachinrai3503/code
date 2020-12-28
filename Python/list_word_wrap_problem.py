# https://www.geeksforgeeks.org/word-wrap-problem-space-optimized-solution/
# https://www.geeksforgeeks.org/word-wrap-problem-dp-19/
"""
Given a sequence of words, and a limit on the number of characters that can be
 put in one line (line width). Put line breaks in the given sequence such that
 the lines are printed neatly. Assume that the length of each word is smaller 
 than the line width. When line breaks are inserted there is a possibility
 that extra spaces are present in each line. The extra spaces includes spaces 
 put at the end of every line except the last one.

The problem is to minimize the following total cost.
 Total cost = Sum of cost of all lines, 
              where cost of line is = (Number of extra spaces in the line)^2.


For example, consider the following string and line width M = 15
“Geeks for Geeks presents word wrap problem”
Following is the optimized arrangement of words in 3 lines
Geeks for Geeks
presents word
wrap problem

The total extra spaces in line 1 and line 2 are 0 and 2. 
Space for line 3 is not considered as it is not extra space as described above. 
So optimal value of total cost is 0 + 2*2 = 4.

Examples:

Input : arr[] = {3, 2, 2, 5}
Width = 6
Output : 1 1 2 3 4 4
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 3
Line number 3: From word no. 4 to 4 
"""

def print_words_in_line(words_in_line):
    length = len(words_in_line)
    i = 0
    k = 1
    while i < length and words_in_line[i] != -1:
        print('Line', k, 'word from', i+1, 'to', words_in_line[i])
        i = words_in_line[i]
        k += 1


def wrap_word(words, width, x):
    if width <= 0:
        print('Invalid')
        return -1, [-1]
    length = len(words)
    dp = [0]*length
    ans = [-1]*length
    # Since last line cost is to be taken as 0
    dp[-1] = 0
    ans[-1] = length
    for i in range(length-2, -1, -1):
        cur_width = words[i]
        cur_cost = (width-cur_width)**x + dp[i+1]
        dp[i] = cur_cost
        ans[i] = i+1
        j = i+1
        while j < length and (cur_width + 1 + words[j]) <= width:
            cur_width = cur_width + 1 + words[j]
            cur_cost = (width-cur_width)**x + (dp[j+1] if j < length-1 else 0)
            # If we can accomodate all the words from i to j in last line then
            # cost is 0.
            if j==length-1:
                cur_cost = 0
            if cur_cost < dp[i]:
                dp[i] = cur_cost
                ans[i] = j+1
            j += 1
    # print(dp)
    # print(ans)
    return dp[0], ans


def main():
    # words = [5,3,5,7,4,4,7]
    words = [1,1,1,1]
    width = 5
    x = 3
    print('Words width >', words)
    print('Line width >', width)
    cost, words_in_line = wrap_word(words, width, x)
    print('Cost =', cost)
    print('Words in line>>')
    print_words_in_line(words_in_line)


if __name__ == '__main__':
    main()
