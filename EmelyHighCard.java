import java.util.Arrays;

public class HighCard extends HandCategory {
    Rank[] ranks; // Array to store the ranks of the high card hand

    // Constructor to initialize a HighCard hand with an array of ranks
    public HighCard(Rank[] ranks) {
        this.ranks = ranks;
    }

    // Override the toString method to provide a custom string representation of the HighCard hand
    @Override
    public String toString() {
        return "HighCard [ranks=" + Arrays.toString(ranks) + "]";
    }

    // Override the compareRank method to compare the rank of this HighCard hand with another HighCard hand
    @Override
    int compareRank(Object right0) {

        // Cast the right0 object to a HighCard object
        HighCard right = (HighCard) right0;
        // Compare the ranks of cards from highest to lowest (index 4 to 0 in the ranks array)
        for (int i = 4; i > 0; i--) {
            int high = ranks[i].compareTo(right.ranks[i]);
            if (high != 0) {
                return high; // Return the results if ranks are not equal
            }
        }
        // If all ranks are equal, compare the ranks of the first cards (index 0)
        return ranks[0].compareTo(ranks[0]);
    }

    // Override the category method to specify the category value for HighCard
    @Override
    int category() {
        return 10; // Return a category value of 10 for HighCard hands
    }

}
