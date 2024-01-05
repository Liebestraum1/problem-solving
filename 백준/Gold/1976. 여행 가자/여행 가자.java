import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] parents;
	
	public static void makeset(int num) {
		parents = new int[num];
		for(int i = 0; i < num; i++)
			parents[i] = i;
	}
	
	public static int find(int e) {
		if(parents[e] == e)
			return e;
		return parents[e] = find(parents[e]);
	}
	
	public static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		
		if(aRoot == bRoot)
			return false;
		parents[bRoot] = parents[aRoot];
		return true;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		int[][] cities = new int[N][N];
		
		makeset(N);
		
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 0; j < i + 1; j++){
				int link = Integer.parseInt(st.nextToken());
				if(link == 1) {
					union(i, j);
				}
			}
		}
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int parent = find(Integer.parseInt(st.nextToken()) - 1);
		
		for(int i = 0; i < M - 1; i++) {
			if(parent != find(Integer.parseInt(st.nextToken()) - 1)) {
				System.out.println("NO");
				return;
			}
		}
		System.out.println("YES");
	}
}