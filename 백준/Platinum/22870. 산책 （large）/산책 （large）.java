import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	public static long INF = Long.MAX_VALUE;
	public static long[] startToEndDist;
	public static long[] endToStartDist;
	public static boolean[] isVisit;
	public static ArrayList<Node>[] graph;
	public static ArrayList<Integer> path;

	public static class Node implements Comparable<Node> {
		int node;
		long distance;

		Node(int node, long distance) {
			this.node = node;
			this.distance = distance;
		}

		@Override
		public int compareTo(Node o) {
			if (this.distance > o.distance)
				return 1;
			else if (this.distance < o.distance)
				return -1;
			else
				return 0;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		graph = new ArrayList[N + 1];
		isVisit = new boolean[N + 1];
		path = new ArrayList<Integer>();

		startToEndDist = new long[N + 1];
		endToStartDist = new long[N + 1];

		for (int i = 1; i < N + 1; i++)
			graph[i] = new ArrayList<Node>();

		Arrays.fill(startToEndDist, INF);
		Arrays.fill(endToStartDist, INF);

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			graph[a].add(new Node(b, w));
			graph[b].add(new Node(a, w));
		}

		st = new StringTokenizer(br.readLine());
		int startNode = Integer.parseInt(st.nextToken());
		int endNode = Integer.parseInt(st.nextToken());

		startToEndDist[startNode] = 0;
		pq.add(new Node(startNode, startToEndDist[startNode]));

		while (!pq.isEmpty()) {
			Node curNode = pq.poll();
			int curNodeNum = curNode.node;
			long curDist = curNode.distance;

			if (startToEndDist[curNodeNum] < curDist)
				continue;

			for (Node nextNode : graph[curNodeNum]) {
				int nextNodeNum = nextNode.node;
				long nextDist = nextNode.distance;

				if (startToEndDist[nextNodeNum] <= startToEndDist[curNodeNum] + nextDist)
					continue;
				startToEndDist[nextNodeNum] = startToEndDist[curNodeNum] + nextDist;
				pq.add(new Node(nextNodeNum, startToEndDist[nextNodeNum]));
			}
		}

		Arrays.fill(endToStartDist, INF);
		endToStartDist[endNode] = 0;
		pq.add(new Node(endNode, endToStartDist[endNode]));

		while (!pq.isEmpty()) {
			Node curNode = pq.poll();
			int curNodeNum = curNode.node;
			long curDist = curNode.distance;

			if (endToStartDist[curNodeNum] < curDist)
				continue;

			for (Node nextNode : graph[curNodeNum]) {
				int nextNodeNum = nextNode.node;
				long nextDist = nextNode.distance;

				if (endToStartDist[nextNodeNum] <= endToStartDist[curNodeNum] + nextDist)
					continue;
				endToStartDist[nextNodeNum] = endToStartDist[curNodeNum] + nextDist;
				pq.add(new Node(nextNodeNum, endToStartDist[nextNodeNum]));
			}
		}

		long go = startToEndDist[endNode];

		int nodeForTracking = startNode;
		int preNode = startNode;
		isVisit[startNode] = true;

		while (nodeForTracking != endNode) {
			int minNode = Integer.MAX_VALUE;
			for (int i = 0; i < graph[nodeForTracking].size(); i++) {
				Node nextNode = graph[nodeForTracking].get(i);
				if(nextNode.node == preNode) continue;
				if (!isVisit[nextNode.node] && startToEndDist[nodeForTracking] + nextNode.distance + endToStartDist[nextNode.node] == go) {
					minNode = Integer.min(minNode, nextNode.node);
				}
			}
			isVisit[minNode] = true;
			preNode = nodeForTracking;
			nodeForTracking = minNode;
		}

		Arrays.fill(endToStartDist, INF);
		isVisit[startNode] = false;
		isVisit[endNode] = false;
		endToStartDist[endNode] = 0;
		pq.add(new Node(endNode, endToStartDist[endNode]));

		while (!pq.isEmpty()) {
			Node curNode = pq.poll();
			int curNodeNum = curNode.node;
			long curDist = curNode.distance;

			if (endToStartDist[curNodeNum] < curDist)
				continue;

			for (Node nextNode : graph[curNodeNum]) {
				int nextNodeNum = nextNode.node;
				long nextDist = nextNode.distance;

				if(endToStartDist[nextNodeNum] <= endToStartDist[curNodeNum] + nextDist) continue;
				if(isVisit[nextNodeNum]) continue;
				endToStartDist[nextNodeNum] = endToStartDist[curNodeNum] + nextDist;
				pq.add(new Node(nextNodeNum, endToStartDist[nextNodeNum]));
			}
		}

		long come = endToStartDist[startNode];

		System.out.println(go + come);
	}
}