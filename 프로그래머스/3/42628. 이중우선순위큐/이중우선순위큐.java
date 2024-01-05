import java.util.*;

class DoublePQ {
    TreeMap<Integer, Integer> data = new TreeMap<>();
    
    void insert(int num){
        if(!data.containsKey(num)){
            data.put(num, 1);
        } else {
            data.put(num, data.get(num) + 1);
        }
    }
    
    boolean isEmpty(){
        if(data.isEmpty()){
            return true;
        }
        return false;
    }
    
    int poll(){
        int head = data.firstKey();
        int count = data.get(head) - 1;
        if(count == 0){
            data.remove(head);
        } else {
            data.replace(head, count);
        }
        return head;
    }
    
    int pop() {
        int tail = data.lastKey();
        int count = data.get(tail) - 1;
        if(count == 0){
            data.remove(tail);
        } else {
            data.replace(tail, count);
        }
        return tail;
    }
}

class Solution {
    public int[] solution(String[] operations) {
        DoublePQ dpq = new DoublePQ();
        int[] answer = new int[2];
        
        for(String operation : operations){
            StringTokenizer st = new StringTokenizer(operation);
            String operator = st.nextToken();
            int operand = Integer.parseInt(st.nextToken());
            
            if(operator.equals("I")){
                dpq.insert(operand);
            } else if(!dpq.isEmpty() && operand == 1){
                dpq.pop();
            } else if(!dpq.isEmpty() && operand == -1){
                dpq.poll();
            }
        }
        
        if(dpq.data.size() == 0){
            answer[0] = 0;
            answer[1] = 0;
        } else if(dpq.data.size() == 1){
            int num = dpq.poll();
            answer[0] = num;
            answer[1] = num;
        } else {
            answer[0] = dpq.pop();
            answer[1] = dpq.poll();
        }
        
        return answer;
    }
}