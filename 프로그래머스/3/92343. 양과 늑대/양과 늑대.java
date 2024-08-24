import java.util.*;

class Node {
    int val;
    Node left;
    Node right;
    boolean sheep;
    
    Node(int val){
        this.val = val;
    }
}

class Solution {
    static int answer;
    public void dfs(Node[] nodes, Node node, boolean[] visited, boolean[] shouldVisit, int sheep, int wolf){
        answer = Integer.max(answer, sheep);
        
        if(node.left != null) shouldVisit[node.left.val] = true;
        if(node.right != null) shouldVisit[node.right.val] = true;
        
        for(int i = 0; i < shouldVisit.length; i++){
            if(!shouldVisit[i]) continue;
            
            Node nextNode = nodes[i];
            int nSheep = sheep;
            int nWolf = wolf;
            
            if(nextNode.sheep){
                nSheep++;
            } else {
                nWolf++;
            }
            
            if(nWolf >= nSheep || visited[nextNode.val]) continue;
            visited[nextNode.val] = true;
            dfs(nodes, nextNode, visited, shouldVisit, nSheep, nWolf);
            visited[nextNode.val] = false;
        }
        
        if(node.left != null) shouldVisit[node.left.val] = false;
        if(node.right != null) shouldVisit[node.right.val] = false;
    }
    
    public int solution(int[] info, int[][] edges) {
        final int N = info.length;
        answer = 0;
        
        Node[] node = new Node[N];
        boolean[] visited = new boolean[N];
        boolean[] shouldVisit = new boolean[N];
        
        for(int[] edge : edges){
            int parent = edge[0];
            int child = edge[1];
            
            if(node[parent] == null) node[parent] = new Node(parent);
            if(node[child] == null) node[child] = new Node(child);
            
            if(node[parent].left == null){
                node[parent].left = node[child];
            } else {
                node[parent].right = node[child];
            }
            
        }
        
        for(int i = 0; i < N; i++){
            node[i].sheep = info[i] == 0 ? true : false;
        }
        
        visited[0] = true;
        dfs(node, node[0], visited, shouldVisit, 1, 0);
        
        return answer;
    }
}