# https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""
A car travels from a starting position to a destination which is target miles east of the
 starting position.

There are gas stations along the way. The gas stations are represented as an array stations
 where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles
 east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters
 of fuel in it. It uses one liter of gas per one mile that it drives. When the car
 reaches a gas station, it may stop and refuel, transferring all the gas from the
 station into the car.

Return the minimum number of refueling stops the car must make in order to reach its
 destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel 
 there. If the car reaches the destination with 0 fuel left, it is still considered to
 have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 
Constraints:
1 <= target, startFuel <= 109
0 <= stations.length <= 500
0 <= positioni <= positioni+1 < target
1 <= fueli < 109
"""

class Heap:
    def __init__(self, max_size):
        self.data = [None for i in range(max_size)]
        self.cur_size = 0
        self.max_size = max_size
    
    def is_empty(self):
        return self.cur_size==0

    def is_full(self):
        return self.cur_size==self.max_size

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def max_heapify(self, index):
        left = index*2+1
        right = index*2+2
        max_index = index
        if left<self.cur_size and self.data[left]>self.data[max_index]:
            max_index = left
        if right<self.cur_size and self.data[right]>self.data[max_index]:
            max_index = right
        if index!=max_index:
            self.swap(index, max_index)
            self.max_heapify(max_index)
    
    def insert_data(self, data):
        if self.is_full():
            print("Full")
            return
        else:
            index = self.cur_size
            parent_index = (index-1)//2
            self.cur_size+=1
            self.data[index] = data
            while index>0 and self.data[index]>self.data[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2
    
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.max_heapify(0)
            return temp

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        stop = 0
        stations_len = len(stations)
        fuel_stops = Heap(stations_len)
        cur_reach = startFuel
        station_index = 0
        while cur_reach<target:
            while station_index<stations_len and stations[station_index][0]<=cur_reach:
                fuel_stops.insert_data(stations[station_index][1])
                station_index+=1
            # print(f'fuel_stops = {fuel_stops.data[:fuel_stops.cur_size]}, {cur_reach=}, {stop=}')
            if not fuel_stops.is_empty():
                temp = fuel_stops.delete_top()
                # print(f'{temp=}')
                cur_reach+=temp
                stop+=1
            else: return -1
        return stop