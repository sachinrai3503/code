import java.util.PriorityQueue;

class Range implements Comparable<Range>{
    int i, j;

    public Range(int i, int j){
        this.i = i;
        this.j = j;
    }

    @Override
    public int compareTo(Range range) {
        if(this.i<range.i) return -1;
        if(this.i>range.i) return 1;
        return 0;
    }

    public boolean isValid(){
        if(this.i<=this.j){
            return true;
        }
        return false;
    }

}

public class ArrKthSmallestElementFromArrOfIntervals {
    static int getKthSmallestElement(Range[] ranges, int k){
        PriorityQueue<Range> pq = new PriorityQueue<Range>();
        for(int i = 0;i<ranges.length;i++){
            if(ranges[i].isValid())
                pq.add(ranges[i]);
        }
        int lastElement = Integer.MIN_VALUE;
        int count = 0;
        while(!pq.isEmpty() && count<k){
            Range temp = pq.poll();
            lastElement = temp.i;
            temp.i++;
            if(temp.isValid()) pq.add(temp);
            count++;
        }
        if(count==k) return lastElement;
        return Integer.MIN_VALUE;
    }
    
    public static void main(String[] args) {
        int[][] ip = {{5, 11}, {10, 15}, {12, 20}};
        int k = 7;
        Range[] ranges = new Range[ip.length];
        int i = 0;
        for(;i<ip.length;i++){
            ranges[i] = new Range(ip[i][0],ip[i][1]);
        }
        System.out.println(k + " th smallest element = " + 
                           getKthSmallestElement(ranges,k));
    }   
}