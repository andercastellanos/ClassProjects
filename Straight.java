// Ariel

public class Straight extends HandCategory { // Declare a class named "Straight" that extends the "HandCategory" class.
    Rank highest; // Declare an enum variable of type Rank

    public Straight(Rank highest) { // Constructor of the Straight class that accepts a single argument: the highest rank card in a Straight deck.
        this.highest = highest;
        // this.highest is an instance variable of the Straight class. Assigns the value of the highest parameter (the value passed into the constructor) to the highest instance variable of the current Straight object.
    }

    @Override // Overrides the method from the superclass
    public String toString() {
        return "Straight [highest=" + highest + "]";
        // Returns a string that contains the highest rank.
    }

    @Override // Overrides the method from the superclass
    int compareRank(Object right0) { // Takes an argument of type Object named right0 and compares the rank of the current object with the rank of another object by returning an integer. Used in determining which hand is stronger in a game.
        // Try to cast the right0 object to the Straight class.
        Straight right = (Straight) right0;
        // Compares Rank of two Straight objects by providing an integer value.
        return highest.compareTo(right.highest); 
    }

    @Override // Overrides the method from the superclass
    int category() { // Simple method to return the category code for Straight.
        return 6;
    }

}
