//  https://www.lintcode.com/problem/907/
/*
Description
Given a non-empty string s and an integer k, rearrange the string such that the
 same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange
 the string, return an empty string "".

Example
Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation:
The same letters are at least distance 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation:
It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "bacabcd"
Explanation:
Another possible answer is: "abcabcda"
The same letters are at least distance 2 from each other.
*/

import java.util.Iterator;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.HashMap;

class Info implements Comparable<Info>{

    char c;
    int count;

    Info(char c, int count){
        this.c = c;
        this.count = count;
    }

    @Override
    public int compareTo(Info obj){
        if(this.count>obj.count) return -1;
        if(this.count<obj.count) return 1;
        return 0;
    }

    @Override
    public String toString(){
        return new String(c + " " + count);
    }

}

public class list_rearrange_str_such_that_each_char_is_k_dist_apart {
    /**
     * @param s: a string
     * @param k: an integer
     * @return: a string such that the same characters are at least distance k from each other
     */
    public String rearrangeString(String s, int k) {
        int sLen = s.length();
        if(sLen==0) return "";
        HashMap<Character, Integer> countMap = new HashMap<Character, Integer>();
        PriorityQueue<Info> heap = new PriorityQueue<Info>();
        for(int i=0;i<sLen;i++){
            char c = s.charAt(i);
            if(countMap.containsKey(c)){
                countMap.put(c, countMap.get(c) + 1);
            }else{
                countMap.put(c, 1);
            }
        }
        // System.out.println(countMap);
        Iterator<Entry<Character, Integer>> it = countMap.entrySet().iterator();
        while(it.hasNext()){
            Entry<Character, Integer> et = it.next();
            heap.add(new Info(et.getKey(), et.getValue()));
        }
        // System.out.println(heap);
        int maxCharCount = heap.peek().count;
        // System.out.println(maxCharCount + " :: " + (sLen/k + ((sLen%k!=0)?1:0)));
        if(maxCharCount>(sLen/k + ((sLen%k!=0)?1:0))) return "";
        char[] op = new char[sLen];
        int i = 0;
        int j = 0;
        while(!heap.isEmpty()){
            Info tInfo = heap.poll();
            while(tInfo.count>0){
                op[j] = tInfo.c;
                j+=k;
                if(j>=sLen){
                    i+=1;
                    j=i;
                }
                tInfo.count-=1;
            }
        }
        // System.out.println(op);
        return new String(op);
    }
}