class Solution {
    public int solution(int[] a) {
        int answer = 0;
        int[] forward = new int[a.length];
        int[] backward = new int[a.length];
        forward[0] = a[0];
        backward[a.length - 1] = a[a.length - 1];
        
        for(int i = 1; i < a.length; i++){
            forward[i] = Integer.min(forward[i - 1], a[i]);
            backward[a.length - 1 - i] = Integer.min(backward[a.length - i], a[a.length - 1 - i]);
        }
        
        for(int i = 0; i < a.length; i++){
            if(forward[i] < a[i]){
                if(backward[i] >= a[i]){
                    answer += 1;
                }
            } else {
                answer += 1;
            }
        } 
        return answer;
    }
}