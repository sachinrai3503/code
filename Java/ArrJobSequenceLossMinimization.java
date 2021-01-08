// https://www.geeksforgeeks.org/job-sequencing-problem-loss-minimization/
/*
We are given N jobs numbered 1 to N. For each activity, let Ti denotes the
 number of days required to complete the job. For each day of delay before
 starting to work for job i, a loss of Li is incurred.

We are required to find a sequence to complete the jobs so that overall loss
 is minimized. We can only work on one job at a time.

If multiple such solutions are possible, then we are required to give the
 lexicographically least permutation (i.e earliest in dictionary order).

Examples:
Input : L = {3, 1, 2, 4} and 
        T = {4, 1000, 2, 5}
Output : 3, 4, 1, 2
Explanation: We should first complete 
job 3, then jobs 4, 1, 2 respectively.

Input : L = {1, 2, 3, 5, 6} 
        T = {2, 4, 1, 3, 2}
Output : 3, 5, 4, 1, 2 
Explanation: We should complete jobs 
3, 5, 4, 1 and then 2 in this order.
*/

import java.util.Collections;
import java.util.ArrayList;

class Job implements Comparable<Job>{
    int days, loss;
    int id;
    private static int count;

    static{
        count = 0;
    }

    public Job(int days, int loss){
        this.id = ++Job.count;
        this.days = days;
        this.loss = loss;
    }

    @Override
    public int compareTo(Job job){
        int t1 = this.loss * job.days;
        int t2 = job.loss * this.days;
        if(t1<t2){
            return 1;
        }else if(t1>t2) return -1;
        return 0;
    }

    @Override
    public String toString(){
        return "(" + this.id + "-" + this.days + "-" + this.loss + ")";
    }
}

public class ArrJobSequenceLossMinimization {
    
    public static void printJobs(ArrayList<Job> jobs){
        for(int i = 0;i<jobs.size();i++){
            System.out.print(jobs.get(i));
        }
        System.out.println();
    }

    public static int getJobSeqWithMinLoss(ArrayList<Job> jobs){
        if(jobs.size()==0) return 0;
        int loss = 0;
        Collections.sort(jobs);
        int totalLoss = 0;
        for(Job job : jobs)
            totalLoss+=job.loss;
        for(Job job : jobs){
            totalLoss-=job.loss;
            loss = loss + (totalLoss*job.days);
        }
        return loss;
    }

    public static void main(String[] args) {
        int T[] = {2, 4, 1, 3, 2};
        int L[] = {1, 2, 3, 5, 6};
        int length = T.length;
        ArrayList<Job> jobs = new ArrayList<Job>();
        for(int i = 0;i<length;i++){
            jobs.add(new Job(T[i],L[i]));
        }
        printJobs(jobs);
        int minLoss = getJobSeqWithMinLoss(jobs);
        System.out.println("Min loss = " + minLoss);
        printJobs(jobs);
    }
}