import java.io.*;
import java.util.*;
public class JavaStdinandStdoutII {


public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        double num=sc.nextDouble();
        sc.nextLine();
        String s=sc.nextLine();
        System.out.println("String: "+ s);
        System.out.println("Double: "+ num);
        System.out.println("Int: "+ n);
        sc.close();
        
    }
}
}
