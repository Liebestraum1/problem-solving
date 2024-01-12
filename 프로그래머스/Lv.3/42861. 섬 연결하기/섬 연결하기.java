import java.util.*;

class Edge implements Comparable<Edge> {
    int source;
    int dest;
    int weight;
    
    Edge(int source, int dest, int weight){
        this.source = source;
        this.dest = dest;
        this.weight = weight;
    }
    
    @Override
    public int compareTo(Edge e){
        return this.weight - e.weight;
    }
}

class Solution {
    int[] parents;
    
    void init(int n){
        this.parents = new int[n];
        for(int i = 0; i < n; i++){
            parents[i] = i;
        }
    }
    
    int find(int x){
        if(parents[x] == x){
            return x;
        }
        return parents[x] = find(parents[x]);
    }
    
    boolean union(int x, int y){
        int xRoot = find(x);
        int yRoot = find(y);
        
        if(xRoot == yRoot){
            return false;
        }
        
        parents[xRoot] = parents[yRoot];
        return true;
    }
    
    public int solution(int n, int[][] costs) {
        Edge[] edges = new Edge[costs.length];
        int count = 0;
        int answer = 0;
        init(n);
        
        for(int i = 0; i < costs.length; i++){
            int[] edge = costs[i];
            edges[i] = new Edge(edge[0], edge[1], edge[2]);
        }
        
        Arrays.sort(edges);
        
        for(int i = 0; i < edges.length; i++){
            Edge nextEdge = edges[i];
            
            if(!union(nextEdge.source, nextEdge.dest)){
                continue;
            }
            answer += nextEdge.weight;
            count++;
            
            if(count == n - 1){
                break;
            }
        }

        return answer;
    }
}