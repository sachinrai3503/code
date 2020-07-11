# https://www.geeksforgeeks.org/check-if-all-enemies-are-killed-with-bombs-placed-in-a-matrix/

"""
1. The matrix can contain 3 characters
X –> Denotes the War area.
B –> Denotes the bomb.
E –> Denotes the Enemies.

2. Bomb ‘B’ can blast in only horizontal and vertical directions from one end to another.
3. If all enemies are killed by the present bombs, print Yes, else print No
"""

def is_enemy_killed(war_matrix):
    row, col = len(war_matrix), len(war_matrix[0])
    enemy_alive = 0
    row_list, col_list = [0]*row, [0]*col
    for i in range(row):
        for j in range(col):
            if war_matrix[i][j] == 'B':
                enemy_alive = enemy_alive - (row_list[i] + col_list[j])
                row_list[i], col_list[j] = -1, -1
            elif war_matrix[i][j] == 'E':
                if row_list[i]==-1 or col_list[j]==-1:
                    continue
                else:
                    row_list[i]+=1
                    col_list[j]+=1
                    enemy_alive+=1
    if enemy_alive == 0:
        print("All enemy killed.")
        return True
    else:
        print(enemy_alive," not killed.")
        return False

def main():
    war_matrix = [  ['X','X','X','E','X'],
                    ['E','X','B','E','X'],
                    ['X','X','E','X','X'],
                    ['X','X','X','X','X'],
                    ['X','X','X','X','X']
                ]
    # print('ip',war_matrix)
    is_enemy_killed(war_matrix)

if __name__ == '__main__':
    main()
