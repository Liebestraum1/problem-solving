class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] DP = new int[n][m];
        int divider = 1000000007;
        
        for(int[] puddle : puddles){
            int row = puddle[1] - 1;
            int col = puddle[0] - 1;
            DP[row][col] = -1;
        }
        
        for(int row = 1; row < n; row++){
            if(DP[row][0] == -1 || DP[row - 1][0] == -1){
                DP[row][0] = -1;
            } else {
                DP[row][0] = 1;
            }
        }
        
        for(int col = 1; col < m; col++){
            if(DP[0][col] == -1 || DP[0][col - 1] == - 1){
                DP[0][col] = -1;
            } else {
                DP[0][col] = 1;
            }
        }
        
        for(int row = 1; row < n; row++){
            for(int col = 1; col < m; col++){       
                if(DP[row][col] == -1){
                    continue;
                }
                
                if(DP[row - 1][col] == -1 && DP[row][col - 1] == -1){
                    DP[row][col] = -1;
                } else if(DP[row - 1][col] == -1 && DP[row][col - 1] != -1){
                    DP[row][col] = DP[row][col - 1];
                } else if(DP[row - 1][col] != -1 && DP[row][col - 1] == -1){
                    DP[row][col] = DP[row - 1][col];
                } else {
                    DP[row][col] = (DP[row - 1][col] % divider + DP[row][col - 1] % divider) % divider;
                }
            }
        }
        return DP[n - 1][m - 1] <= 0 ? 0 : DP[n - 1][m - 1];
    }
}