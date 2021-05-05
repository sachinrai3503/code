// https://www.geeksforgeeks.org/queue-based-approach-for-first-non-repeating-character-in-a-stream/
/*
Given a stream of characters, find the first non-repeating character from stream.
You need to tell the first non-repeating character in O(1) time at any moment.
*/

// For DLL based see - DLL_1st_unique_char_in_stream_of_chars.c

import java.util.LinkedList;
import java.util.Queue;

public class Queue1stUniqueCharInStreamOfChars{

    static void getUniqueChars(String s){
        Queue<Character> que = new LinkedList<Character>();
        int[] count = new int[26];
        for(int i = 0; i<s.length();i++){
            count[s.charAt(i)-97]++;
            if(count[s.charAt(i)-97]==1){
                que.add(s.charAt(i));
            }
            while(que.isEmpty()==false && count[que.peek()-97]>1){
                que.poll();
            }
            if(que.isEmpty()) System.out.println(-1);
            else System.out.println(que.peek());
        }
    }

    public static void main(String[] args){
        String s = "geekforgeekandgeeksandquizfor";
        System.out.println("Ip>" + s);
        Queue1stUniqueCharInStreamOfChars.getUniqueChars(s);
    }
}