public class OnePair extends HandCategory { //: This line declares a Java class named OnePair that extends another class called HandCategory
    Rank highest; //This line declares an instance variable named highest of type Rank. It represents the rank of the pair of cards in a "One Pair" hand.

    // Contractor 
    public OnePair(Rank highest) { //This is the constructor of the OnePair class. It takes a parameter of type Rank named highest and assigns it to the highest instance variable. This constructor is used to initialize OnePair objects.
        this.highest = highest;
    }

    //Custom string representation
    @Override //This annotation indicates that the methods below are intended to override methods from a superclass.
    public String toString() { //This method overrides the toString() method from the superclass Object. It provides a custom string representation of a OnePair object, including the highest rank.
        return "OnePair [highest=" + highest + "]";
    }

    //Compare two OnePair objects based on the rank of the pair 
    @Override ////This annotation indicates that the methods below are intended to override methods from a superclass.
    int compareRank(Object right0) { //This method overrides the compareRank() method from the superclass HandCategory. It compares two OnePair objects based on the rank of the pair (highest attribute) and returns the result using the compareTo() method of the Rank class.

        OnePair right = (OnePair) right0;
        return highest.compareTo(right.highest);
    }


    //Get the category code for OnePair 
    @Override //This annotation indicates that the methods below are intended to override methods from a superclass.
    int category() { //This method overrides the category() method from the superclass HandCategory. It returns the integer value 9, which seems to represent the category code for "One Pair" in a poker hand ranking system.
        // TODO Auto-generated method stub
        return 9;
    }

}
