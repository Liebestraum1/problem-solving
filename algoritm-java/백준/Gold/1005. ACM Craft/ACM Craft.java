import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());

			int[] time = new int[N];
			int[] inDegree = new int[N];
			int[] DP = new int[N];
			Queue<Integer> queue = new ArrayDeque<Integer>();

			ArrayList<Integer>[] adjacencyList = new ArrayList[N];

			for (int i = 0; i < N; i++)
				adjacencyList[i] = new ArrayList<Integer>();

			st = new StringTokenizer(br.readLine()); // 건설 시간 입력
			for (int i = 0; i < N; i++)
				time[i] = Integer.parseInt(st.nextToken());
			
			
			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine());
				int startNode = Integer.parseInt(st.nextToken()) - 1;
				int endNode = Integer.parseInt(st.nextToken()) - 1;
				adjacencyList[startNode].add(endNode);
				inDegree[endNode] += 1;
			}

			int target = Integer.parseInt(br.readLine()) - 1;

			for (int i = 0; i < N; i++) {
				if (inDegree[i] == 0) {
					DP[i] = time[i];
					queue.add(i);
				}
			}

			while (!queue.isEmpty()) {
				int currentNode = queue.poll();
				for (int nextNode : adjacencyList[currentNode]) {
					DP[nextNode] = Integer.max(DP[nextNode], DP[currentNode] + time[nextNode]);
					
					inDegree[nextNode]--;
					
					if (inDegree[nextNode] == 0) {
						queue.add(nextNode);
					}
				} 
			}
			System.out.println(DP[target]);
		}
	}
}