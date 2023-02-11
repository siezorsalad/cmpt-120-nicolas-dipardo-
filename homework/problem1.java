import java.util.Scanner;
public class problem2 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        double windChill, temperature, windSpeed;

        //collect user input 
        System.out.println("Enter a temperature in Fahrenheit between -58F and 41F: ");
        temperature = scan.nextDouble();
            if (temperature > 41){
                System.out.println("The temperature range is out of range");
                    return;
            }else if (temperature < -58){
                System.out.println("The temperature range is out of range");
                    return;
            }

        System.out.println("Enter the wind speed (>=2) in miles per hour: ");
        windSpeed = scan.nextDouble();
            if (windSpeed < 2){
                System.out.println("The wind speed is out of range");
                    return;
            }
                
        //Calculate windchill
        windChill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * Math.pow(windSpeed, 0.16);   
        System.out.println("Wind chill is: " + windChill); 
            if (windChill >=16  && windChill <= 30){
                System.out.println("COLD. Unpleasant.");
                    return;
            } else if (windChill >=1 && windChill <= 15){
                System.out.println("VERY COLD. Very unpleasant.");
                    return;
            } else if (windChill >=-21 && windChill <= 0){
                System.out.println("BITTER COLD. forstbite possible.");
                    return;
            } else if (windChill < 0){
                System.out.println("EXTREMELY COLD. frostbite likely. outdoor activity becomes dangerous.");
                    return;

        //print out results

  
        
                
        }  
    }
}