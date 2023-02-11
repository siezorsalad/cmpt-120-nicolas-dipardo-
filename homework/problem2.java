import java.util.Scanner;
import java.util.Math;
public class problem1 {
    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a whole number: ");

        int n = scan.nextInt();
        
        if( n < 0 ) {
            System.out.println(n * n);
        } else if(n > 0) {
            System.out.println(java.lang.Math.sqrt(n));
        } else if(n == 0) {
            System.out.println("The number is 0");
        } else {
            System.out.println("Enter a valid number");
        


        }


    }
    
}
