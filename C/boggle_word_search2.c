// https://leetcode.com/problems/word-search/
/*
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 

word = "ABCCED"
Output: true
*/

#include <malloc.h>
#include <string.h>
#include <stdio.h>
#define false 0
#define true 1

typedef int bool;


int adj[2][4] = {{0,0,-1,1},{1,-1,0,0}};

void set2DArr(bool (*ip)[200], int row, int col){
    int i = 0;
    for(;i<row;i++){
        int j = 0;
        for(;j<col;j++){
            ip[i][j] = false;
        }
    }
}

bool isValid(char **ip, int i, int j, int row, int col, bool (*visited)[200], char c){
    if(i<0 || i>=row || j<0 || j>=col) return false;
    if((visited && visited[i][j]) || ip[i][j]!=c) return false;
    return true;
}

bool search(char **ip, int row, int col, int i, int j, char *word, int index, bool (*visited)[200]){
    if(index==strlen(word)) return true;
    if(!isValid(ip,i,j,row,col,visited,word[index])) return false;    
    visited[i][j] = true;
    int k = 0;
    for(;k<4;k++){
        int ti = i+adj[0][k];
        int tj = j+adj[1][k];
        bool result = search(ip,row,col,ti,tj,word,index+1,visited);
        if(result) return true;
    }
    visited[i][j] = false;
    return false;
}

bool exist(char** board, int boardSize, int* boardColSize, char * word){
    bool visited[200][200];
    set2DArr(visited,boardSize, *boardColSize);
    int i = 0;
    for(;i<boardSize;i++){
        int j = 0;
        for(;j<*boardColSize;j++){
            if(board[i][j] == word[0]){
                bool result = search(board,boardSize,*boardColSize,i,j,word,0,visited);
                if(result) return result;
            }
        }
    }
    return false;
}