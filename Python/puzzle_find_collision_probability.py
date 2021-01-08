# https://www.geeksforgeeks.org/probability-of-collision-between-two-trucks/
"""
Given two strings S and T, where S represents the first lane in which vehicles
 move from left to right and T represents the second lane in which vehicles
 move from right to left. Vehicles can be of either B (bike), C (car) or
T (truck). The task is to find the probability of collision between two trucks.

Examples:

Input: S = “TCCBCTTB”, T = “BTCCBBTT”
Output: 0.194444
Explanation:
Total collision = 7
Total accident = 36
Therefore, the probability can be calculated by 7/36 = 0.19444.

Input: S = “BTT”, T = “BTCBT”
Output: 0.25000
"""

def get_total_truck(ip_str):
    count = 0
    for c in ip_str:
        if c == 'T' or c == 't':
            count+=1
    return count

def get_collision_accident_count(s_str, t_str):
    collision, accident = 0, 0
    l1 = len(s_str)
    l2 = len(t_str)
    total_truck = get_total_truck(t_str)
    print(collision, accident, total_truck)
    for i in range(l1 if l1<l2 else l2):
        if s_str[i] == 't' or s_str[i] == 'T':
            collision += total_truck
        accident += (l2-i)
        if t_str[i] == 't' or t_str[i] == 'T':
            total_truck -= 1
    print(collision, accident, total_truck)
    return collision, accident


def get_collision_probability(s, t):
    collision, accident = get_collision_accident_count(s, t)
    if accident == 0:
        return 0
    return collision/accident


def main():
    s = 'BTT'
    t = 'BTCBT'
    print('S>', s)
    print('T>', t)
    print('Collision Probability =', get_collision_probability(s, t))


if __name__ == '__main__':
    main()
