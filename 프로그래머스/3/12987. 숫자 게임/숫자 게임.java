import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
		Arrays.sort(A); // 약한쪽부터 가장 낮은 순서로 이기는 법
        Arrays.sort(B);
        
        int pointer = 0;
        int answer = 0;
        
        for(int i : B){
            if(A[pointer] >= i){
                continue;
            } else {
                pointer += 1;
                answer++;
            }
        }
        return answer;
    }
}