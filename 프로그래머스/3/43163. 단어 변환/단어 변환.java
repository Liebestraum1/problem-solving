import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        final int GRAPH_SIZE = words.length + 1;
        final int WORD_SIZE = words[0].length();
        
        boolean[] visited = new boolean[GRAPH_SIZE];
        String[] w = new String[GRAPH_SIZE];
        List<Integer>[] graph = new List[GRAPH_SIZE];
        
        w[0] = begin;
        for(int i = 1; i < GRAPH_SIZE; i++){
            w[i] = words[i - 1];
        }
        
        for(int i = 0; i < GRAPH_SIZE; i++){
            graph[i] = new ArrayList<Integer>();
        }
        
        for(int i = 0; i < GRAPH_SIZE; i++){
            String curWord = w[i];
            for(int j = 0; j < GRAPH_SIZE; j++){
                String nextWord;
                int count = 0;

                nextWord = w[j];
                
                for(int c = 0; c < WORD_SIZE; c++){
                    if(curWord.charAt(c) != nextWord.charAt(c)){
                        count += 1;
                    }
                }
                
                if(count == 1){
                    graph[i].add(j);
                }                
            }
        }
        
        Queue<Integer> queue = new ArrayDeque<>();
        
        queue.add(0);
        visited[0] = true;
        
        int answer = Integer.MAX_VALUE;
        int depth = 0;
        int cnt = 0;
        int queueSize = 1;
        
        while(!queue.isEmpty()){
            int curNode = queue.poll();
            cnt += 1;
            
            if(target.equals(w[curNode])){
                answer = Integer.min(depth, answer);
            }
            
            for(int nextNode : graph[curNode]){
                if(!visited[nextNode]){
                    visited[nextNode] = true;
                    queue.add(nextNode);
                }
            }
            
            if(cnt == queueSize){
                depth += 1;
                cnt = 0;
                queueSize = queue.size();
            }
        }
        
        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
}