import java.lang.Math;

interface SegementTreeOperation{
    int queryIndexRange(int i, int j);
    void updateIndex(int index, int value);
    int operate(int a, int b);
    int getNodeValue(int index);
}

abstract class SegmentTree implements SegementTreeOperation{

    public int[] ip;
    public int ipLen;
    public int[] treeArr;
    public int treeArrLen;

    public SegmentTree(int[] ip, int length){
        this.ip = ip;
        this.ipLen = length;
        int x = (int)Math.ceil(Math.log(length)/Math.log(2));
        int size = 2*((int)Math.pow(2,x))- 1;
        if(size<0) size = 0;
        this.treeArr = new int[size];
        this.treeArrLen = size;
        constructSegmentTree(ip,0,length-1,0);
    }

    private void constructSegmentTree(int[] ip, int s, int e, int index){
        if(s>e) return;
        if(s==e) this.treeArr[index] = ip[s];
        else{
            int mid = s + (e-s)/2;
            constructSegmentTree(ip,s,mid,index*2+1);
            constructSegmentTree(ip,mid+1,e,index*2+2);
            this.treeArr[index] = getNodeValue(index);
        }
    }

    private int query(int index, int s, int e, int i, int j){
        if(s<0 || e>=this.ipLen || i<0 || j>=this.ipLen) 
            return Integer.MIN_VALUE;
        if(s>e || i>j || j<s || i>e) return Integer.MIN_VALUE;
        if(i==s && j==e) return this.treeArr[index];
        int mid = s + (e-s)/2;
        if(j<=mid) return query(index*2+1, s, mid, i, j);
        else if(i>mid) return query(index*2+2, mid+1, e, i, j);
        else{
            return operate(query(index*2+1, s, mid, i, mid),
                            query(index*2+2, mid+1, e, mid+1, j));
        }
    }

    @Override
    public int queryIndexRange(int i, int j){
        return query(0,0,this.ipLen-1,i,j);
    }

    private void update(int treeNodeIndex, int s, int e, int arrIndex, int value)
    {
        if(s<0 || e>=this.ipLen) return;
        if(arrIndex<s || arrIndex>e) return;
        if(s==e){
            this.ip[arrIndex] = value;
            this.treeArr[treeNodeIndex] = value;
            return;
        }
        int mid = s + (e-s)/2;
        if(arrIndex<=mid) 
            update(treeNodeIndex*2+1, s, mid, arrIndex, value);
        else if(arrIndex>mid)
            update(treeNodeIndex*2+2, mid+1, e, arrIndex, value);
        this.treeArr[treeNodeIndex] = getNodeValue(treeNodeIndex);
    }

    @Override
    public void updateIndex(int index, int value){
        update(0,0,this.ipLen-1, index, value);
    }
}

class SumSegmentTree extends SegmentTree{

    public SumSegmentTree(int[] ip, int length){
        super(ip,length);
    }

    @Override
    public int operate(int a, int b) {
        return a + b;
    }

    @Override
    public int getNodeValue(int index) {
        return operate(this.treeArr[index*2+1],this.treeArr[index*2+2]);
    }
}

class MaxSegmentTree extends SegmentTree{
    
    public MaxSegmentTree(int[] ip, int length){
        super(ip,length);
    }

    @Override
    public int operate(int a, int b) {
        if(a>b) return a;
        return b;
    }

    @Override
    public int getNodeValue(int index) {
        return operate(this.treeArr[index*2+1],this.treeArr[index*2+2]);
    }
}

public class SegmentTreeMultiType {

    public static void printArr(int[] ip, int length){
        int i = 0;
        for(;i<length;i++){
            System.out.print(ip[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] ip = {1, 3, 5, 7, 9, 11};
        int length = ip.length;
        System.out.print("Ip>>");
        printArr(ip,length);
        // All of the are indexs below
        int i = 2;
        int j = 5;
        int updateIndex = 2;
        int value = 17;


        // System.out.println("=======Sum Segment Tree===========");
        // SumSegmentTree sumTree = new SumSegmentTree(ip, length);
        // System.out.print("Sum Segement Tree >>");
        // printArr(sumTree.treeArr, sumTree.treeArrLen);
        // System.out.println("Query sum betn "+i+":"+j+"=" + 
        //                     sumTree.queryIndexRange(i, j));
        // sumTree.updateIndex(updateIndex, value);
        // System.out.println("After update Query sum betn "+i+":"+j+"=" + 
        //                     sumTree.queryIndexRange(i, j));
        // System.out.print("Sum Segement Tree >>");
        // printArr(sumTree.treeArr, sumTree.treeArrLen);

        System.out.println("=======Max Segment Tree===========");
        MaxSegmentTree maxTree = new MaxSegmentTree(ip, length);
        System.out.print("Max Segement Tree >>");
        printArr(maxTree.treeArr, maxTree.treeArrLen);
        System.out.println("Query max betn " + i + ":" + j + "=" + 
                            maxTree.queryIndexRange(i, j));
        maxTree.updateIndex(updateIndex, value);
        System.out.println("After update Query max betn " + i + ":" + j + "=" +
                            maxTree.queryIndexRange(i, j));
        System.out.print("Max Segement Tree >>");
        printArr(maxTree.treeArr, maxTree.treeArrLen);
    }
}