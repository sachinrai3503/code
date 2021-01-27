import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map.Entry;

class Candidate{
    String name;
    String area;
    int age;

    public Candidate(String name, String area, int age){
        this.name = name;
        this.age = age;
        this.area = area;
    }

    @Override
    public String toString(){
        return this.name + " " + this.area + " " + this.age;
    }

    @Override
    public boolean equals(Object obj){
        System.out.println("equals called for " + this + " :: " + obj);
        if(obj instanceof Candidate){
            Candidate candidate = (Candidate)obj;
            // if((this.name+this.area).equals(candidate.name+candidate.area)){
            //     return true;
            // }
            if((this.name+this.area).equals(candidate.name+candidate.area) && 
                this.age == candidate.age){
                    return true;
            }
        }
        return false;
    }

    @Override
    public int hashCode(){
        System.out.println("hashcode called for " + this);
        return (this.name+this.area).hashCode();
    }
}

public class HashMapHashSetInfo {

    static void addToHashMap(HashMap<Candidate, Integer> map, String[] names, String[] areas){
        for(int i = 0;i<names.length;i++){
            Candidate candidate = new Candidate(names[i], areas[i], i);
            boolean is_present = map.containsKey(candidate);
            System.out.println("Looked for is_present");
            if(is_present){
                System.out.println("Repeat occurance for " + candidate);
                int new_value = map.get(candidate)+1;
                System.out.println("Got new value");
                map.put(candidate,new_value);
            }else{
                System.out.println("First occurance for " + candidate);
                map.put(candidate,1);
            }
            System.out.println("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
        }
    }

    static void printMap(HashMap<Candidate, Integer> map){
        Iterator<Entry<Candidate, Integer>> it = map.entrySet().iterator();
        while(it.hasNext()){
            Entry<Candidate, Integer> entry = it.next();
            Candidate candidate = entry.getKey();
            int vote = entry.getValue();
            System.out.println(candidate + " votes = " + vote + " hashcode = " + candidate.hashCode());
        }
    }

    static void addToSet(HashSet<Candidate> set, String[] names, String[] areas){
        for(int i = 0;i<names.length;i++){
            Candidate candidate = new Candidate(names[i], areas[i], i);
            boolean is_present = set.contains(candidate);
            System.out.println("Looked for is present");
            if(is_present){
                System.out.println("Already present again adding");
                set.add(candidate);
            }else{
                System.out.println("Not present and adding");
                set.add(candidate);
            }
            System.out.println("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
        }
    }

    static void printSet(HashSet<Candidate> set){
        Iterator<Candidate> it = set.iterator();
        while(it.hasNext()){
            Candidate candidate = it.next();
            System.out.println(candidate + " hashcode = " + candidate.hashCode());
        }
    }

    public static void main(String[] args){
        String[] names = {"Sachin","Sourav","Ruchit","Sachin","Ruchit","Sachin"};
        String[] areas = {"Hyd","DHN","BLR","Hyd","BLR","Hyd"};
        
        // HashMap<Candidate, Integer> map = new HashMap<Candidate, Integer>();
        // addToHashMap(map, names, areas);
        // System.out.println("======================================");
        // printMap(map);
        
        HashSet<Candidate> set = new HashSet<Candidate>();
        addToSet(set, names, areas);
        System.out.println("======================================");
        printSet(set);
    }
}