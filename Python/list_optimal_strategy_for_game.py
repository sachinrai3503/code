# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-set-2/?ref=lbp
# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-set-3/?ref=rp
"""
Consider a row of n coins of values v1 . . . vn, where n is even. 
We play a game against an opponent by alternating turns. 
In each turn, a player selects either the first or last coin from the row, 
removes it from the row permanently, and receives the value of the coin.

Determine the maximum possible amount of money we can definitely win 
if we move first.

Note: The opponent is as clever as the user.

Also, print the sequence of moves in the optimal game. 
As many sequences of moves may lead to the optimal answer, print 
any valid sequence.

Examples:
Input: 10 80 90 30
Output: 110 RRRL

Input: 10 100 10
Output: 20 RRL
"""

def get_max(a, b):
    return a if a>b else b

def find_max_amount(ip_list):
    length = len(ip_list)
    if length<=0: return -1, []
    best_seq = list()
    op = [[0]*length, [0]*length]
    for i in range(length-1, -1, -1):
        cur_row = i%2
        prev_row = 1 if cur_row==0 else 0
        sum = 0
        for j in range(i,length):
            sum+=ip_list[j]
            if i==j:
                op[cur_row][j] = ip_list[i]
                if i==0: best_seq.append('L')
            else:
                with_i, with_j = 0, 0
                with_i = ip_list[i] + (sum-ip_list[i]-op[prev_row][j])
                with_j = ip_list[j] + (sum-ip_list[j]-op[cur_row][j-1])
                if with_i>with_j:
                    op[cur_row][j] = with_i
                    if i==0: best_seq.append('L')
                else:
                    op[cur_row][j] = with_j
                    if i==0: best_seq.append('R')
    best_seq = list(reversed(best_seq))
    return op[0][length-1], best_seq

def main():
    ip_list = [18, 20, 15, 30, 10, 14]
    print('ip>>',ip_list)
    max_amt, best_seq = find_max_amount(ip_list)
    print('Max amount =',max_amt)
    print('Best seq.',best_seq)

if __name__ == '__main__':
    main()
