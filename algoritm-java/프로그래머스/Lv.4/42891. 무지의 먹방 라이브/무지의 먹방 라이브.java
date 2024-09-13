import java.util.*;

class Solution {
    public int solution(int[] food_times, long k) {
        int left = 0;
        int right = 100_000_000;
        
        while(left <= right){
            int targetFood = (left + right) / 2; // 먹어치울 음식 사이즈
            int eatenFoodCount = 0;
            long eatenFood = 0;
            
            for(int i = 0; i < food_times.length; i++){
                if(food_times[i] > targetFood){
                    eatenFood += targetFood;
                } else if(food_times[i] == targetFood){
                    eatenFood += targetFood;
                    eatenFoodCount += 1;
                } else {
                    eatenFood += food_times[i];
                    eatenFoodCount += 1;
                }
            }

            int leftFoodCount = food_times.length - eatenFoodCount;
            long leftTime = k - eatenFood;
            
            
            if(0 > leftTime){
                right = targetFood - 1;
            } else if(0 < leftTime){
                left = targetFood + 1;
            } else {
                break;
            }
        }
        
        int targetFood = (left + right) / 2;
        
        for(int i = 0; i < food_times.length; i++){
            if(food_times[i] - targetFood >= 0){
                k -= targetFood;
                food_times[i] -= targetFood;
            } else {
                k -= food_times[i];
                food_times[i] = 0;
            }
        }
 
        for(int i = 0; i < food_times.length; i++){
            if(k == 0 && food_times[i] > 0){
                return i + 1;
            }  
            if(food_times[i] > 0){
                k -= 1;
            }
        }
        
        return -1;
    }
}