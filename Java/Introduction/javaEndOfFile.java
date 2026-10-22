import java.io.*;
import java.util.*;
public class javaEndOfFile {
     public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int lno=1;
        while(sc.hasNext()){
            String line=sc.nextLine();
            System.out.println(lno+" "+line);
            lno++;
        }
        sc.close();
}
}
