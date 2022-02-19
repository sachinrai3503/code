# https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/
# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
"""
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i])
 where S[i] is the start time of meeting i and F[i] is finish time of meeting i.
The task is to find the maximum number of meetings that can be accommodated in the
 meeting room. Print all meeting numbers

Examples: 
Attention reader! Don’t stop learning now. Get hold of all the important DSA concepts
 with the DSA Self Paced Course at a student-friendly price and become industry ready.
To complete your preparation from learning a language to DS Algo and many more,  
 please refer Complete Interview Preparation Course.

In case you wish to attend live classes with experts, please refer DSA Live Classes for
 Working Professionals and Competitive Programming Live for Students.

Input : s[] = {1, 3, 0, 5, 8, 5}, f[] = {2, 4, 6, 7, 9, 9} 
Output : 1 2 4 5 
First meeting [1, 2] 
Second meeting [3, 4] 
Fourth meeting [5, 7] 
Fifth meeting [8, 9]

Input : s[] = {75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924}, 
f[] = {112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252 } 
Output : 6 7 1 
"""

def get_max_meeting(start:list, end:list):
    length = len(start)
    timings = [[start[i], end[i]] for i in range(length)]
    timings.sort(key = lambda x : x[1])
    meeting = list()
    last_end_time = -1
    for timing  in timings:
        if timing[0]>=last_end_time:
            meeting.append(timing)
            last_end_time = timing[1]
    return meeting

def main():
    start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
    meetings = get_max_meeting(start, end)
    print(meetings)

if __name__ == '__main__':
    main()