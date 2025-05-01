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

from typing import List
from collections import defaultdict

class DJSet:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj: return
        ri = self.rank[pi]
        rj = self.rank[pj]
        if ri>rj:
            self.parent[pj] = pi
        elif ri<rj:
            self.parent[pi] = pj
        else:
            self.parent[pj] = pi
            self.rank[pi]+=1

class Solution:
    def accountsMerge1(self, accounts: List[List[str]]) -> List[List[str]]:
        account_len = len(accounts)
        dj_set = DJSet(account_len)
        email_to_acc_map = dict()
        acc_to_email_map = dict()
        for i in range(account_len):
            for email in accounts[i][1:]:
                if email not in email_to_acc_map:
                    email_to_acc_map[email] = i
                else:
                    dj_set.union(email_to_acc_map[email], i)
        # print(f'{dj_set.parent=}')
        for i in range(dj_set.size):
            parent_i = dj_set.find_parent(i)
            # print(f'{i=} {parent_i=}')
            if parent_i not in acc_to_email_map:
                acc_to_email_map[parent_i] = [accounts[i][0], accounts[i][1:]]
            else:
                acc_to_email_map[parent_i][1].extend(accounts[i][1:])
        # print(f'{acc_to_email_map=}')
        op = list()
        for key in acc_to_email_map:
            name, emails = acc_to_email_map[key]
            emails = set(emails)
            op.append([name, *sorted(emails)])
        return op

    # no need for set and simple
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_len = len(accounts)
        dj_set = DJSet(account_len)
        email_to_acc_map = dict()
        acc_to_email_map = defaultdict(list)
        for i in range(account_len):
            for email in accounts[i][1:]:
                if email not in email_to_acc_map:
                    email_to_acc_map[email] = i
                else:
                    dj_set.union(email_to_acc_map[email], i)
        # print(f'{dj_set.parent=}')
        for email, i in email_to_acc_map.items():
            parent = dj_set.find_parent(i)
            acc_to_email_map[parent].append(email)
        # print(f'{acc_to_email_map=}')
        op = list()
        for key in acc_to_email_map:
            name, emails = accounts[key][0], acc_to_email_map[key]
            op.append([name, *sorted(emails)])
        return op
