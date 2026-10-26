package Java.Strings;

import java.util.Scanner;

public class JavaStringTokens {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        if (!sc.hasNextLine()) {
            System.out.println(0);
            sc.close();
            return;
        }
        String s=sc.nextLine();
        sc.close();
        s=s.trim();
        if(s.isEmpty()){
            System.out.println(0);
            return;
        }
        String[] t=s.split("[ !,?. _'@]+");
        System.out.println(t.length);
         for (String token : t) {
            System.out.println(token);
        }
    }
}
