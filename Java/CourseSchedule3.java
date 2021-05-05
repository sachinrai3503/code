// https://leetcode.com/problems/course-schedule-iii/
/*
There are n different online courses numbered from 1 to n. Each course has some
 duration(course length) t and closed on dth day. A course should be taken
 continuously for t days and must be finished before or on the dth day.
 You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the
 maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
*/

// This method has Time O(nlogn). Space - O(n)
// For DP based sol. course_schedule3.c

/*
IMP Test cases - 
[[2,5],[2,19],[1,8],[1,3]] -- This test cases shows why sorting is needed.
[[100,200],[200,1300],[1000,1250],[2000,3200]]
[[100,200],[500,800],[900,1000],[200,300],[50,600]]
[[7,11],[1,11],[1,3],[2,6],[5,6],[7,7],[4,8],[2,20],[1,17],[8,11]]
*/
import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.Collections;

public class CourseSchedule3 {
    public int scheduleCourse(int[][] courses) {
        PriorityQueue<Integer> que = new PriorityQueue<Integer>(Collections.reverseOrder());
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        int cur_time = 0;
        int length = courses.length;
        for(int i = 0; i<length; i++){
            int duration = courses[i][0];
            if(cur_time+courses[i][0]<=courses[i][1]){
                que.add(duration);
                cur_time+=duration;
            }else if(!que.isEmpty() && que.peek()>duration){
                cur_time = cur_time - que.poll() + duration;
                que.add(duration);
            }
        }
        return que.size();
    }
}