# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
"""
RandomizedCollection is a data structure that contains a collection of numbers,
 possibly duplicates (i.e., a multiset). It should support inserting and removing
 specific elements and also removing a random element.

Implement the RandomizedCollection class:
RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item 
                     is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. 
                     Returns true if the item is present, false otherwise.
                     Note that if val has multiple occurrences in the multiset, we 
                     only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. 
                The probability of each element being returned is linearly related
                 to the number of same values the multiset contains.

You must implement the functions of the class such that each function works on
 average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if
 there is at least one item in the RandomizedCollection.

Example 1:
Input
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
Output
[null, true, false, true, 2, true, 1]

Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls in total will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

import random

class RandomizedCollection:

    def __init__(self):
        self.ele_list = [None for i in range(200000)]
        self.dict = dict() # ele to index_in_ele_list
        # if ele_list[i] = ele and dict[ele][M] = i then index_in_eles_index_in_ele_list[i] = M
        self.index_in_eles_index_in_ele_list = [None for i in range(200000)]
        self.cur_size = 0

    def search(self, val):
        return self.dict.get(val, None)
        
    def insert(self, val: int) -> bool:
        is_not_present = False
        val_index_list = self.search(val)
        if val_index_list is None:
            is_not_present = True
            val_index_list = list()
            self.dict[val] = val_index_list
        self.ele_list[self.cur_size] = val
        val_index_list.append(self.cur_size)
        self.index_in_eles_index_in_ele_list[self.cur_size] = len(val_index_list)-1
        self.cur_size+=1
        # print(self.dict, self.ele_list[:self.cur_size])
        return is_not_present

    def remove(self, val: int) -> bool:
        val_index_list = self.search(val)
        if val_index_list is None: return False
        last_val_index = val_index_list.pop()
        self.ele_list[last_val_index] = None
        self.index_in_eles_index_in_ele_list[last_val_index] = None
        self.cur_size-=1
        if last_val_index != self.cur_size:
            self.ele_list[last_val_index] = self.ele_list[self.cur_size]
            self.dict[self.ele_list[last_val_index]][self.index_in_eles_index_in_ele_list[self.cur_size]] = last_val_index
            self.index_in_eles_index_in_ele_list[last_val_index] = self.index_in_eles_index_in_ele_list[self.cur_size]
            self.ele_list[self.cur_size] = None
            self.index_in_eles_index_in_ele_list[self.cur_size] = None 
        if len(val_index_list) == 0:
            self.dict.pop(val)
        # print(self.dict, self.ele_list[:self.cur_size])
        return True

    def getRandom(self) -> int:
        return self.ele_list[random.randint(0,self.cur_size-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
