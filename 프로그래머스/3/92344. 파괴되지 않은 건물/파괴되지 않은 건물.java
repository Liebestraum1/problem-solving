import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        final int N = board.length; // ROW_SIZE
        final int M = board[0].length; // COL_SIZE
        int[][] sum = new int[N + 1][M + 1];
        int answer = 0;
        
        for(int[] cast : skill){
            int type = cast[0] == 1 ? -1 : 1;
            int startRow = cast[1];
            int startCol = cast[2];
            int endRow = cast[3];
            int endCol = cast[4];
            int degree = cast[5] * type;
            
            sum[startRow][startCol] += degree;
            sum[endRow + 1][endCol + 1] += degree;
            sum[startRow][endCol + 1] -= degree;
            sum[endRow + 1][startCol] -= degree;
        }
        
        for(int r = 0; r < N + 1; r++){
            for(int c = 0; c < M; c++){
                sum[r][c + 1] += sum[r][c];
            }
        }
        
        for(int c = 0; c < M + 1; c++){
            for(int r = 0; r < N; r++){
                sum[r + 1][c] += sum[r][c];
            }
        }
        
        for(int r = 0; r < N; r++){
            for(int c = 0; c < M; c++){
                board[r][c] += sum[r][c];
                if(board[r][c] > 0) answer++;
            }
        }
        
        
        return answer;
    }
    
    
}