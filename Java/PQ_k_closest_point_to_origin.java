import java.util.PriorityQueue;

class Position implements Comparable<Position>{
    
    int x, y;

    Position(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Position o) {
        int distance_from_origin1 = (this.x*this.x) + (this.y*this.y);
        int distance_from_origin2 = (o.x*o.x) + (o.y*o.y);
        if(distance_from_origin1<distance_from_origin2) return 1;
        if(distance_from_origin1>distance_from_origin2) return -1;
        return 0;
    }
    
    @Override
    public String toString(){
        return this.x + ":" + this.y;
    }
}

public class PQ_k_closest_point_to_origin {

    private int get_distance(Position pos){
        return (pos.x*pos.x) + (pos.y*pos.y);
    }

    void print_k_nearest_points(Position[] pos_arr, int k){
        if(k<=0){
            System.out.println("Invalid k");
            return;
        }
        PriorityQueue<Position> pq = new PriorityQueue<Position>();
        for(Position pos:pos_arr){
            if(pq.size()<k){
                pq.add(pos);
            }else if(get_distance(pos)<get_distance(pq.peek())){
                pq.remove();
                pq.add(pos);
            }
            // System.out.println(pq);
        }
        while(!pq.isEmpty()){
            System.out.print(pq.poll() + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[][] coordinates =  {{1,2,3,-5,1,0},
                                {0,1,6,2,-4,-1}};

        Position[] pos_arr = new Position[coordinates[0].length];
        for(int i=0; i<coordinates[0].length;i++){
            pos_arr[i] = new Position(coordinates[0][i], coordinates[1][i]);
        }
        for(Position pos : pos_arr){
            System.out.print(pos + " ");
        }
        System.out.println();
        PQ_k_closest_point_to_origin pq_k_points = 
                new PQ_k_closest_point_to_origin();
        for(int k=0;k<pos_arr.length+1;k++){
            System.out.print("K=" + k + "=> ");
            pq_k_points.print_k_nearest_points(pos_arr, k);
        }
    }

}