import java.util.*;

class Solution {
    public int timeParser(String time){
        String[] hourAndMinute = time.split(":");
        int hour = Integer.parseInt(hourAndMinute[0]) * 60;
        int minute = Integer.parseInt(hourAndMinute[1]);
        return hour + minute;
    }
    
    public String timeBuilder(int time){
        StringBuilder sb = new StringBuilder();
        
        int hour = time / 60;
        int minute = time % 60;
        
        if(hour < 10) {
            sb.append(0).append(hour);
        } else {
            sb.append(hour);
        }
        
        if(minute < 10){
            sb.append(":").append(0).append(minute);
        } else {
            sb.append(":").append(minute);
        }
        
        return sb.toString();
    }
    
    public String solution(int n, int t, int m, String[] timetable) {
        int answer = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        int[] intTimetable = new int[timetable.length];
        
        for(int i = 0; i < timetable.length; i++){
            intTimetable[i] = timeParser(timetable[i]);
        }
        
        Arrays.sort(intTimetable);
        
        for(int i = 0; i < timetable.length; i++){
            queue.add(intTimetable[i]);
        }
        
        for(int i = 0; i < n; i++){
            int startTime = 540 + i * t;
            int lastPassenger = 1440;
            int count = 0;
            
            while(!queue.isEmpty() && count < m){
                lastPassenger = queue.peek();
                if(lastPassenger <= startTime){
                    queue.poll();
                    count += 1;
                } else {
                    break;
                } 
            }
            
            if(count == m){
                answer = lastPassenger - 1;
            } else {
                answer = startTime;
            }
        }
        
        return timeBuilder(answer);
    }
}