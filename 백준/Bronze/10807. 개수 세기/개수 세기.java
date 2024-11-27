import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        Map<Integer, Integer> mapping = new HashMap<>();
        
        for (int i = 0; i < N; i++) {
            int compo = scan.nextInt();
            if (mapping.containsKey(compo) == true) {
                mapping.put(compo, mapping.get(compo)+1);
            }
            else {
                mapping.put(compo, 1);
            }
        }
        
        int sel = scan.nextInt();
        if (mapping.containsKey(sel) == false) {
            System.out.println(0);
        }
        else {
            System.out.println(mapping.get(sel));
        }
    }
}
