class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        int[] fail = {-1};
        int share = s / n;
        int remainder = s % n;
        
        if(share < 1){
            return fail;
        }
        
        for(int i = 0; i < n; i++){
            answer[i] = share;
            if(i >= n - remainder){
                answer[i] += 1;
                remainder -= 1;
            }
        }
        
        return answer;
    }
}