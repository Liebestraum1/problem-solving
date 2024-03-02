import java.util.*;

class Pair {
    int row;
    int col;
    
    Pair(int row, int col){
        this.row = row;
        this.col = col;
    }
}

class Solution {
    static final int[] dr = {1, -1, 0, 0};
    static final int[] dc = {0, 0, 1, -1};
    
    public boolean check(int[][] land, int[][] visited, int row, int col){
        if(row < 0 || row >= visited.length || col < 0 || col >= visited[0].length){
            return false;
        }
        
        if(land[row][col] != 1 || visited[row][col] != 0) {
            return false;
        }
        
        return true;
    }
    
    public void find(Pair startPoint, int[][] land, int[][] visited, int chunk){
        Queue<Pair> queue = new ArrayDeque<>();
        
        queue.add(startPoint);
        visited[startPoint.row][startPoint.col] = chunk;
        
        while(!queue.isEmpty()){
            Pair curPair = queue.poll();
            int row = curPair.row;
            int col = curPair.col;
            
            for(int i = 0; i < 4; i++){
                int nextRow = curPair.row + dr[i];
                int nextCol = curPair.col + dc[i];
                if(check(land, visited, nextRow, nextCol)){
                    visited[nextRow][nextCol] = chunk;
                    queue.add(new Pair(nextRow, nextCol));
                }
            }
        }
    }
    
    public int solution(int[][] land) {
        final int ROW = land.length;
        final int COL = land[0].length;
        int[][] visited = new int[ROW][COL];
        
        int chunk = 1;
        
        for(int r = 0; r < ROW; r++){
            for(int c = 0; c < COL; c++){
                if(check(land, visited, r, c)){
                    find(new Pair(r, c), land, visited, chunk);
                    chunk += 1;
                }
            }
        }
        
        int[] chunks = new int[chunk];
        boolean[][] answers = new boolean[COL][chunk];
        
        for(int r = 0; r < ROW; r++){
            for(int c = 0; c < COL; c++){
                if(visited[r][c] != 0){
                    chunks[visited[r][c]] += 1;
                    answers[c][visited[r][c]] = true;
                }
            }
        }
        
        int answer = 0;
        for(boolean[] linkedChunk : answers){
            int tempAnswer = 0;
            for(int i = 0; i < chunk; i++){
                if(linkedChunk[i] == true){
                    tempAnswer += chunks[i];
                }
            }
            answer = Integer.max(answer, tempAnswer);
        }

        return answer;
        // 전체 탐색
        // visited 배열 만들기
        
    }
}