import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    long idx = 0;
    
    public long[] calculateDigit(long a, long b) {
        long[] result = new long[1000];
        result[(int)idx] = a;
        
        while (true) {
            long component = result[(int)idx] * a;
            
            if (component % 10 == result[0]) {
                break;
            }
            
            else {
                idx += 1;
            }
            
            result[(int)idx] = component % 10;
        }
        
        // System.out.println(result);
        
        return result;
    }

    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        long T = Long.parseLong(scanner.nextLine());

        while (T-- > 0) {
            main.idx = 0;
            ArrayList<Long> nums = new ArrayList<>();
            String line = scanner.nextLine();
            String[] characters = line.split(" ");

            for (String compo : characters) {
                nums.add(Long.parseLong(compo));
            }

            if (nums.size() == 2) {
                long a = nums.get(0);
                long b = nums.get(1);
                
                long[] result = main.calculateDigit(a, b);
                
                if (result.length > 0) {
                    // System.out.println(b);
                    // System.out.println(main.idx);
                    if (main.idx == 0) {
                        System.out.println(result[0]);
                        continue;
                    }
                    
                    if (main.idx < b) {
                        if ((int)(b - (main.idx+1) * (b/(main.idx+1))) - 1 < 0) {
                            System.out.println(result[(int)(b - (main.idx+1) * (b/(main.idx+1) -1))-1]);
                            continue;
                        }
                        
                        System.out.println(result[(int)(b - (main.idx+1) * (b/(main.idx+1))) - 1]);
                    }
                    
                    else {
                        System.out.println(result[(int)(b - 1)]);
                    }
                }
            }
        }
        
        scanner.close();
    }
}
