// https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
/*
Given a dictionary, and two words ‘start’ and ‘target’ (both of same length).
Find length of the smallest chain from ‘start’ to ‘target’ if it exists, 
such that adjacent words in the chain only differ by one character and each word 
in the chain is a valid word i.e., it exists in the dictionary. 

It may be assumed that the ‘target’ word exists in dictionary and length of 
all dictionary words is same.
Example:
Input: Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}
       start = TOON
       target = PLEA
Output: 7
TOON - POON - POIN - POIE - PLIE - PLEE - PLEA

Input: Dictionary = {ABCD, EBAD, EBCD, XYZA}
       Start = ABCV
       End = EBAD
Output: 4
ABCV - ABCD - EBCD - EBAD
*/

import java.util.TreeSet;
import java.util.ArrayList;

public class WordLadder{

    int getLadderLength(String start, String dest, TreeSet<String> dict){
        if(start==null || dest==null) {
            System.out.println("Invalid");
            return Integer.MAX_VALUE;
        }
        if(start.equals(dest)) return 1;
        ArrayList<String> que = new ArrayList<String>();
        String nullString = "";
        que.add(start);
        que.add(nullString);
        int length = 1;
        while(!que.isEmpty() && que.get(0).equals(nullString)==false){
            while(!que.isEmpty() && que.get(0).equals(nullString)==false){
                String temp = que.remove(0);
                char[] temp_arr = temp.toCharArray();
                int temp_len = temp.length();
                for(int i=0;i<temp_len;i++){
                    char c = temp_arr[i];
                    for(int j=0;j<26;j++){
                        if(j!=c-97){
                            temp_arr[i] = (char)(j+97);
                            String s = new String(temp_arr);
                            if(dict.contains(s)){
                                if(s.equals(dest)) return length+1;
                                dict.remove(s);
                                que.add(s);
                            }
                        }
                    }
                    temp_arr[i] = c;
                }
            }
            if(!que.isEmpty())  que.remove(0);
            que.add(nullString);
            length++;
        }
        return Integer.MAX_VALUE;
    }

    public static void main(String[] args) {
        String[] dictArr = {"hot","dot","dog","lot","log"};
        String start = "hot";
        String dest = "log";

        TreeSet<String> dict = new TreeSet<String>();
        for(String s : dictArr){
            dict.add(s);
        }
        System.out.println("length="+new WordLadder().getLadderLength(start, dest, dict));
    }
}