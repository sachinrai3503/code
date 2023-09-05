// https://leetcode.com/problems/reverse-words-in-a-string
/*
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be 
 separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between 
 two words. The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single
 space in the reversed string.

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve 
 it in-place with O(1) extra space?
*/

#include<stdio.h>
#include<stdbool.h>

void swap(char *a, char *b){
    char c = *a;
    *a = *b;
    *b = c;
}

void reverse_string(char *s, int s_len){
    int i = 0, j = s_len-1;
    while(i<j){
        swap(s+i, s+j);
        i++;
        j--;
    }
}

void reverse_words(char *s, int s_len){
    if(s==NULL || s_len<=0) return;
    int i = 0, j = 0;
    while(j<s_len){
        if(s[j]==' '){
            reverse_string(s+i, j-i);
            i = ++j;
        }else{
            j++;
        }
    }
    reverse_string(s+i, j-i);
}

char* remove_extra_spaces(char *s, int s_len){
    int i = 0;
    int j = 0;
    bool has_word = false;
    int t = s_len-1;
    while(t>=0 && s[t]==' ') t--;
    while(j<=t){
        if(s[j]==' '){
            if(has_word){
                i++;
                j++;
            }else{
                j++;
            }
            has_word = false;
        }else{
            swap(s+i, s+j);
            i++;
            j++;
            has_word = true;
        }
    }
    s[i] = '\0';
    // printf("%s\n",s);
    return s;
}

char * reverseWords(char * s){
    int s_len = strlen(s);
    char *t_s = remove_extra_spaces(s, s_len);
    int t_s_len = strlen(t_s);
    reverse_words(t_s, t_s_len);
    reverse_string(t_s, t_s_len);
    return t_s;
}