import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String line1 = scanner.nextLine();
        String line2 = scanner.nextLine();
        
        String[] numbers1 = line1.split(" ");
        String[] numbers2 = line2.split(" ");
        
        int[] intNumber1 = new int[numbers1.length];
        for (int i = 0; i < numbers1.length; i++) {
            intNumber1[i] = Integer.parseInt(numbers1[i]);
        }
        
        int[] intNumber2 = new int[numbers2.length];
        for (int i = 0; i < numbers2.length; i++) {
            intNumber2[i] = Integer.parseInt(numbers2[i]);
        }
        
        scanner.close();
        
        System.out.printf("%d %d %d", intNumber2[0]-intNumber1[2], intNumber2[1]/intNumber1[1], intNumber2[2]-intNumber1[0]);
    }
}