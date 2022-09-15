// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
// https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/
// https://www.geeksforgeeks.org/find-k-pairs-smallest-sums-two-arrays/
/*
 You are given two integer arrays nums1 and nums2 sorted in ascending order and
  an integer k.

Define a pair (u, v) which consists of one element from the first array and one 
 element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],
 [7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],
 [2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:
1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 104
*/

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.HashSet;

public class ArrFindKPairSmallestSums {
    
    // This is not very efficient
    public List<List<Integer>> kSmallestPairs1(int[] nums1, int[] nums2, int k) {
        class Info implements Comparable<Info>{
            int i,j;
            Info(int i, int j){
                this.i = i;
                this.j = j;
            }

            @Override
            public int compareTo(Info obj){
                int this_sum = nums1[this.i] + nums2[this.j];
                int obj_sum = nums1[obj.i] + nums2[obj.j];
                if(this_sum>obj_sum) return 1;
                if(this_sum<obj_sum) return -1;
                return 0;
            }
            
            @Override
            public String toString(){
                return new String(this.i + "" + this.j);
            }
            
        }
        int len1 = nums1.length;
        int len2 = nums2.length;
        PriorityQueue<Info> que = new PriorityQueue<Info>();
        HashSet<String> set = new HashSet<String>();
        que.add(new Info(0,0));
        set.add("0:0");
        List<List<Integer>> op = new ArrayList<List<Integer>>();
        int i = 0;
        for(;i<k && !que.isEmpty();i++){
            Info info = que.poll();
            ArrayList<Integer> tOp = new ArrayList<Integer>();
            tOp.add(nums1[info.i]);
            tOp.add(nums2[info.j]);
            op.add(tOp);
            String nextPair1 = (info.i+1) + ":" + info.j;
            String nextPair2 = info.i + ":" + (info.j+1);
            if(info.i+1<len1 && set.contains(nextPair1)==false) {
                que.add(new Info(info.i+1, info.j));
                set.add(nextPair1);
            }
            if(info.j+1<len2 && set.contains(nextPair2)==false) {
                que.add(new Info(info.i, info.j+1));
                set.add(nextPair2);
            }
            // System.out.println(que);
        }
        // System.out.println(set);
        return op;
    }
    
    // Will solve it without using set
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        class Info implements Comparable<Info>{
            int i,j;
            Info(int i, int j){
                this.i = i;
                this.j = j;
            }

            @Override
            public int compareTo(Info obj){
                int this_sum = nums1[this.i] + nums2[this.j];
                int obj_sum = nums1[obj.i] + nums2[obj.j];
                if(this_sum>obj_sum) return 1;
                if(this_sum<obj_sum) return -1;
                return 0;
            }
            
            @Override
            public String toString(){
                return new String(this.i + "" + this.j);
            }
            
        }
        int len1 = nums1.length;
        int len2 = nums2.length;
        PriorityQueue<Info> que = new PriorityQueue<Info>();
        for(int i=0;i<len1;i++) que.add(new Info(i,0));
        List<List<Integer>> op = new ArrayList<List<Integer>>();
        int i = 0;
        while(i<k && !que.isEmpty()){
            Info info = que.poll();
            ArrayList<Integer> tOp = new ArrayList<Integer>();
            tOp.add(nums1[info.i]);
            tOp.add(nums2[info.j]);
            op.add(tOp);
            i++;
            int next_j = info.j+1;
            if(next_j==len2) continue;
            que.add(new Info(info.i, next_j));
            // System.out.println(que);
        }
        // System.out.println(set);
        return op;
    }
    
}