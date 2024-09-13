import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 1;
        long low = 1;
        long high = (long) 1_000_000_000 * (times.length);
        
        Arrays.sort(times);
        
        while(low <= high){
            long people = 0;
            long mid = (low + high) / 2;
            
            for(int time : times){
                people += mid / time;
            }
            
            if(people >= n){
                answer = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return answer;
    }
}