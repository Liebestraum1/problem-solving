import java.util.*;

class Solution {
    public int solution(int[] money) {
        int LEN = money.length;
        
        
        int[] firstDP = new int[LEN];
        int[] secondDP = new int[LEN];
        
        // 0번째 집을 반드시 터는 DP
        firstDP[0] = money[0];
        firstDP[1] = money[0];
        firstDP[2] = money[0] + money[2];
        
        for(int i = 3; i < LEN - 1; i++){
            firstDP[i] = Integer.max(firstDP[i - 1],
                                     Integer.max(firstDP[i - 2],
                                                 firstDP[i - 3]) + money[i]);
        }
        
        // 0번째 집을 절대로 털지 않는 DP
        secondDP[0] = 0;
        secondDP[1] = money[1];
        secondDP[2] = Integer.max(money[1], money[2]);

        for(int i = 3; i < LEN; i++){
            secondDP[i] = Integer.max(secondDP[i - 1],
                                     Integer.max(secondDP[i - 2],
                                                 secondDP[i - 3]) + money[i]);
        }
        
        return Integer.max(firstDP[LEN - 2], secondDP[LEN - 1]);
    }
}