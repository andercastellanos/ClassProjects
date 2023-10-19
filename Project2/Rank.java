//    Define a java enum type name rank to represent playing cards rank 
public enum Rank {
   
    // enum constants representing card ranks
    r2, r3, r4, r5, r6, r7, r8, r9, r10, jack, queen, king, ace;

    //convert a rank enum constant to a human-readale string representation 
    public String toString() {

        //use a switch statement to map each enum constant to its corresponding string 
        switch (this) {
            case ace:
                return "Ace";
            case r2:
                return "2";
            case r3:
                return "3";
            case r4:
                return "4";
            case r5:
                return "5";
            case r6:
                return "6";
            case r7:
                return "7";
            case r8:
                return "8";
            case r9:
                return "9";
            case r10:
                return "10";
            case jack:
                return "Jack";
            case queen:
                return "Queen";
            case king:
                return "King";
        }

        //if an unknown enum constant is encountered, throw an exception 
        throw new RuntimeException("Unknown Case");
    }

    //get an string representation of the rank enum constant (used for file selection or categorization)
    public String fileSection() {
        switch (this) {
            case ace:
                return "ace";
            case r2:
                return "2";
            case r3:
                return "3";
            case r4:
                return "4";
            case r5:
                return "5";
            case r6:
                return "6";
            case r7:
                return "7";
            case r8:
                return "8";
            case r9:
                return "9";
            case r10:
                return "10";
            case jack:
                return "jack";
            case queen:
                return "queen";
            case king:
                return "king";
        }

        //if an unknown enum constant is encountered, throw an exception 
        throw new RuntimeException("Unknown Case");
    }

    //get the next rank in the enum based on the current rank and integer n
    public Rank next(int n) {
        // Iterate through all values of the 'Rank' enum
        for (int i = 0; i < values().length; i++) {
            // Check if the current enum value matches 'this' (the current rank)
            if (values()[i] == this) {
            // Return the enum value that is 'n' positions ahead in the enum
            // This effectively calculates the next rank by adding 'n' to the current index
                return values()[i + n];
            }
        }

        //if an unknown enum constant is encountered, throw an exception 
        throw new RuntimeException("Unknown Case");
    }

    // inclusive
    //get an array of rank enums representing a range from lower to higher 
    public static Rank[] range(Rank lower, Rank higher) {
        // Initialize a counter to keep track of the number of ranks in the range
        int count = 0;
        // Start with the lower rank
        Rank current = lower;
        // Iterate through ranks until the 'higher' rank is reached
        while (current != higher) {
            // Increment the count for each rank encountered
            count++;
            // Move to the next rank using the 'next' method
            current = current.next(1);
        }
        // Create an array to store the ranks in the range (plus one for 'higher' rank)
        Rank[] result = new Rank[count + 1];
        // Initialize an index variable for populating the 'result' array
        for (int i = 0; i < count; i++) {
            // Set the current rank in the 'result' array
            result[i] = lower;
            // Move to the next rank using the 'next' method
            lower = lower.next(1);
        }
        // Assign the 'higher' rank to the last element of the 'result' array
        result[count] = higher;
        // Return the array containing the ranks in the specified range
        return result;
    }

}
