import java.util.*;
class Solution {
    public int solution(int n) {
        int sum = 0;
        int answer = 0;
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        
        for(int i = 1; i < n + 1; i++){
            sum += i;
            deque.addLast(i);
            
            while(sum > n){
                sum -= deque.pollFirst();
            }
            if(sum == n){
                answer += 1;
            }
        }
        return answer;
    }
}