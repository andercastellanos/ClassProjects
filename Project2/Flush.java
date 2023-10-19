public class Flush extends HandCategory { // Declare a class named "Flush" that inherits from another class named "HandCategory"
    
    Rank highest; // Declare a variable "highest" of type "Rank" to store the highest card in the flush

    public Flush(Rank highest) { // Declare a constructor "Flush" that takes a "Rank" object as an argument and initializes AS "highest"
        this.highest = highest; // Assign the parameter "highest" to the member variable "highest"
    }

    @Override   // Override the "toString" method from the Object class to display the highest rank in the flush
    public String toString() {
        return "Flush [highest=" + highest + "]"; // returns a string that starts with "Flush [highest=", followed by the highest rank contained in this Flush object.
    } //This is the body of the method, and it specifies what string to return. 

    @Override 
    int compareRank(Object right0) { // declares an int to take an object as an argument 
        Flush right = (Flush) right0;
        return highest.compareTo(right.highest); // line uses compareTo method of "RANK" of the "Flush" Object
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 5; // methods return an int (5) indicating the category type for a Flush hand
    }

}
