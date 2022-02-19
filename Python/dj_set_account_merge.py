# https://leetcode.com/problems/accounts-merge/
"""
Given a list of accounts where each element accounts[i] is a list of strings,
 where the first element accounts[i][0] is a name, and the rest of the elements are
 emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the
 same person if there is some common email to both accounts. Note that even if two
 accounts have the same name, they may belong to different people as people could
 have the same name. A person can have any number of accounts initially, but all of
 their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first
 element of each account is the name, and the rest of the elements are emails in
 sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 
Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

class DJSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find_parent(self, u):
        if self.parent[u]==u: return u
        self.parent[u] = self.find_parent(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        p_u = self.find_parent(u)
        p_v = self.find_parent(v)
        if p_u==p_v: return
        # Here rank is by depth
        if self.rank[p_u]==self.rank[p_v]:
            self.parent[p_v] = p_u
            self.rank[p_u]+=1
        elif self.rank[p_u]<self.rank[p_v]:
            self.parent[p_u] = p_v
        elif self.rank[p_u]>self.rank[p_v]:
            self.parent[p_v] = p_u
            
    def print_dj_set(self):
        print(self.parent)
        print(self.rank)
            
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dj_set = DJSet(n)
        email_to_index_map = dict()
        for i in range(n):
            account = accounts[i]
            for email in account[1:]:
                parent = email_to_index_map.get(email, None)
                if parent is None:
                    email_to_index_map[email] = i
                else:
                    dj_set.union(parent, i)
            # dj_set.print_dj_set()
        # print(email_to_index_map)
        merged_acc = list()
        for i in range(n):
            parent_i = dj_set.find_parent(i)
            if parent_i==i:
                merged_acc.append(accounts[i])
            else:
                accounts[parent_i].extend(accounts[i][1:])
        # print(merged_acc)
        for i in range(len(merged_acc)):
            acc = merged_acc[i]
            merged_acc[i] = acc[0:1] + sorted(set(acc[1:]))
        return merged_acc