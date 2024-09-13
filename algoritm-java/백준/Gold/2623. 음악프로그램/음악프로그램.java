import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] graph;
	static int[] inDegree;
	static int N;
	static int M;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList[N + 1];
		inDegree = new int[N + 1];
		
		for(int i = 0; i < N + 1; i++)
			graph[i] = new ArrayList<Integer>();
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int people = Integer.parseInt(st.nextToken());
			int[] input = new int[people];
			for(int j = 0; j < people; j++) {
				input[j] = Integer.parseInt(st.nextToken());
			}
			
			for(int j = 0; j < people; j++) {
				for(int k = j + 1; k < people; k++) {
					if(!graph[input[j]].contains(input[k]))
					graph[input[j]].add(input[k]);
				}
			}
		}
		
		Queue<Integer> queue = new ArrayDeque<Integer>();
		
		for(int i = 1; i < N + 1; i++) {
			for(int j = 0; j < graph[i].size(); j++) {
				inDegree[graph[i].get(j)] += 1;
			}
		}
		
		for(int i = 1; i < N + 1; i++) {
			if(inDegree[i] == 0) {
				queue.add(i);
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		int cnt = 0;
		while(!queue.isEmpty()) {
			int currentNode = queue.poll();
			cnt += 1;
			sb.append(currentNode).append("\n");
			
			for(int nextNode : graph[currentNode]) {
				inDegree[nextNode] -= 1;
				if(inDegree[nextNode] == 0) {
					queue.add(nextNode);
				}
			}
		}
		if(cnt != N)
			System.out.println(0);
		else
			System.out.println(sb);
	}
}