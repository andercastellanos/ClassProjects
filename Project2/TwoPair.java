// Define a Java class named TwoPair that represents the "Two Pair" poker hand category
public class TwoPair extends HandCategory {
    // Instance variables to store the ranks of the higher and lower pairs
    Rank higher;
    Rank lower;

    // Constructor that initializes a TwoPair object with two Rank values for higher and lower pairs
    public TwoPair(Rank higher, Rank lower) {
        this.higher = higher;
        this.lower = lower;
    }

    // Override the toString method to provide a custom string representation of the TwoPair object    
    @Override
    public String toString() {
        // Construct and return a string that includes the class name, and the values of 'higher' and 'lower'
        return "TwoPair [higher=" + higher + ", lower=" + lower + "]";
    }

    // Override the compareRank method to compare TwoPair objects based on ranks of higher and lower pairs
    @Override
    int compareRank(Object right0) {
        // Cast the right object to TwoPair
        TwoPair right = (TwoPair) right0;
        // Compare the ranks of the higher pairs using the compareTo method of the Rank class
        int high = higher.compareTo(right.higher);
        // If the ranks of the higher pairs are equal, compare the ranks of the lower pairs
        if (high == 0) {
            return lower.compareTo(right.lower);
        } else {
            return high;
        }
    }

    // Override the category method to return the category code for Two Pair
    @Override
    int category() {
        return 8;
    }

}
