// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
/*
You are given two integer arrays nums1 and nums2 sorted in ascending order and 
 an integer k.

Define a pair (u,v) which consists of one element from the first array and one
 element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
*/

import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Pair implements Comparable<Pair>{
    int i;
    int j;
    int sum;
    
    static int[] l1;
    static int[] l2;
    
    static void setArrays(int[] l1, int[] l2){
        Pair.l1 = l1;
        Pair.l2 = l2;
    }
    
    Pair(int i, int j){
        this.i = i;
        this.j = j;
        this.sum = Pair.l1[i] + Pair.l2[j];
    }
    
    @Override
    public String toString(){
        return "("+ i + " " + j +")";
    }
    
    @Override
    public int compareTo(Pair pair){
        if(this.sum<pair.sum) return -1;
        if(this.sum>pair.sum) return 1;
        return 0;
    }
    
}

public class ArrFindKPairWithSmallestSum {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        Pair.setArrays(nums1, nums2);
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        boolean[][] visited = new boolean[nums1.length][nums2.length];
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        if(nums1.length>0 && nums2.length>0){
            pq.add(new Pair(0,0));
            visited[0][0] = true;
        }
        int count = 0;
        while(count<k && !pq.isEmpty()){
            Pair tPair = pq.poll();
            ArrayList<Integer> tList = new ArrayList<Integer>();
            tList.add(nums1[tPair.i]);
            tList.add(nums2[tPair.j]);
            list.add(tList);
            if(tPair.i<nums1.length-1 && !visited[tPair.i+1][tPair.j]){
                pq.add(new Pair(tPair.i+1, tPair.j));
                visited[tPair.i+1][tPair.j] = true;
            }
            if(tPair.j<nums2.length-1 && !visited[tPair.i][tPair.j+1]){
                 pq.add(new Pair(tPair.i, tPair.j+1));
                 visited[tPair.i][tPair.j+1] = true;
            }
            count++;
        }
        return list;
    }
}