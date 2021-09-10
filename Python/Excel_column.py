# https://www.geeksforgeeks.org/find-excel-column-name-given-number/
# https://www.geeksforgeeks.org/find-excel-column-number-column-title/
# https://leetcode.com/problems/excel-sheet-column-title/
# https://leetcode.com/problems/excel-sheet-column-number/

def get_column_name(col_num):
    """
    Input          Output
    26             Z
    51             AY
    705            AAC
    """
    col_name = str()
    num = col_num
    while num>0:
        rem = (num-1)%26
        quo = (num-1)//26
        col_name = chr(rem+65) + col_name
        num = quo
    return col_name

def get_column_number(col_name_str):
    """
    column  column number
    A  ->  1
    AA ->  27
    AB ->  28 
    """
    col_num = 0
    length = len(col_name_str)
    for i in range(length):
        col_num= col_num +  (26**i)*(ord(col_name_str[length-1-i])-64)
    return col_num

def main():
    col_name = 'CDA'
    print('col name =>',col_name)
    col_num = get_column_number(col_name)
    print('col num =>',col_num)
    print('cal. col. name =>',get_column_name(col_num))

if __name__ == '__main__':
    main()
