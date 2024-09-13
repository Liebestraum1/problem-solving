import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] dr = {1, -1, 0, 0};
	static int[] dc = {0, 0, 1, -1};
	
	static class Coordinate{
		int row;
		int col;
		
		Coordinate(){};
		
		Coordinate(int row, int col){
			this.row = row;
			this.col = col;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		
		Queue<Coordinate> queue = new ArrayDeque<Coordinate>();
		ArrayList<Integer> answerList = new ArrayList<Integer>();
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		boolean[][] isVisit = new boolean[N][N];
		int[][] board = new int[N][N];
		int complex = 0;
		
		for(int r = 0; r < N; r++) {
			String row = br.readLine();
			for(int c = 0; c < N; c++) {
				board[r][c] = row.charAt(c) - '0';
			}
		}
		

		
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < N; c++) {
				if(isVisit[r][c] || board[r][c] == 0)
					continue;
				
				complex++;
				int cnt = 0;
				queue.add(new Coordinate(r, c));
				isVisit[r][c] = true;
				
				while(!queue.isEmpty()) {
					Coordinate currentNode = queue.poll();
					cnt += 1;
					for(int i = 0; i < 4; i++) {
						int nr = currentNode.row + dr[i];
						int nc = currentNode.col + dc[i];
						if(nr >= N || nr < 0 || nc >= N || nc < 0 || board[nr][nc] == 0 || isVisit[nr][nc])
							continue;
						queue.add(new Coordinate(nr, nc));
						isVisit[nr][nc] = true;
					}
				}
				answerList.add(cnt);
			}
		}
		System.out.println(complex);
		Collections.sort(answerList);
		for(int i : answerList) {
			sb.append(i).append("\n");
		}
		System.out.println(sb);
		
		
	}
}