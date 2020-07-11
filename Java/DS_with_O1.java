import java.util.HashMap;
import java.util.Random;

/**
* DS to insert,delete,search and getRandom in O(1) time.
*/
class DataStructure{

    private HashMap<Integer,MapValue> map = null;
    private Integer[] data = null;
    final private int maxSize;
    private int currentIndex;

    private class MapValue{
        int positionIndex;
        int count;

        MapValue(int positionIndex, int count){
            this.positionIndex = positionIndex;
            this.count = count;
        }
    }

    public DataStructure(int maxSize){
        this.maxSize = maxSize;
        this.currentIndex = -1;
        this.data = new Integer[maxSize];
        this.map = new HashMap<Integer,MapValue>();
    }

    public boolean isEmpty(){
        if(this.currentIndex==-1) return true;
        return false;
    }

    public boolean isFull(){
        if(this.currentIndex==this.maxSize-1) return true;
        return false;
    }

    public int search(int data){
        if(this.map.containsKey(data)) return this.map.get(data).positionIndex;
        return -1;
    }

    public void insert(int data){
        if(isFull()){
            System.out.println("Full : Can't insert");
        }else{
            if(this.map.containsKey(data)) map.get(data).count++;
            else{   
                this.map.put(data,new MapValue(currentIndex+1,1));
                this.data[++currentIndex] = data;
            }
        }
    }

    public int delete(int data){
        if(isEmpty()){
            System.out.println("Empty\n");
            return -1;
        }
        if(search(data)==-1){
            System.out.println(data + " not present.");
            return -1;
        }
        MapValue value = this.map.get(data);
        value.count--;
        if(value.count==0){
            this.data[value.positionIndex] = this.data[this.currentIndex];
            this.map.get(this.data[value.positionIndex]).positionIndex = value.positionIndex;
            this.map.remove(data);
            this.currentIndex--;
        }
        return value.positionIndex;
    }

    public int getRandom(){
        if(isEmpty()){
            System.out.println("Empty");
            return -1;
        }
        return this.data[new Random().nextInt(this.currentIndex+1)];
    }

    public void print(){
        for(int i=0;i<=this.currentIndex;i++){
            System.out.print(data[i] + " ");
        }
        System.out.println();
    }
}

public class DS_with_O1 {
    public static void main(String[] args) {
        
        int[] insert = {1,2,3,4,5,6,7,8,9,4,5,10,1,3,3,2,5,6,7};
        int[] search = {1000,4,1,7,5,3};
        int[] delete = {1000,9,1,6,3,6,1};
        int[] search2 = {1000,4,1,7,5,3,6};

        DataStructure ds = new DataStructure(100);
 
        for(int i:insert){
            System.out.println("Inserted " + i);
            ds.insert(i);
        }

        System.out.print("DS = " );
        ds.print();

        for(int i:search){
            System.out.println(i + " is at: "  + ds.search(i));
        }

        for(int i:delete){
            System.out.println("Deleted "+i+" from " + ds.delete(i));
        }

        System.out.print("DS = " );
        ds.print();

        for(int i:search2){
            System.out.println(i + " is at: "  +  ds.search(i));
        }


        for(int i=0; i<5;i++){
            System.out.println("Random at : " + ds.getRandom());
        }
    }
}