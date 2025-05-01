# https://leetcode.com/problems/car-pooling
"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] 
 indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them
 off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 
Constraints:
1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""

from typing import List

class Solution:

    # Will fail for [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        trips_len = len(trips)
        trips.sort(key = lambda x : x[1])
        cur_cap = 0
        print(f'{trips=}')
        i, j = 0, 0
        while i < trips_len:
            if trips[i][1]<trips[j][2]:
                cur_cap+=trips[i][0]
                i+=1
            else:
                cur_cap-=trips[j][0]
                j+=1
            print(f'{i=} {j=}')
            if cur_cap>capacity:
                return False
        return True
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_len = len(trips)
        start = [i for i in range(trips_len)]
        end = [j for j in range(trips_len)]
        start.sort(key = lambda x : trips[x][1])
        end.sort(key = lambda x : trips[x][2])
        cur_cap = 0
        i, j = 0, 0
        while i<trips_len:
            if trips[start[i]][1]<trips[end[j]][2]:
                cur_cap+=trips[start[i]][0]
                i+=1
            else:
                cur_cap-=trips[end[j]][0]
                j+=1
            # print(f'{i=} {j=}')
            if cur_cap>capacity:
                return False
        return True