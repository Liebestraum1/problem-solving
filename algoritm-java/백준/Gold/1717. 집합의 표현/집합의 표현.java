import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Character.Subset;
import java.util.StringTokenizer;
class UnionFind {
    int[] subsets;

    void init(int n){
        subsets = new int[n + 1];
        for(int i = 0; i < n + 1; i++){
            subsets[i] = -1;
        }
    }

    int find(int i){
        if(subsets[i] < 0){
            return i;
        }
        return subsets[i] = find(subsets[i]);
    }

    void union(int x, int y){
        int xRoot = find(x);
        int yRoot = find(y);
        
        if(xRoot == yRoot){
            return;
        }

        if(subsets[xRoot] < subsets[yRoot]){
            subsets[xRoot] += subsets[yRoot];
            subsets[yRoot] = xRoot;
        } else {
            subsets[yRoot] += subsets[xRoot];
            subsets[xRoot] = yRoot;
        }
    }

}

public class Main {
    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        UnionFind subset = new UnionFind();

        subset.init(N);

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());

            int type = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(type == 0){
                subset.union(a, b);
            } else {
                if(subset.find(a) == subset.find(b)){
                    sb.append("YES\n");
                } else {
                    sb.append("NO\n");
                }
            }
        }
        System.out.print(sb);
    }
}