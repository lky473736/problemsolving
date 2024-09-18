import java.lang.Math;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = Integer.parseInt(scanner.nextLine());
        
        for (int i = 0; i < T; i++) {
            ArrayList<Integer> nums = new ArrayList<>();
            String line = scanner.nextLine();
            String[] characters = line.split(" ");
    
            for (String compo : characters) {
                nums.add(Integer.parseInt(compo));
            }
            
            int n = nums.get(0);
            int m = nums.get(1);
            
            int cnt = 0;
            int a = 1, b = 2;
            
            while (a < n - 1) {
                if (b == n) {
                    a += 1;
                    b = a + 1;
                    if (a >= n - 1) {
                        break;
                    }
                }
                
                if ((Math.pow(a, 2) + Math.pow(b, 2) + m) % (a * b) == 0) {
                    cnt += 1;
                }
                
                b++;
            }
            
            System.out.println(cnt);
        }
        
        scanner.close();
    }
}