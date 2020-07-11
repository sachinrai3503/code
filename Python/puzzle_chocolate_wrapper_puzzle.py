#https://www.geeksforgeeks.org/program-chocolate-wrapper-puzzle/
"""
Given following three values, the task is to find the total number of maximum chocolates you can eat.

money : Money you have to buy chocolates
price : Price of a chocolate
wrap : Number of wrappers to be returned for getting one extra chocolate.

It may be assumed that all given values are positive integers and greater than 1.

Input :   money = 16, price = 2, wrap = 2
Output :   15

Input :   money = 15, price = 1, wrap = 3
Output :   22

Input :  money = 20, price = 3, wrap = 5
Output :   7
"""

def get_max_chocolate(money, price, wrap):
    total_chocolate = money//price
    total_wrapper = total_chocolate
    while total_wrapper >= wrap:
        extra_chocolate = total_wrapper//wrap
        total_chocolate+=extra_chocolate
        total_wrapper = total_wrapper%wrap + extra_chocolate
    return total_chocolate

def main():
    money, price, wrap = 20, 3, 5
    print('Total Chocolate =',get_max_chocolate(money,price,wrap))

if __name__ == '__main__':
    main()