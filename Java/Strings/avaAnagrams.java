package Java.Strings;

import java.util.Scanner;

public class avaAnagrams {
     static boolean isAnagram(String a,String b){
        if(a == null || b == null || a.length()!=b.length()){
            return false;
        }
         a = a.toLowerCase();
        b = b.toLowerCase();
        int[] fre=new int[26];
        for(int i=0;i<a.length();i++){
            fre[a.charAt(i)-'a']++;
            fre[b.charAt(i)-'a']--;
        }
          for (int f :fre) {
            if (f != 0) {
                return false;
            }
        }
        
        return true;
    }
    

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        sc.close();
        
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
