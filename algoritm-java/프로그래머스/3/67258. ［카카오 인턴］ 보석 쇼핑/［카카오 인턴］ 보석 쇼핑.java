import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        HashSet<String> set = new HashSet<>(Arrays.asList(gems));
        HashMap<String, Integer> map = new HashMap<>();
        
        final int TARGET_SIZE = set.size();
        int[] answer = {1, gems.length};
        int left = 0;
        
        for(int right = 0; right < gems.length; right++){
            String rightKey = gems[right];
            map.put(rightKey, map.getOrDefault(rightKey, 0) + 1);
            
            while(map.size() == TARGET_SIZE){
                String leftKey = gems[left];
                int leftGemCount = map.get(leftKey);
                
                if(answer[1] - answer[0] > right - left){
                    answer[0] = left + 1;
                    answer[1] = right + 1;
                }
                
                if(leftGemCount > 1){
                    map.put(leftKey, leftGemCount - 1);
                } else {
                    map.remove(leftKey);
                }
                left += 1;
            }
        }
        
        return answer;
    }
}