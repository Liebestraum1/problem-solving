import java.util.*;

class Solution {
    public String solution(String s) {
        String[] strings = s.split(" ");
        int maxInt = Arrays.stream(strings).mapToInt(Integer :: parseInt).max().getAsInt();
        int minInt = Arrays.stream(strings).mapToInt(Integer :: parseInt).min().getAsInt();
        return minInt + " " + maxInt;
    }
}