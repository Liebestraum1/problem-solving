class DisjointSet {
    int[] parents;
    
    void init(int n){
        parents = new int[n];
        for(int i = 0; i < n; i++){
            parents[i] = i;
        }
    }
    
    int find(int e) {
        if(parents[e] == e){
            return e;
        }
        return parents[e] = find(parents[e]);
    }
    
    boolean union(int a, int b){
        int aRoot = find(a);
        int bRoot = find(b);
        
        if(aRoot == bRoot){
            return false;
        }
        parents[bRoot] = parents[aRoot];
        return true;
    }
}

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] isParent = new boolean[n];
        DisjointSet network = new DisjointSet();
        network.init(n);
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(computers[i][j] == 1){
                    network.union(i, j);
                }
            }
        }
    
        for(int i = 0; i < n; i++){
            isParent[network.find(i)] = true;
        }
        
        for(int i = 0; i < n; i++){
            if(isParent[i]){
                answer += 1;
            }
        }

        return answer;
    }
}