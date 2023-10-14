import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	public static class Lecture implements Comparable<Lecture>{
		int start;
		int end;
		
		Lecture(int start, int end){
			this.start = start;
			this.end = end;
		}
		
		public int compareTo(Lecture o) {
			if(this.start > o.start) return 1;
			else if(this.start < o.start) return -1;
			else {
				if(this.end > o.end) return 1;
				else if(this.end < o.end) return -1;
				else return 0;
			}
		}
		
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		int N = Integer.parseInt(br.readLine());
		int count = 0;
		Lecture[] arr = new Lecture[N];
		
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			arr[i] = new Lecture(start, end);
		}
		
		Arrays.sort(arr);
		pq.add(Integer.MAX_VALUE);
		
		for(int i = 0; i < N; i++) {
			int minEndTime = pq.peek();
			pq.add(arr[i].end);
			if(arr[i].start < minEndTime) {
				count += 1;
			} else {
				pq.poll();
			}
		}
		System.out.println(count);
	}
}