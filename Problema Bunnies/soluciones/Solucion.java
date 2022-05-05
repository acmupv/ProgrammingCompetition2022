import java.util.Scanner;

public class Bunnies {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();

        for(int i = 0; i < cases; i++){
            String fila = sc.nextLine(); // palabra a analizar
            boolean validRow = validPalindrome(fila); 
            if(validRow){
                System.out.println("conejos bien ubicados");
            }
            else{
                System.out.println("demasiados conejos deben reubicarse");
            }
            
        }
        sc.close();
    }

    public static boolean validPalindrome(String s) {
        int p1 = 0; int p2 = s.length() - 1;
        while(p1 < p2){
            if(s.charAt(p1) != s.charAt(p2)){
                return recvalidPalindrom(s, p1, p2 - 1) || recvalidPalindrom(s, p1 + 1, p2);
            }
            p1++;
            p2--;
        }
        return true;
    }
    protected static boolean recvalidPalindrom(String s, int p1, int p2){
        if(s.length() < 2){ return true; }
        while(p1 < p2){
            if(s.charAt(p1++) != s.charAt(p2--)){ return false; }
        }
        return true;
    }

}

