import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> heap = new PriorityQueue<Integer>((o1, o2) ->  {
			return o2 - o1;
		});
		
		int N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
			int X = Integer.parseInt(br.readLine());
			if(X == 0 && heap.isEmpty()) {
				sb.append("0\n");
			} else if (X == 0 && !heap.isEmpty()) {
				sb.append(heap.poll()).append("\n");
			} else
				heap.add(X);
		}
		System.out.print(sb);
	}
}