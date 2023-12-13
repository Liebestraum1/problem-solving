import java.util.*;

class Solution {
    int ROW_SIZE = 0;
    int COL_SIZE = 0;
    
    int[][] arr;
    boolean[][] visited;
    
    int[] dr = {1, -1, 0, 0};
    int[] dc = {0, 0, 1, -1};
    
    public boolean check(int row, int col, int startColor){
        if(row >= ROW_SIZE || row < 0 || col >= COL_SIZE || col < 0)
            return false;
        if(visited[row][col] || arr[row][col] != startColor || arr[row][col] == 0)
            return false;
        return true;
    }
    
    public int BFS(int startRow, int startCol) {
        Queue<int[]> queue = new ArrayDeque<>();
        
        int[] startRowCol = {startRow, startCol};
        int startColor = arr[startRow][startCol];
        int sizeOfCurrentArea = 1;
        
        visited[startRow][startCol] = true;
        queue.add(startRowCol);
        
        while(!queue.isEmpty()){
            int[] currentRowCol = queue.poll();
            int currentRow = currentRowCol[0];
            int currentCol = currentRowCol[1];
            
            for(int i = 0; i < 4; i++){
                int nextRow = currentRow + dr[i];
                int nextCol = currentCol + dc[i];
                if(check(nextRow, nextCol, startColor)){
                    sizeOfCurrentArea += 1;
                    visited[nextRow][nextCol] = true;
                    int[] nextRowCol = {nextRow, nextCol};
                    queue.add(nextRowCol);
                }
            }   
        }
        return sizeOfCurrentArea;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        ROW_SIZE = m;
        COL_SIZE = n;
        
        visited = new boolean[ROW_SIZE][COL_SIZE];
        arr = picture;
        
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        for(int r = 0; r < ROW_SIZE; r++){
            for(int c = 0; c < COL_SIZE; c++){
                if(check(r, c, arr[r][c])){
                    numberOfArea += 1;
                    
                    int sizeOfCurrentArea = BFS(r, c);
                    if(sizeOfCurrentArea > maxSizeOfOneArea){
                        maxSizeOfOneArea = sizeOfCurrentArea;
                    }
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}