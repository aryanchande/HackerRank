import java.io.*;
import java.util.*;

public class javaOutputFormat {

    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();
            
            // This is the line you need to add/complete
            System.out.printf("%-15s%03d%n", s1, x);
        }
        
        System.out.println("================================");
        sc.close();
    }
}