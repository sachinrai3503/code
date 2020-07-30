# https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/
"""
Given the array representation of Complete Binary Tree i.e, if index i is the
 parent, index 2*i + 1 is the left child and index 2*i + 2 is the right child. 
 
Find the minimum number of swap required to convert it into BST.

Input : arr[] = { 5, 6, 7, 8, 9, 10, 11 }
Output : 3

                    5
            6               7
        8       9       10      11

                    To
            
                    8
            6               10
        5       7       9       11

Input : arr[] = { 1, 2, 3 }
Output : 1
"""

def swap(ip_list, i, j):
    ip_list[i], ip_list[j] = ip_list[j], ip_list[i]

def sort(pri_list, sec_list):
    for i in range(len(pri_list)):
        min = i
        for j in range(i+1,len(pri_list)):
            min = j if pri_list[j]<pri_list[min] else min
        swap(pri_list,i,min)
        swap(sec_list,i,min)

class In_Order:

    def __init__(self):
        self.in_order = list()
    
    def get_in_order(self):
        return self.in_order

    def add_node(self, data):
        self.in_order.append(data)

def get_in_order(ip_list, index, in_order):
    if index>=len(ip_list):return
    get_in_order(ip_list,index*2+1,in_order)
    in_order.add_node(ip_list[index])
    get_in_order(ip_list,index*2+2,in_order)

def count_min_swap(ip_list, expected_index_list):
    count = 0
    i = 0
    while i<len(ip_list):
        if i!=expected_index_list[i]:
            swap(ip_list,i,expected_index_list[i])
            swap(expected_index_list,i,expected_index_list[i])
            count+=1
        else:i+=1
    return count

def find_min_swap(tree_arr):
    in_order = In_Order()
    get_in_order(tree_arr,0,in_order)
    in_order_index = [i for i in range(len(in_order.get_in_order()))]
    sort(in_order.get_in_order(),in_order_index)
    print(in_order.get_in_order())
    print(in_order_index)
    return count_min_swap(in_order.get_in_order(),in_order_index)

def main():
    tree_arr = [1,2,3]
    print('Tree>',tree_arr)
    print('Min Swap=',find_min_swap(tree_arr))

if __name__ == "__main__":
    main()