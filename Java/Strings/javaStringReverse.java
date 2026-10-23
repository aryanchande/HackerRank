package Java.Strings;

import java.util.Scanner;

public class javaStringReverse {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String a=sc.next();
        sc.close();
        String r=new StringBuilder(a).reverse().toString();
        if(a.equals(r)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
