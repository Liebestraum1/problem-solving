import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String gem : gems){
            if(!map.containsKey(gem)){
                map.put(gem, 0);
            }
        }
        
        int targetSize = map.size();
        map.clear();
        
        int left = 0;
        int right = 0;
        int[] answer = {0, Integer.MAX_VALUE};
        
        map.put(gems[right], 1);
        
        while(left != gems.length - 1 || right != gems.length - 1){
            if(map.size() < targetSize && right < gems.length - 1) {
                right += 1;
                if(!map.containsKey(gems[right])){
                    map.put(gems[right], 1);
                } else {
                    map.put(gems[right], map.get(gems[right]) + 1);
                }
            } else {
                if(map.size() == targetSize && answer[1] - answer[0] > right - left){
                    answer[0] = left + 1;
                    answer[1] = right + 1;
                }
                
                map.put(gems[left], map.get(gems[left]) - 1);
                if(map.get(gems[left]) == 0){
                    map.remove(gems[left]);
                }
                
                left += 1;           
            }
        }
        
        return answer;
    }
}