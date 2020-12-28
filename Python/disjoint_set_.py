# https://www.geeksforgeeks.org/disjoint-set-data-structures/
"""
Consider a situation with a number of persons and following tasks to be 
performed on them.

Add a new friendship relation, i.e., a person x becomes friend of other person y.
Find whether individual x is a friend of individual y (direct or indirect friend)
Example:

We are given 10 individuals say,
a, b, c, d, e, f, g, h, i, j

Following are relationships to be added.
a <-> b  
b <-> d
c <-> f
c <-> i
j <-> e
g <-> j

And given queries like whether a is a friend of d
or not.

We basically need to create following 4 groups
and maintain a quickly accessible connection
among group items:
G1 = {a, b, d}
G2 = {c, f, i}
G3 = {e, g, j}
G4 = {h}
Problem : To find whether x and y belong to same group or not, i.e., 
to find if x and y are direct/indirect friends.
"""

class DisjointSet:
    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.rank   = [0 for i in range(length)]
    
    def find(self, element):
        if self.parent[element] == element:
            return element
        else:
            self.parent[element] = self.find(self.parent[element])
            return self.parent[element]
    
    def union(self, ele1, ele2):
        ele1_repr = self.find(ele1)
        ele2_repr = self.find(ele2)
        if ele1_repr==ele2_repr: return
        if self.rank[ele1_repr] == self.rank[ele2_repr]:
            self.parent[ele1_repr] = ele2_repr
            self.rank[ele2_repr]+=1
        elif self.rank[ele1_repr] < self.rank[ele2_repr]:
            self.parent[ele1_repr] = ele2_repr
        else:
            self.parent[ele2_repr] = ele1_repr

def main():
    dj_set = DisjointSet(10)
    dj_set.union(0, 2)
    dj_set.union(4, 2)
    dj_set.union(3, 1)
    if dj_set.find(4) == dj_set.find(0): 
        print('Yes') 
    else: 
        print('No') 
    if dj_set.find(1) == dj_set.find(0): 
        print('Yes') 
    else: 
        print('No')

if __name__ == '__main__':
    main()