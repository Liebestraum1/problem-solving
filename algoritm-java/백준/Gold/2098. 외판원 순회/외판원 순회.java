import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static int N;
	public static int[][] DP;
	public static int[][] W;
	public static int INF = Integer.MAX_VALUE / 2;
	public static int TSP(int visitedNode, int currentNode) {
		if(DP[visitedNode][currentNode] != 0) { // 해당 노드를 방문했는가?
			return DP[visitedNode][currentNode];
		}
		
		if(visitedNode == (1 << N) - 1) {
			if(W[currentNode][0] != 0)
				return W[currentNode][0];
			return INF;
		}
		
		
		else {
			DP[visitedNode][currentNode] = INF;
			for(int i = 0; i < N; i++) { // 0은 무조건 방문되어 있으므로 1부터 밀기 시작
				if((visitedNode & (1 << i)) == 0 && W[currentNode][i] != 0) {
					DP[visitedNode][currentNode] = Integer.min(DP[visitedNode][currentNode], 
							TSP(visitedNode | (1 << i), i) + W[currentNode][i]); // Top-Down이므로 i에서 currentNode로 가는 경우로   
				}
			}
		}
		
		return DP[visitedNode][currentNode];
		//Top - Down으로 진행할 때 이미 방문한 마을 다시 안 가도 되는 이유는?
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		DP = new int[1 << N][N];
		W = new int[N][N];
		
		for(int r = 0; r < N; r++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int c = 0; c < N; c++) {
				W[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(TSP(1, 0));
	}
}