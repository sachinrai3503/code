// https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
/**
 * 
 * Given an array of words, print all anagrams together.
 *  For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”},
 *  then output may be “cat tac act dog god”.
 */

//  Here the solution uses only HashMap to solve in O(N*M) time.
//  Let there be N words and each word has maximum M characters

// For sorting based solution see - string_print_all_anagram_together.c
// For sort & dict based solution see dict_group_anagrams.py.

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>,ArrayList<String>> map = new HashMap<HashMap<Character, Integer>,ArrayList<String>>();
        for(String word : strs){
            HashMap<Character, Integer> countMap = new HashMap<Character, Integer>();
            for(int i = 0;i<word.length();i++){
                char c = word.charAt(i);
                if(countMap.containsKey(c)){
                    int count = countMap.get(c);
                    countMap.put(c,count+1);
                }else{
                    countMap.put(c,1);                    
                }
            }
            if(map.containsKey(countMap)){
                map.get(countMap).add(word);
            }else{
                ArrayList<String> list = new ArrayList<String>();
                list.add(word);
                map.put(countMap,list);
            }
        }
        List<List<String>> anagramList = new ArrayList<List<String>>();
        Iterator<Entry<HashMap<Character,Integer>,ArrayList<String>>> it = map.entrySet().iterator();
        while(it.hasNext()){
            Entry<HashMap<Character,Integer>,ArrayList<String>> entry = it.next();
            anagramList.add(entry.getValue());
        }
        // System.out.println(anagramList);
        return anagramList;
    }
}