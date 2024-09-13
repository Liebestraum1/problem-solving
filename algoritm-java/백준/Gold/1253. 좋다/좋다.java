import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine()); 
		long[] arr = new long[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}
		
		if(arr.length < 3) {
			System.out.println(0);
			return;
		}
		
		Arrays.sort(arr);
		int answer = 0;
		
		int left;
		int right;
		
		for(int idx = 0; idx < N; idx++) {
			long targetNum = arr[idx];
			right = N - 1;
			left = 0;
			while(left < right) {
				if(arr[right] + arr[left] == targetNum) {
					if((right != idx) && (left != idx)) {
						answer += 1;
						break;
					}
					else if(right == idx) {
						right -= 1;
					}
					else if (left == idx) {
						left += 1;
					}
				}
				else if (arr[left] + arr[right] < targetNum) {
					left += 1;
				} else {
					right -= 1;
				}
			}
		}
		System.out.println(answer);
	}
}