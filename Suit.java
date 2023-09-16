// Define a Java enum type named Suit to represent card suits
public enum Suit {
    // Enum constants representing card suits
    clubs, diamonds, hearts, spades;

    // Convert a Suit enum constant to a human-readable string representation
    public String toString() {
        // Use a switch statement to map each enum constant to its corresponding string
        switch (this) {
            case clubs:
                return "Clubs";
            case diamonds:
                return "Diamonds";
            case hearts:
                return "Hearts";
            case spades:
                return "Spades";
        }
        // If an unknown enum constant is encountered, throw an exception
        throw new RuntimeException("Unknown Case");
    }
   
    // Get a string representation of the Suit enum constant (used for file sections or categorization)
    public String fileSection() {
        
        // Use a switch statement to map each enum constant to its corresponding string
        switch (this) {
            case clubs:
                return "clubs";
            case diamonds:
                return "diamonds";
            case hearts:
                return "hearts";
            case spades:
                return "spades";
        }
        // If an unknown enum constant is encountered, throw an exception
        throw new RuntimeException("Unknown Case");
    }
    
    // Get the next Suit enum constant based on the current Suit and an integer n
    public Suit next(int n) {
        // Iterate through all values of the Suit enum
        for (int i = 0; i < values().length; i++) {
            // Check if the current enum value matches 'this' (the current Suit)
            if (values()[i] == this) {
                // Return the enum value that is 'n' positions ahead in the enum
                // This effectively calculates the next Suit by adding 'n' to the current index
                return values()[i + n];
            }
        }
        // If an unknown enum constant is encountered or 'n' is out of range, throw an exception
        throw new RuntimeException("Unknown Case");
    }
}
