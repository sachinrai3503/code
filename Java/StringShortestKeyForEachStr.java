import java.util.ArrayList;
import java.util.Collections;

// https://www.geeksforgeeks.org/find-shortest-unique-prefix-every-word-given-list-set-2-using-sorting/
/*
Given an array of words, 
find all shortest unique prefixes to represent 
each word in the given array. 

Assume that no word is a prefix of another. 
Output the shortest unique prefixes in sorted order.

Input  : {"zebra", "dog", "duck", "dove"}
Output : z, dog, dov, du

Input: {"geeksgeeks", "geeksquiz", "geeksforgeeks"}
Output: geeksf, geeksg, geeksq
*/

// Trie based solution in c :: trie_string_shortest_key_for_each_str.c

class WordKey implements Comparable<WordKey>{
    String word;
    String key;

    WordKey(String word){
        this.word = word;
    }

    WordKey(String word, String key){
        this.word = word;
        this.key = key;
    }

    void updateKey(String newKey){
        if(this.key==null || this.key.length()<newKey.length()){
            this.key = newKey;
        }
    }

    void appendKeyWith(char c){
        if(this.key==null){
            this.key = "";
        }
        this.key+=c;
    }

    void appendKeyWith(String str){
        this.key+=str;
    }

    @Override
    public int compareTo(WordKey wk){
        String tKey1 = "";
        String tKey2 = "";
        String s1 = this.word;
        String s2 = wk.word;
        int l1 = s1.length();
        int l2 = s2.length();
        int i = 0, j = 0;
        for(;i<l1 && j<l2;i++,j++){
            tKey1+=s1.charAt(i);
            tKey2+=s2.charAt(j);
            if(s1.charAt(i)!=s2.charAt(j)) break;
        }
        this.updateKey(tKey1);
        wk.updateKey(tKey2);
        if(i==l1 && j==l2){
            return 0;
        }else if(i==l1){
            tKey2+=s2.charAt(j);
            wk.updateKey(tKey2);
            return -1;
        }else if(j==l2){
            tKey1+=s1.charAt(i);
            this.updateKey(tKey1);
            return 1;
        }
        if(s1.charAt(i)<s2.charAt(j)) return -1;
        return 1;
    }

    public String toString(){
        return this.word + "::" + this.key;
    }
}

public class StringShortestKeyForEachStr {

    static ArrayList<WordKey> initList(String[] arr){
        ArrayList<WordKey> list = new ArrayList<WordKey>();
        for(String str : arr){
            list.add(new WordKey(str));
        }
        return list;
    }

    public static void main(String[] args){
        String[] arr = {"dog", "monkey", "bucket", "bulk", "bully","bullyw",
             "bullyww", "bullywwzaq"};
        ArrayList<WordKey> word_list = initList(arr);
        System.out.println(word_list);
        Collections.sort(word_list);
        for(WordKey wk : word_list){
            System.out.println(wk.word + "::" + wk.key);
        }
    }
}