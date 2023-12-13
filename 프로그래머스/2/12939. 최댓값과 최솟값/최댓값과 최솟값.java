import java.util.*;

class Solution {
    public String solution(String s) {
        String[] strings = s.split(" ");
        int maxValue = Integer.MIN_VALUE;
        int minValue = Integer.MAX_VALUE;
        
        for(String parsedString : strings){
            int curValue = Integer.parseInt(parsedString);
            if(curValue >= maxValue)
                maxValue = curValue;
            if(curValue <= minValue)
                minValue = curValue;
        }
        return minValue + " " + maxValue;
    }
}