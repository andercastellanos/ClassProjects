// Ariel

public class StraightFlush extends HandCategory { // Declare a class named "StraightFlush" that extends the "HandCategory" class.
    Rank highest; // Declare an enum variable of type Rank
    Suit suit; // Declare an enum variable of type Suit

    public StraightFlush(Rank highest, Suit suit) { // Constructor of the StraightFlush class that accepts two arguments: the highest rank card in a Straight deck, and the suit.
        // Assigns the value of the highest parameter (the value passed into the constructor) to the highest instance variable of the current StraightFlush object.
        this.highest = highest;
        // Assigns the value of the suit (the value passed into the constructor) to the suit instance variable of the current StraightFlush object.
        this.suit = suit;
    }

    @Override // Overrides the method from the superclass
    public String toString() {
        return "StraightFlush [highest=" + highest + ", suit=" + suit + "]";
        // Returns a string that contains the highest rank and the suit.
    }

    @Override // Overrides the method from the superclass
    int compareRank(Object right0) { // Takes an argument of type Object named right0 and compares the rank of the current object with the rank of another object by returning an integer. Used in determining which hand is stronger in a game.
        
        // Try to cast the right0 object to the Straight class.
        StraightFlush right = (StraightFlush) right0;

        // Compares Rank of two StraightFlush objects by providing an integer value.
        int high = highest.compareTo(right.highest);

        // If the rank is the different for both StraightFlush objects, return the integer value of the comparison the Suit of both StraightFlush objects.
        if (high == 0) {
            return suit.compareTo(right.suit);
        } 
        // If the rank is the same for both StraightFlush objects, return the integer value of the comparison between the highest Ranks.
        else {
            return high;
        }

    }

    @Override // Overrides the method from the superclass
    int category() { // Simple method to return the category code for StraightFlush.
        return 2;
    }

}
