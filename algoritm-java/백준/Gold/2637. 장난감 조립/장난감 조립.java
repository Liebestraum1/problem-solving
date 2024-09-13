import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		Queue<Integer> queue = new ArrayDeque<Integer>();
		int[] inDegree = new int[N + 1];
		boolean[] basicComponent = new boolean[N + 1];
		int[][] DP = new int[N + 1][N + 1]; //DP[i][j] = i를 만들때 필요한 j의 개수
		int[][] board = new int[N + 1][N + 1];
		
		for(int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int X = Integer.parseInt(st.nextToken());
			int Y = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			inDegree[X] += 1; // 연결되는 간선 개수 추가
			board[X][Y] = K;
		}
		
		for(int i = 1; i < N + 1; i++) {
			DP[i][i] = 1;
			if(inDegree[i] == 0) {
				queue.add(i); // 기본 부품들 추가하기
				basicComponent[i] = true;
			}
		}
		
		while(!queue.isEmpty()) {
			int currentNode = queue.poll(); // 탐색할 노드 빼기
			for(int nextNode = 1; nextNode < N + 1; nextNode++) {
				if(currentNode != nextNode && board[nextNode][currentNode] != 0) { // 연결 여부를 탐색, 만약 연결되어 있을 경우
					inDegree[nextNode] -= 1; // 간선을 끊는다.
					
					if(inDegree[nextNode] == 0) 
						queue.add(nextNode);
					
					for(int j = 1; j < N + 1; j++) {
						DP[nextNode][j] = DP[nextNode][j] + DP[currentNode][j] * board[nextNode][currentNode];
					}
				}
			}
		}
		
		for(int i = 0; i < N + 1; i++) {
			if(basicComponent[i]) {
				System.out.println(i + " " + DP[N][i]);
			}
		}
	}
}