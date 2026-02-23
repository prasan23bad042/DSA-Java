import java.util.*;

public class Codechef {

    // Method to generate a random number between 1 and 100
    public static int getRandomNumber() {
        Random rand = new Random();
        return rand.nextInt(100) + 1;
    }

    // Method to provide hints based on the user's guess
    public static String giveHint(int number, int guess) {

        if (guess == number) {
            return "Right";
        }

        if (Math.abs(guess - number) <= 10) {
            return "Hot";
        }

        return "Cold";
    }

    // Method to run the guessing game
    public static void runGuess() {

        int secretNumber = getRandomNumber();
        Scanner scanner = new Scanner(System.in);

        while (true) {   // loop until correct guess

            System.out.print("Enter a number between 1 and 100: ");
            int userGuess = scanner.nextInt();

            String hint = giveHint(secretNumber, userGuess);

            if (hint.equals("Right")) {
                System.out.println("You guessed it right!!");
                break;   // terminate game
            } else {
                System.out.println(hint);
            }
        }

        scanner.close();
    }

    // Main method
    public static void main(String[] args) {
        runGuess();
    }
}