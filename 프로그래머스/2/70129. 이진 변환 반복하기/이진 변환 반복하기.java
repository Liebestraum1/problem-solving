class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int initialLength = 0;
        
        if(!s.equals("1")){
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == '1'){
                    initialLength += 1;
                }
            }
            answer[0] += 1;
            answer[1] += s.length() - initialLength;
            s = Integer.toBinaryString(initialLength);
        }
        
        while(!s.equals("1")){
            int beforeLength = s.length();
            int afterLength = Integer.bitCount(Integer.parseInt(s, 2));
            
            answer[0] += 1;
            answer[1] += beforeLength - afterLength;
            s = Integer.toBinaryString(afterLength);
        }
        return answer;
    }
}