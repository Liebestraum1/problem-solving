import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int answer = Integer.MAX_VALUE;
		int answerNum = Integer.MAX_VALUE;
		
		ArrayList<Integer>[]  adjList = new ArrayList[N];
		for(int i = 0; i < N; i++)
			adjList[i] = new ArrayList<Integer>();
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int startNode = Integer.parseInt(st.nextToken()) - 1;
			int endNode = Integer.parseInt(st.nextToken()) - 1;
			
			adjList[startNode].add(endNode);
			adjList[endNode].add(startNode);
		}
		
		for(int i = 0; i < N; i++) {
			Queue<Integer> queue = new ArrayDeque<>();
			boolean[] isVisit = new boolean[N];
			
			queue.add(i);
			isVisit[i] = true;
			
			int peopleOfCurrentDepth = queue.size();
			int currentAnswer = 0;
			int depth = 0;
			int cnt = 0;
			
			while(!queue.isEmpty()) {
				int currentNode = queue.poll();
				currentAnswer += depth;
				
				for(int nextNode : adjList[currentNode]) {
					if(!isVisit[nextNode]) {
					queue.add(nextNode);
					isVisit[nextNode] = true;
					}
				}
				
				cnt += 1;
				if(cnt == peopleOfCurrentDepth) {
					cnt = 0;
					depth += 1;
					peopleOfCurrentDepth = queue.size();
					
				}
			}
			
			if(answer > currentAnswer) {
				answer = currentAnswer;
				answerNum = i;
			} else if(answer == currentAnswer && i < answerNum) {
				answerNum = i;
			}
		}
		System.out.println(answerNum + 1);
	}
}