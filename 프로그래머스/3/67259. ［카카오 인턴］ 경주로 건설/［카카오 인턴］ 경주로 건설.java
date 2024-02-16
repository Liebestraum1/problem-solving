import java.util.*;

class Pair {
    int row;
    int col;
    int cost;
    int direction; // 0 = 오른쪽으로 진행중, 1 = 왼쪽으로 진행중, 2 = 아래쪽으로 진행중, 3 = 위쪽으로 진행중
    
    public Pair(int row, int col, int cost, int direction){
        this.row = row;
        this.col = col;
        this.cost = cost;
        this.direction = direction;
    }
    
    public Pair goStraight(){
        int newCost = this.cost + 100;
        
        if(direction == 0) {
            return new Pair(this.row, this.col + 1, newCost, direction);
        } else if (direction == 1){
            return new Pair(this.row, this.col - 1, newCost, direction);
        } else if (direction == 2){
            return new Pair(row + 1, col, newCost, direction);
        } else {
            return new Pair(row - 1, col, newCost, direction);
        }
    }
    
    public Pair turnLeft(){
        int newCost = this.cost + 600;
        
        if(direction == 0){ //우측 진행하다가 왼쪽으로 턴
            return new Pair(this.row - 1, col, newCost, 3);
        } else if (direction == 1){ // 좌측 진행하다가 왼쪽으로 턴
            return new Pair(row + 1, col, newCost, 2);
        } else if (direction == 2){ // 아래쪽 진행하다가 왼쪽으로 턴
            return new Pair(row, col + 1, newCost, 0);
        } else {
            return new Pair(row, col - 1, newCost, 1);
        }
    }
    
    public Pair turnRight(){
        int newCost = this.cost + 600;
        if(direction == 0){ //우측 진행하다가 오른쪽으로 턴
            return new Pair(row + 1, col, newCost, 2);
        } else if (direction == 1){ // 왼쪽 진행하다가 오른쪽으로 턴
            return new Pair(row - 1, col, newCost, 3);
        } else if (direction == 2){ // 아래쪽 진행하다가 오른쪽으로 턴
            return new Pair(row, col - 1, newCost, 1);
        } else {
            return new Pair(row, col + 1, newCost, 0);
        }
    }
    
}

class Solution {
    int BOARD_SIZE = 0;
    
    // 벽인지 아닌지 판별하기
    // 방문했는지 아닌지 판별하기
    // 코너인지 아닌지 판별하기
    
    public boolean isInBound(Pair pair, int[][] board) {
        int row = pair.row;
        int col = pair.col;
        if(row < 0 || col < 0 || row >= BOARD_SIZE || col >= BOARD_SIZE || board[row][col] == 1){
            return false;
        }
        return true;
    };
    
    public boolean isCheaper(Pair pair, int[][][] costs){
        if(pair.cost <= costs[pair.row][pair.col][pair.direction]){
            return true;
        }
        return false;
    }
    
    public boolean move(Pair movingPair, int[][] board, int[][][] costs){
        if(isInBound(movingPair, board) && isCheaper(movingPair, costs)){
            costs[movingPair.row][movingPair.col][movingPair.direction] = movingPair.cost;
            return true;
        }
        return false;
    }
    
    
    public int solution(int[][] board) {
        BOARD_SIZE = board.length;
        Queue<Pair> queue = new ArrayDeque<>();
        int[][][] costs = new int[BOARD_SIZE][BOARD_SIZE][4];
        
        for(int r = 0; r < BOARD_SIZE; r++){
            for(int c = 0; c < BOARD_SIZE; c++){
                for(int d = 0; d < 4; d++){
                    costs[r][c][d] = Integer.MAX_VALUE;
                }
            }
        }
        
        queue.add(new Pair(0, 0, 0, 0));
        queue.add(new Pair(0, 0, 0, 2));
        
        while(!queue.isEmpty()){
            Pair pair = queue.poll();
            
            Pair straightPair = pair.goStraight();
            Pair leftTurnPair = pair.turnLeft();
            Pair rightTurnPair = pair.turnRight();
            
            if(move(straightPair, board, costs)) queue.add(straightPair);
            if(move(leftTurnPair, board, costs)) queue.add(leftTurnPair);
            if(move(rightTurnPair, board, costs)) queue.add(rightTurnPair);
        }
        
        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < 4; i++){
            answer = Integer.min(answer, costs[BOARD_SIZE - 1][BOARD_SIZE - 1][i]);
        }
        
        return answer;
    }
}