import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        int low = 1;
        int high = K;

        while (low <= high){
            int mid = (low + high) / 2;

            int remainder = 0;
            for(int i = 1; i < N + 1; i++) {
                if(mid / i > N){
                    remainder += N;
                } else {
                    remainder += mid / i;
                }
            }

            if(remainder < K){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        System.out.println(low);
    }
}