import java.io.*;
import java.util.*;

public class javaIntToString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        sc.close();
        
        // Convert the integer to a String
        String s = Integer.toString(a);
        
        // Challenge verification logic
        if (a == Integer.parseInt(s)) {
            System.out.println("Good job");
        } else {
            System.out.println("Wrong answer");
        }
    }
}
