import java.util.*;

class Solution{
    public boolean palindrome(List<Character> str){
        for(int i = 0; i < str.size() / 2 + 1; i++){
            if(str.get(i) != str.get(str.size() - i - 1)){
                return false;
            }
        }
        return true;
    }
    
    public int solution(String s){
        int answer = 0;
        
        List<Character> str = new ArrayList<>();
        
        for(int i = 0; i < s.length(); i++){
            if(s.length() - i < answer){
                continue;
            }
            
            str.clear();
            for(int j = i; j < s.length(); j++){    
                str.add(s.charAt(j));
                
                if((j - i) < answer){
                    continue;
                }
                
                if(palindrome(str)){
                    answer = j - i + 1;
                }
            }
        }
        return answer;
    }
}