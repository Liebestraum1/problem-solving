import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[] dr = {1, -1, 0, 0};
	static int[] dc = {0, 0, 1, -1};
	
	static char[][] board;
	static int[][][] isVisit;
	
	static int INF = Integer.MAX_VALUE;
	static int answer = Integer.MAX_VALUE;
	
	public static boolean check(int row, int col, int key) {
		if(row >= N || row < 0 || col >= M || col < 0 || board[row][col] == '#')
			return false; //1. 범위 체크
	
		if(board[row][col] >= 'A' && board[row][col] <= 'F') { //문인 경우
			int door = board[row][col] - 'A';
			if((key & (1 << door)) == 0) { //현재 문에 해당하는 키가 있는지 확인
				return false; //없으면 false
			}
		}
		return true;
	}
	
	public static class Moon{
		int row;
		int col;
		int key;
		int count;
		
		Moon(int row, int col, int key, int count){
			this.row = row;
			this.col = col;
			this.key = key;
			this.count = count;
		}
	}
	
	public static void main(String[] args) throws IOException {
		//큐에 들어갈 것: 행좌표, 열좌표, 가진 열쇠 상태, 이동 회수
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		board = new char[N][M];
		isVisit = new int[N][M][1 << 6];
		
		Queue<Moon> queue = new ArrayDeque<Moon>();
		
		for(int row = 0; row < N; row++) {
			for(int col = 0; col < M; col++) {
				for(int key = 0; key < (1 << 6); key++) {
					isVisit[row][col][key] = INF;  
				}
			}
		}
		
		for(int row = 0; row < N; row++) {
			String r = br.readLine();
			for(int col = 0; col < M; col++) {
				board[row][col] = r.charAt(col);
				if(board[row][col] == '0') {
					queue.add(new Moon(row, col, 0, 0));
					isVisit[row][col][0] = 0;
				}
			}
		}
		
		// a = 1, b = 2, c = 3, d = 4, e = 5, f = 6
		while(!queue.isEmpty()) {
			Moon curMoon = queue.poll();
			for(int m = 0; m < 4; m++) {
				int nr = curMoon.row + dr[m];
				int nc = curMoon.col + dc[m];
				int curKey = curMoon.key;
				int nextCnt = curMoon.count + 1;	
				
				if(!check(nr, nc, curKey)) //범위를 벗어나거나 키가 없는 경우
					continue;
				
				if(board[nr][nc] == '1') {
					answer = Integer.min(answer, nextCnt);
					continue;
				}
				
				if(board[nr][nc] >= 'a' && board[nr][nc] <= 'f') { //다음 범위가 키인 경우
					int nextKey = 1 << (board[nr][nc] - 'a');
					if((curKey & nextKey) == 0) {
						curKey |= nextKey; // 키 획득
					}
				}
				
				if(isVisit[nr][nc][curKey] > nextCnt) { //이동할 위치의 값 판단
					
					isVisit[nr][nc][curKey] = nextCnt;
					queue.add(new Moon(nr, nc, curKey, nextCnt));
				}
			}
		}
		if(answer == INF) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
	}
}