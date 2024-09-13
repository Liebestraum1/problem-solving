import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        // n을 적절히 배분하여 works에 있는 원소들의 값을 배제하라
        // 결과적으로 SUM(work : works => work ** 2)의 값을 최소화하라
        // 3 4 5
        //
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> o2 - o1);
        long answer = 0;
        int count = 0;

        for(int work : works){
            pq.add(work);
        }
        
        while(pq.size() > 1 && n > 0){
            int curWork = pq.poll();
            int nextWork = pq.peek();
            
            while(curWork >= nextWork && curWork > 0 && n > 0){
                curWork -= 1;
                n -= 1;
            }
            
            if(curWork != 0){
                pq.add(curWork);
            }
        }
        
        if(pq.size() == 1 && n > 0){
            int curWork = pq.poll();
            if(curWork >= n){
                return (curWork - n) * (curWork - n);
            } else {
                return 0;
            }
        } else {
            while(!pq.isEmpty()){
                int work = pq.poll();
                answer += (work * work);
            }
            return answer;
        }  
    }
}