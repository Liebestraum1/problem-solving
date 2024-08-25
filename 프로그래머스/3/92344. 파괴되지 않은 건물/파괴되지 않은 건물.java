import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        final int N = board.length; // ROW_SIZE
        final int M = board[0].length; // COL_SIZE
        int[][] sum = new int[N + 1][M + 1];
        int answer = 0;
        
        for(int[] cast : skill){
            int sr = cast[1], sc = cast[2], er = cast[3], ec = cast[4];
            int d = cast[0] == 1 ? -cast[5] : cast[5];
            
            sum[sr][sc] += d;
            sum[er + 1][ec + 1] += d;
            sum[sr][ec + 1] -= d;
            sum[er + 1][sc] -= d;
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