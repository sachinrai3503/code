// https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/
/*
Given an unsorted array and two numbers x and k, find k closest values to x.

Examples:

Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 
Output : 4 6 7
Three closest values of x are 4, 6 and 7.

Input : arr[] = {-10, -50, 20, 17, 80}, x = 20, k = 2
Output : 17, 20 
*/

// C heap based sol. - arr_k_nearest_num.c

import java.util.PriorityQueue;

class ElementInfo implements Comparable<ElementInfo> {
    private int data;
    private int diff;

    public ElementInfo(int data, int diff) {
        this.data = data;
        this.diff = diff;
    }

    @Override
    public int compareTo(ElementInfo element) {
        if (this.diff > element.diff)
            return -1;
        if (this.diff < element.diff)
            return 1;
        return 0;
    }

    @Override
    public String toString() {
        return new String("(" + this.data + "::" + this.diff + ")");
    }
}

public class ArrKClosestNum {

    public static void printArr(int[] ip) {
        for (int num : ip) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public int getDiff(int a, int b) {
        if (a > b)
            return a - b;
        return b - a;
    }

    public PriorityQueue<ElementInfo> getKClosestElement(int[] ip, int k, int x) {
        PriorityQueue<ElementInfo> pq = new PriorityQueue<ElementInfo>();
        if (k <= 0)
            return pq;
        for (int i = 0; i < ip.length; i++) {
            ElementInfo info = new ElementInfo(ip[i], getDiff(x, ip[i]));
            if (pq.size() < k) {
                pq.add(info);
            } else {
                if (info.compareTo(pq.peek()) == 1) {
                    pq.poll();
                    pq.add(info);
                }
            }
        }
        return pq;
    }

    public static void main(String[] args) {
        int[] ip = { -10, -50, 20, 17, 80 };
        int k = 2;
        int x = 20;

        printArr(ip);
        System.out.println("X=" + x + " K=" + k);
        PriorityQueue<ElementInfo> pq = new ArrKClosestNum().
                                        getKClosestElement(ip, k, x);
        while(pq.size()!=0){
            System.out.println(pq.poll());
        }
    }
}
