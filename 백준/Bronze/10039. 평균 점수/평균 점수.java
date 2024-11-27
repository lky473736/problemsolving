import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr = new int[5];
        
        for (int i = 0; i < arr.length; i++) {
            int compo = scan.nextInt();
            
            if (compo <= 40) {
                compo = 40;
            }
            
            else {
                ;
            }
            
            arr[i] = compo;
        }
        
        int suma = 0;
        for (int i = 0; i < arr.length; i++) {
            suma += arr[i];
        }
        
        System.out.println(suma/arr.length);
    }
}
