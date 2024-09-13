import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i = 0; i < 3; i++){
            String s = br.readLine();
            if(s.charAt(0) != 'F' && s.charAt(0) != 'B'){
                int n = Integer.parseInt(s) + 3 - i;

                if(n % 5 == 0 && n % 3 == 0){
                    System.out.println("FizzBuzz");
                } else if(n % 5 == 0){
                    System.out.println("Buzz");
                } else if(n % 3 == 0){
                    System.out.println("Fizz");
                } else{
                    System.out.println(n);
                }
                return;
            }
        }
    }
}
