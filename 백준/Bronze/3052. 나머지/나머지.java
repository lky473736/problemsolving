import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int cnt = 0;
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < 10; i++) {
            set.add(scan.nextInt()%42);
        }
        System.out.println(set.size());
    }
}
