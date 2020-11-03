# https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
"""
Given a 2D grid of characters and a word, find all occurrences of the given 
word in the grid. A word can be matched in all 8 directions at any point. 

Word is said to be found in a direction if all characters match in this 
direction (not in zig-zag form).

The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up 
and 4 Diagonal directions.

Example:

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "GEEKS"

Output: pattern found at 0, 0
        pattern found at 0, 8
        pattern found at 1, 0

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "EEE"

Output: pattern found at 0, 2
        pattern found at 0, 10
        pattern found at 2, 2
        pattern found at 2, 12
"""


def is_valid(row_count, col_count, i, j):
    if i < 0 or i >= row_count or j < 0 or j >= col_count:
        return False
    return True


def search_in_given_direction(grid, word, si, sj, i_offset, j_offset):
    """
    @param s1, sj - Starting index to search from in the grid.
    @param i_offset, j_offset - For giving the direction to search.
    """
    if len(word) <= 0 or len(grid) <= 0 or len(grid[0]) <= 0:
        print('Invalid input')
        return False
    word_len = len(word)
    row_count = len(grid)
    col_count = len(grid[0])
    ti, tj = si, sj
    k = 0
    while k < word_len and is_valid(row_count, col_count, ti, tj) and \
            grid[ti][tj] == word[k]:
        ti, tj = ti+i_offset, tj+j_offset
        k += 1
    if k != word_len:
        return False
    return True


def search_word_in_grid(grid, word):
    adj_offset = [[-1, -1, -1, 0, 1, 1, 1, 0],
                  [-1, 0, 1, 1, 1, 0, -1, -1]]
    row_count = len(grid)
    col_count = len(grid[0])
    i, j = 0, 0
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j] == word[0]:
                for k in range(8):
                    is_found = search_in_given_direction(grid, word, i, j,
                                                         adj_offset[0][k],
                                                         adj_offset[1][k])
                    if is_found:
                        print('Found at (', i, ':', j, ')', sep='')
                        break


def main():
    grid = ["GEEKSFORGEEKS",
            "GEEKSQUIZGEEK",
            "IDEQAPRACTICE"]
    word = 'EE'
    print('grid=', grid)
    print('word>', word)
    search_word_in_grid(grid, word)


if __name__ == '__main__':
    main()
