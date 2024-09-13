import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		int[] time = new int[N];
		int[] inDegree = new int[N];
		int[] DP = new int[N];
		Queue<Integer> queue = new ArrayDeque<Integer>();

		ArrayList<Integer>[] adjacencyList = new ArrayList[N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			adjacencyList[i] = new ArrayList<Integer>();
			time[i] = Integer.parseInt(st.nextToken());
			
			int len = Integer.parseInt(st.nextToken());
			
			for(int j = 0; j < len; j++) {
				int linkedNode = Integer.parseInt(st.nextToken()) - 1;
				adjacencyList[linkedNode].add(i);
				inDegree[i] += 1;
			}
		}

		int answer = 0;
		for (int i = 0; i < N; i++) {
			if (inDegree[i] == 0) {
				queue.add(i);
				DP[i] = time[i];
				answer = Integer.max(DP[i], answer);
			}
		}
		
		while (!queue.isEmpty()) {
			int currentNode = queue.poll();
			
			for (int nextNode : adjacencyList[currentNode]) {
				DP[nextNode] = Integer.max(DP[nextNode], DP[currentNode] + time[nextNode]);
				answer = Integer.max(answer, DP[nextNode]);
				inDegree[nextNode]--;

				if (inDegree[nextNode] == 0) {
					queue.add(nextNode);
				}
			}
		}
		System.out.println(answer);
	}
}