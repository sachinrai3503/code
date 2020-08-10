# https://www.geeksforgeeks.org/next-greater-element/
"""
Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element on the 
right side of x in array. 
Elements for which no greater element exist, 
consider next greater element as -1.

lement       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   -1
"""

class Stack:
    def __init__(self, max_size):
        self.data_list = list()
        self.cur_size = 0
        self.max_size = max_size
    
    def push(self, data):
        if self.is_full():
            print('Stack Full')
        else: 
            self.data_list.append(data)
            self.cur_size+=1

    def pop(self):
        if self.is_empty():
            print('Empty')
            return -1
        else:
            self.cur_size-=1
            return self.data_list.pop(-1)
    
    def get_top(self):
        if self.is_empty():
            return -1
        else: return self.data_list[-1]

    def is_full(self):
        if self.cur_size==self.max_size: return True
        return False

    def is_empty(self):
        if self.cur_size==0: return True
        return False


def find_NGT(ip_list):
    nge_list = [-1 for i in range(len(ip_list))]
    stck = Stack(len(ip_list))
    for i in range(len(ip_list)):
        while(stck.is_empty()==False and ip_list[stck.get_top()]<ip_list[i]):
            temp = stck.pop()
            nge_list[temp] = ip_list[i]
        stck.push(i)
    while(stck.is_empty()==False):
        temp = stck.pop()
        nge_list[temp] = -1
    return nge_list

def main():
    ip_list = [13, 7, 6, 12]
    print('ip_list>',ip_list)
    nge_list = find_NGT(ip_list)
    print('NGE=',nge_list)

if __name__ == '__main__':
    main()