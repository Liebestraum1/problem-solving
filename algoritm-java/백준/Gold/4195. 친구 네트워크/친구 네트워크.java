import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
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
        } else if (subsets[xRoot] >= subsets[yRoot]){
            subsets[yRoot] += subsets[xRoot];
            subsets[xRoot] = yRoot;
        }
    }

}

public class Main {

    public static void main(String[] args) throws IOException {

        UnionFind subset;
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int TC = Integer.parseInt(br.readLine());

        for (int t = 0; t < TC; t++) {
            int N = Integer.parseInt(br.readLine());

            HashMap<String, Integer> hashMap = new HashMap<>();
            String[][] queries = new String[N][2];
            subset = new UnionFind();

            int idx = 0;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                String x = st.nextToken();
                String y = st.nextToken();

                queries[i] = new String[2];
                queries[i][0] = x;
                queries[i][1] = y;

                if (!hashMap.containsKey(x)) {
                    hashMap.put(x, idx);
                    idx++;
                }

                if (!hashMap.containsKey(y)) {
                    hashMap.put(y, idx);
                    idx++;
                }
            }
            
            subset.init(hashMap.size());
            
            for(String[] query : queries) {
                String x = query[0];
                String y = query[1];
                
                subset.union(hashMap.get(x), hashMap.get(y));
                int xRoot = subset.find(hashMap.get(x));
                int yRoot = subset.find(hashMap.get(y));

                int next = -Integer.min(subset.subsets[xRoot], subset.subsets[yRoot]);
                sb.append(next).append(" ");
            }
        }
        System.out.print(sb);
    }
}