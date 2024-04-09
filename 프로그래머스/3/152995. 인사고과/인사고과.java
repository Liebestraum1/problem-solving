import java.util.*; 

class Employee {
    int id;
    int aScore;
    int bScore;
    
    Employee(int id, int aScore, int bScore){
        this.id = id;
        this.aScore = aScore;
        this.bScore = bScore;
    }
}
class Solution {
    public int solution(int[][] scores) {
        int SIZE = scores.length;
        
        PriorityQueue<Employee> pq = new PriorityQueue<>((o1, o2) -> {
            return (o2.aScore + o2.bScore) - (o1.aScore + o1.bScore);
        });
        Employee[] employee = new Employee[SIZE];
        
        for(int i = 0; i < SIZE; i++){
            employee[i] = new Employee(i, scores[i][0], scores[i][1]);
        }
    
        Arrays.sort(employee, (o1, o2) -> {
            if(o1.aScore > o2.aScore) return -1;
            if(o1.aScore == o2.aScore) return o1.bScore - o2.bScore;
            return 1;
        });
        
        int maxA = employee[0].aScore;
        int maxB = employee[0].bScore;
        
        for(Employee e : employee){
            if(e.aScore < maxA && e.bScore < maxB) continue;
            pq.add(e);
            
            if(e.bScore > maxB){
                maxA = e.aScore;
                maxB = e.bScore;
            }
        }
        
        int population = 0;
        int rank = 0;
        int maxScore = Integer.MAX_VALUE;
        while(!pq.isEmpty()){
            Employee e = pq.poll();
            population += 1;
            if((e.aScore + e.bScore) < maxScore){
                maxScore = e.aScore + e.bScore;
                rank = population;
            }
            if(e.id == 0){
                return rank;
            }
        }
        
        return -1;
    }
}