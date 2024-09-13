import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static class Pair implements Comparable<Pair>{
        int row;
        int col;
        int dist;
        Pair(int row, int col, int dist){
            this.row = row;
            this.col = col;
            this.dist = dist;
        }

        @Override
        public int compareTo(Pair o) {
            return this.dist - o.dist;
        }
    }
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    static int[][] initBoard(final int size) throws IOException {
        int[][] board  = new int[size][size];

        for(int r = 0; r < size; r++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int c = 0; c < size; c++){
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }
        return board;
    }

    static int[][] initDists(final int size){
        int[][] dist = new int[size][size];
        for(int r = 0; r < size; r++){
            for(int c = 0; c < size; c++){
                dist[r][c] = Integer.MAX_VALUE;
            }
        }
        return dist;
    }

    static int find(int[][] board, int[][] dists, int size){
        PriorityQueue<Pair> pq = new PriorityQueue<>();

        dists[0][0] = board[0][0];
        pq.add(new Pair(0, 0, dists[0][0]));


        while(!pq.isEmpty()){
            Pair curPair = pq.poll();
            int row = curPair.row;
            int col = curPair.col;

            if(curPair.dist != dists[row][col]){
                continue;
            }

            for(int i = 0; i < 4; i++){
                int nr = row + dr[i];
                int nc = col + dc[i];

                if(nr < 0 || nc < 0 || nr >= size || nc >= size){
                    continue;
                }

                if(dists[nr][nc] <= dists[row][col] + board[nr][nc]){
                    continue;
                }

                dists[nr][nc] = dists[row][col] + board[nr][nc];
                pq.add(new Pair(nr, nc, dists[nr][nc]));
            }
        }
        return dists[size - 1][size - 1];
    }

    public static void main(String[] args) throws IOException {
        int size;
        int number = 1;

        while((size = Integer.parseInt(br.readLine())) != 0){
            int[][] board = initBoard(size);
            int[][] dists = initDists(size);
            int answer = find(board, dists, size);

            System.out.println("Problem " + number + ": " + answer);
            number++;
        }
    }
}