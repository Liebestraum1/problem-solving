import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] board;
	static boolean[][] isVisit;
	static int[] dr = {1, -1, 0, 0};
	static int[] dc = {0, 0, 1, -1};
	static int N;
	static int M;
	static int answer = 0;
	static int initialEmptySpace = 0;
	static ArrayList<Pair> empty = new ArrayList<Pair>();
	static ArrayList<Pair> initVirus = new ArrayList<Pair>(); 
	static Queue<Pair> reverseFlague = new ArrayDeque<Pair>();
	static Queue<Pair> queue = new ArrayDeque<Pair>();
	
	
	static class Pair{
		int row;
		int col;
		
		Pair(int row, int col){
			this.row = row;
			this.col = col;
		}
	}
	
	public static boolean check(int row, int col) {
		if(row >= N || row < 0 || col >= M || col < 0 || board[row][col] == 1 || isVisit[row][col]) {
			return false;
		}
		return true;
	}
	
	public static void dfs(int cnt, int start) {
		if(cnt == 3) {
			int tempAnswer = initialEmptySpace;
			for(int i = 0; i < initVirus.size(); i++)
				queue.add(initVirus.get(i));
			
			while(!queue.isEmpty()) {
				Pair curVirus = queue.poll();
				for(int i = 0; i < 4; i++) {
					int nr = curVirus.row + dr[i];
					int nc = curVirus.col + dc[i];
					if(check(nr, nc)) {
						tempAnswer -= 1;
						queue.add(new Pair(nr, nc));
						isVisit[nr][nc] = true;
						reverseFlague.add(new Pair(nr, nc));
					}
				}
			}
			while(!reverseFlague.isEmpty()) {
				Pair rewind = reverseFlague.poll();
				isVisit[rewind.row][rewind.col] = false;
			}
			answer = Integer.max(answer, tempAnswer);
			return;
		} else { // 벽 세우기
			for(int i = start; i < empty.size(); i++) {
				Pair pair = empty.get(i);
				board[pair.row][pair.col] = 1;
				dfs(cnt + 1, i + 1);
				board[pair.row][pair.col] = 0;
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		board = new int[N][M];
		isVisit = new boolean[N][M];
		
		for(int row = 0; row < N; row++) {
			st = new StringTokenizer(br.readLine());
			for(int col = 0; col < M; col++) {
				int curArea = Integer.parseInt(st.nextToken());
				board[row][col] = curArea;
				if(curArea == 0) {
					empty.add(new Pair(row, col));
					initialEmptySpace += 1;
				} else if(curArea == 2) {
					initVirus.add(new Pair(row, col));
					isVisit[row][col] = true;
				}
			}
		}
		dfs(0, 0);
		System.out.println(answer - 3);
	}
}