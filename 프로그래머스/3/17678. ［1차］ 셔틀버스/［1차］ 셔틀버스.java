import java.util.*;

class Solution {
    public int timeParser(String time){
        String[] hourAndMinute = time.split(":");
        int hour = Integer.parseInt(hourAndMinute[0]) * 60;
        int minute = Integer.parseInt(hourAndMinute[1]);
        return hour + minute;
    }
    
    public String timeBuilder(int time){
        int hour = time / 60;
        int minute = time % 60;
        return String.format("%02d:%02d", hour, minute);
    }
    
    public String solution(int n, int t, int m, String[] timetable) {
        int answer = 0;
        int index = 0;
        final int SIZE = timetable.length;
        int[] intTimetable = new int[SIZE];
        
        for(int i = 0; i < SIZE; i++){
            intTimetable[i] = timeParser(timetable[i]);
        }
        
        Arrays.sort(intTimetable);
        
        for(int i = 0; i < n; i++){
            int startTime = 540 + i * t;
            int lastPassenger = 1440;
            int count = 0;
            
            while(index < SIZE && count < m){
                lastPassenger = intTimetable[index];
                if(lastPassenger <= startTime){
                    index += 1;
                    count += 1;
                } else {
                    break;
                } 
            }
            answer = count == m ? lastPassenger - 1 : startTime;
        }
        return timeBuilder(answer);
    }
}