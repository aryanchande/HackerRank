import java.io.*;
import java.util.*;

public class javaLoops2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        
        for (int i = 0; i < q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            
            int curr = a;
            for (int j = 0; j < n; j++) {
                curr += (1 << j) * b; 
                System.out.print(curr + " ");
            }
            System.out.println(); 
        }
        sc.close();
    }
}
