import java.io.*;
import java.util.*;

public class javaLoops1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        if (scanner.hasNextInt()) {
            int N = scanner.nextInt();
            
            for (int i = 1; i <= 10; i++) {
                System.out.printf("%d x %d = %d%n", N, i, N * i);
            }
        }
        
        scanner.close();
    }
}
