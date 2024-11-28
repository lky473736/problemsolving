import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();  // 입력을 받습니다.
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);  // 문자열에서 i번째 문자를 가져옵니다.
            
            // 대문자일 경우 소문자로 변환하여 출력
            if (Character.isUpperCase(ch)) {
                System.out.print(Character.toLowerCase(ch));
            }
            // 소문자일 경우 대문자로 변환하여 출력
            else if (Character.isLowerCase(ch)) {
                System.out.print(Character.toUpperCase(ch));
            }
        }
    }
}
