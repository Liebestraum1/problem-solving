class Solution {
    public int solution(int[][] triangle) {
        final int ROW = triangle.length;
        
        int[][] DP = new int[ROW][];
        int answer = 0;
        
        // DP 배열 초기화
        for(int r = 0; r < ROW; r++){
            final int COLUMN = triangle[r].length;
            DP[r] = new int[COLUMN];
        }
        
        DP[0][0] = triangle[0][0];
      
        for(int r = 1; r < ROW; r++){
            final int currentColumnSize = DP[r].length;
            for(int c = 0; c < currentColumnSize; c++) {
                if (c == 0) {
                   DP[r][c] = DP[r-1][c] + triangle[r][c]; 
                } else if (c == currentColumnSize - 1){
                    DP[r][c] = DP[r-1][c-1] + triangle[r][c]; 
                } else {
                    DP[r][c] = Integer.max(DP[r-1][c], DP[r-1][c-1]) + triangle[r][c];
                }
                answer = Integer.max(answer, DP[r][c]);
            }
        }
        return answer;
    }
}