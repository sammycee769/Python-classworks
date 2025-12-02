import java.util.Scanner;
import java.util.Random;

public class Guess{
public static void main(String[]args){
Random rand = new Random();
Scanner input = new Scanner(System.in);
int random = rand.nextInt(1,10);
int number = 0;

while(number != random){
System.out.print("Enter a number");
number = input.nextInt();
if(number > random){
System.out.println("Number is too high");
}
if(number < random){
System.out.println("Number is too low");
}
}
if(number == random){
System.out.println("correct");}
}
}


