// https://www.geeksforgeeks.org/minimum-number-of-rabbits-that-must-be-present-in-the-forest/
// https://leetcode.com/problems/rabbits-in-forest/
/*
In a forest, each rabbit has some color. Some subset of rabbits 
 (possibly all of them) tell you how many other rabbits have the same color as
 them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:

Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0

Note:
answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
*/


int* get_freq(int range, int *ip, int length){
    int *freq = (int*)calloc(range, sizeof(int));
    int i = 0;
    for(;i<length;i++){
        freq[ip[i]]++;
    }
    return freq;
}

int numRabbits(int* answers, int answersSize){
    int count = 0;
    int range = 1000;
    int *freq = get_freq(range, answers, answersSize);
    int i = 0;
    for(;i<range;i++){
        if(freq[i]!=0){
            int quo = freq[i]/(i+1);
            int rem = freq[i]%(i+1);
            count = count + (quo*(i+1));
            if(rem) count+=(i+1);
        }
    }
    return count;
}