import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static List<Integer> list;
    static StringBuilder answer = new StringBuilder();

    static void DFS(int m, int[] permutation) {
        if (m == M) {
            for(int n : permutation){
                answer.append(n).append(' ');
            }
            answer.append("\n");
        } else {
            for(int i : list){
                if(m == 0){
                    permutation[m] = i;
                    DFS(m + 1, permutation);
                } else if(permutation[m - 1] <= i){
                    permutation[m] = i;
                    DFS(m + 1, permutation);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        list = new ArrayList<>();

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < N; i++){
            int nextNum = Integer.parseInt(st.nextToken());
            if(!list.contains(nextNum)){
                list.add(nextNum);
            }
        }

        list.sort(Comparator.comparingInt(o -> o));
        DFS(0, new int[M]);
        System.out.print(answer);
    }
}