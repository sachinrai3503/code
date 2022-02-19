// https://www.geeksforgeeks.org/snake-ladder-problem-2/
// https://leetcode.com/problems/snakes-and-ladders/
/*
Given a snake and ladder board, find the minimum number of dice throws 
required to reach the destination or last cell from source or 1st cell.

Basically, the player has total control over outcome of dice throw and wants 
to find out minimum number of throws required to reach last cell.

If the player reaches a cell which is base of a ladder, the player has to climb 
up that ladder and if reaches a cell is mouth of the snake, has to go down to 
the tail of snake without a dice throw.

        25	26	27	28	29	30
        24	23	22	21	20	19
        13	14	15	16	17	18
        12	11	10	9	8	7
        1	2	3	4	5	6
					
 Ladder     	Snake		
From To 	   From	To	
 3 	22		    27	1	
 5	8		    21	9	
 11	26		    19	7	
 20	29		    17	4	

For example, consider the board shown, the minimum number of dice throws 
required to reach cell 30 from cell 1 is 3.
Following are the steps:

a) First throw two on dice to reach cell number 3 and then ladder to reach 22
b) Then throw 6 to reach 28.
c) Finally through 2 to reach 30.

There can be other solutions as well like (2, 2, 6), (2, 4, 4), (2, 3, 5).. etc.
*/

// NOTE - Check SnakeLadderProblem.py for better(correct) logic.
// Below implementation might not work in all the cases.

import java.util.ArrayList;

class SnakeLadder{

    private int[] shortcuts;
    private int lastCellNum;
    private int[] throwCount;

    public SnakeLadder(int lastCellNum){
        this.lastCellNum = lastCellNum;
        this.shortcuts = new int[lastCellNum];
        this.throwCount = new int[lastCellNum];
    }

    /**
     * Marks the final position upon encounting the ladder or snake.
     * @param to - 1 based position for starting of ladder or snake
     * @param from -  1 based final postion to land after climbing the ladder
     *  or sliding down the snake.
     */
    public void markShortcuts(int[] to, int[] from){
        for(int i=0;i<lastCellNum;i++)
            shortcuts[i] = -1;
        for(int i=0;i<to.length;i++){
            shortcuts[to[i]-1] = from[i]-1;
        }
    }

    /**
     * Adds the given index in the que to the rear end. While adding 
     * it removes any index from the rear end which has throwcount >= 
     * throwcount for given index.
     * 
     * @param que - que in which the index is being maintained.
     * @param index - 0 based index of the position to be inserted in the que.
     */
    private void checkAndAdd(ArrayList<Integer> que, int index){
        while(que.size()>0 && throwCount[que.get(que.size()-1)]>=
                                throwCount[index]){
            que.remove(que.size()-1);
        }
        que.add(index);
    }

    // private void printQue(ArrayList<Integer> que){
    //     for (Integer integer : que) {
    //         System.out.print(integer+" - "+throwCount[integer]+ " ");
    //     }
    //     System.out.println();
    // }

    /**
     * Returns the min number of throws needed to reach the 'to' from the 'from'
     * 
     * @param to - 1 based start position.
     * @param from - 1 based final position.
     * @throws Exception When invalid to and from position are given.
     */
    int getMinThrowsNeeded(int from, int to) throws Exception {
        if(to<from){
            throw new Exception("Invalid to and from passed.");
        }
        ArrayList<Integer> que = new ArrayList<Integer>();
        for(int i=to;i>=from;i--){
            int reqThrow = 0;
            if(i!=to){
                if(shortcuts[i-1]==-1)
                    reqThrow = throwCount[que.get(0)] + 1;
                else if(shortcuts[i-1]>i)
                    reqThrow = throwCount[shortcuts[i-1]];
                else
                    reqThrow = Integer.MAX_VALUE;
            }
            throwCount[i-1] = reqThrow;
            checkAndAdd(que,i-1);
            // printQue(que);
            if(que.isEmpty()==false && que.get(0)+1 > ((i-1)+6)){
                que.remove(0);
            }
            // printQue(que);
        }
        return throwCount[from-1];
    }
}

public class SnakeLadderProblem{
    public static void main(String[] args) throws Exception {
        int lastCellNum = 30;
        int from = 29;
        int to = 30;
        int[] shortcutsTo = {3,5,11,20,27,21,17,19,1};
        int[] shortcutsFrom = {22,8,26,29,1,0,4,7,30};
        SnakeLadder sl = new SnakeLadder(lastCellNum);
        sl.markShortcuts(shortcutsTo, shortcutsFrom);
        System.out.println("Min. throws needed from "+from+" to "+to+" = " + 
                sl.getMinThrowsNeeded(from, to));
    }
}