// Define a Java class named RoyalFlush that represents the "Royal Flush" poker hand category
public class RoyalFlush extends HandCategory {
// Instance variable to store the suit of the Royal Flush
Suit suit;
    // Constructor that initializes the RoyalFlush object with a suit
    public RoyalFlush(Suit suit) {
        this.suit = suit;
    }
   
    // Override the toString method to provide a custom string representation of the RoyalFlush object
    @Override
    public String toString() {
        return "RoyalFlush [suit=" + suit + "]";
    }
    
    // Override the compareRank method to compare RoyalFlush objects based on the suit
    @Override
    int compareRank(Object right0) {
        // Cast the right object to RoyalFlush
        RoyalFlush right = (RoyalFlush) right0;
        // Compare the suits using the compareTo method of the Suit class
        return suit.compareTo(right.suit);
    }

    // Override the category method to return the category code for Royal Flush
    @Override
    int category() {
        return 1;
    }

}
