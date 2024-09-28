import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    long idx = 0;

    public ArrayList<Long> calculateDigit(long a) {
        ArrayList<Long> result = new ArrayList<>();
        result.add(a % 10);

        while (true) {
            long component = (result.get((int)idx) * a) % 10;

            if (component == result.get(0)) {
                break;
            } else {
                idx += 1;
            }

            result.add(component);
        }

        return result;
    }

    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        int T = Integer.parseInt(scanner.nextLine());

        while (T-- > 0) {
            main.idx = 0;
            String line = scanner.nextLine();
            String[] input = line.split(" ");

            long a = Long.parseLong(input[0]);
            long b = Long.parseLong(input[1]);

            // a가 10의 배수인 경우
            if (a % 10 == 0) {
                System.out.println(10);
                continue;
            }

            ArrayList<Long> result = main.calculateDigit(a);
            int cycleLength = result.size();

            int position = (int)((b - 1) % cycleLength);
            System.out.println(result.get(position));
        }

        scanner.close();
    }
}
